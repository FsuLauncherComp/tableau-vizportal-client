from vizportal import PayloadBuilder, VizPortalCall
import tableauserverclient as TSC

import uuid
import argparse
import logging


def main():
    parser = argparse.ArgumentParser(
        description="Create a personal access token for a user. Must use Server Admin credentials."
    )
    # Common options; please keep those in sync across all samples
    parser.add_argument("--server", "-s", required=True, help="server address")
    parser.add_argument("--site", "-S", help="site name")
    parser.add_argument(
        "--username",
        "-p",
        required=True,
        help="name of the personal access token used to sign into the server",
    )
    parser.add_argument(
        "--password",
        "-v",
        required=True,
        help="value of the personal access token used to sign into the server",
    )
    parser.add_argument(
        "--target-username",
        "-tu",
        required=True,
        help="The user you want to create a PAT for",
    )
    parser.add_argument(
        "--pat_name",
        "-pn",
        required=False,
        default=str(uuid.uuid4()),
        help="The name of the PAT you want to create",
    )
    parser.add_argument(
        "--logging-level",
        "-l",
        choices=["debug", "info", "error"],
        default="error",
        help="desired logging level (set to error by default)",
    )

    args = parser.parse_args()

    # Set logging level based on user input, or error by default
    logging_level = getattr(logging, args.logging_level.upper())
    logging.basicConfig(level=logging_level)

    server = TSC.Server(args.server)
    server.version = "3.11"
    server.add_http_options({"verify": False})

    admin_auth = TSC.TableauAuth(args.username, args.password, site_id=args.site)

    with server.auth.sign_in(admin_auth):
        user_id = find_user_by_name(server, args.targer_username)
        print(f"Found user with id {user_id}")

    with server.auth.sign_in(
        create_tableau_auth_impersonation(args.username, args.password, args.site, user_id)
    ):
        pat_payload = create_pat_payload(args.pat_name)
        pat_response = create_pat_token(server, pat_payload)
        print(f"user_id: {user_id} | response: {pat_response}")


def create_pat_payload(pat_name: str) -> dict:
    payload = PayloadBuilder()
    payload.add_method("createPersonalAccessToken")
    payload.add_param("clientId", pat_name)
    logging.debug(payload)
    return payload


def find_user_by_name(server: TSC.Server, user_name: str) -> str:
    """Finds the user id by name. Usernames are unique in Tableau"""
    request_options = TSC.RequestOptions()
    request_options.filter.add(
        TSC.Filter(
            TSC.RequestOptions.Field.Name, TSC.RequestOptions.Operator.Equals, user_name
        )
    )
    logging.debug(f"Request options: {request_options}")
    all_users, pagination_item = server.users.get(request_options)
    user_id = all_users[0].id
    logging.debug(f"Found user with id {user_id}")
    return user_id


def create_pat_token(server: TSC.Server, payload: dict) -> str:
    """Creates a PAT token for the user"""
    logging.debug("Creating PAT token")
    pat_response = VizPortalCall(server).make_request(payload)
    result = pat_response["result"]
    return result

def create_tableau_auth_impersonation(
    username: str, password: str, site: str, user_id: str = None
) -> TSC.TableauAuth:
    """Creates a Tableau Auth object as the user"""
    logging.debug("Creating Tableau Auth as user with id {user_id}")
    server_auth = TSC.TableauAuth(
        username,
        password,
        site_id=site,
        user_id_to_impersonate=user_id,
    )
    return server_auth

if __name__ == "__main__":
    main()
