from vizportal import (
    VizportalRequestOptions,
    FilterClauseBuilder,
    PayloadBuilder,
    VizportalPager,
    Endpoints,
)
from vizportal.helpers import merge_results_by_keys
import tableauserverclient as TSC

import argparse
import logging


def lookup_owner(workbook, all_users):
    owner_id = workbook.owner_id
    owner = next((user for user in all_users if user.id == owner_id), None)
    return owner

def lookup_project(workbook, all_projects):
    project_id = workbook.project_id
    project = next((project for project in all_projects if project.id == project_id), None)
    return project

def main():
    parser = argparse.ArgumentParser(description="Explore workbook functions supported by the Server API.")
    # Common options; please keep those in sync across all samples
    parser.add_argument("--server", "-s", required=True, help="server address")
    parser.add_argument("--site", "-S", help="site name")
    parser.add_argument(
        "--token-name", "-p", required=True, help="name of the personal access token used to sign into the server"
    )
    parser.add_argument(
        "--token-value", "-v", required=True, help="value of the personal access token used to sign into the server"
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
    tableau_auth = TSC.PersonalAccessTokenAuth(args.token_name, args.token_value, site_id=args.site)

    with server.auth.sign_in_with_personal_access_token(tableau_auth):
        # create a payload object
        payload = PayloadBuilder()

        # add the method
        payload.add_method(Endpoints.Get.Workbooks)

        # add the page
        payload.add_page(start_index=0, max_items=500)

        # create a filter object
        payload_filter = FilterClauseBuilder()

        # add the clauses
        payload_filter.add_clause(
            VizportalRequestOptions.Operator.Equals,
            VizportalRequestOptions.Field.WorkbookConnFilter,
            VizportalRequestOptions.DatasourceType.Live,
        )

        # add the filter to the payload
        payload.add_filter(payload_filter)

        # check the payload
        print(payload)

        results = merge_results_by_keys(
            VizportalPager(server, payload), ["workbooks", "projects", "users"]
        )

        all_workbooks = results["workbooks"]
    
        for wokbook in all_workbooks:
            wokbook['owner'] = lookup_owner(wokbook, results['users'])
            wokbook['project'] = lookup_project(wokbook, results['projects'])

        print(all_workbooks)

if __name__ == "__main__":
    main()