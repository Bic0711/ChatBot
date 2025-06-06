def param_setup(search_type, search_info):
    params = {}
    if search_type == "random":
        params["random"] = search_info
    elif search_type == "genre":
        params["genre"] = search_info
    elif search_type == "year":
        params["year"] = search_info
    elif search_type == "country":
        params["country"] = search_info
    elif search_type == "actor":
        params["actor"] = search_info
    return params
