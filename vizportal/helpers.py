from vizportal.pager import VizportalPager


def merge_results_by_keys(
    results: VizportalPager | list[dict], keys: str | list[str]
) -> dict:
    """Merges paged results by key. 
    This is useful for combining nested lists from multiple page results into a single object.

    Args:
    -----
        results : VizportalPager | list)
            The results to merge.
        keys (str | list[str]):
            The keys to merge.

    Returns:
    --------
        dict: The merged results.

    Example:
    --------
        merge_results_by_keys(results, ["workbooks", "projects", "users"])
        >>> {"workbooks": [...], "projects": [...], "users": [...]}
    """
    merged_results = {}
    if isinstance(keys, str):
        keys = [keys]
    if isinstance(results, VizportalPager):
        results = list(results)

    for key in keys:
        # Initialize a new list for this key.
        merged_results[key] = []
        for result in results:
            if len(result.keys()) > 2:
                if not isinstance(result, dict):
                    raise TypeError(
                        f"Result is not a dict. Found type: {type(result)}"
                    )
                # Check that the key exists.
                if key not in list(result.keys()):
                    raise ValueError(
                        f"Key {key} not found in result. Found Keys: {list(result.keys())}"
                    )
                key_results = result[key]
                if isinstance(key_results, list):
                    merged_results[key].extend(key_results)
                else:
                    merged_results[key].append(key_results)
    # Return the merged results.
    return merged_results
