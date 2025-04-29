def param_setup(search_type,search_info=None):
    if search_type == ("by_actor"):
        params = {"page": 1, "limit": 250,"persons.id" : search_info, "notNullFields": ("id", "name", "poster.url", "description", "year", "countries.name", "genres.name", "rating.kp")}
    elif search_type == "actor":
        params = {"page": 1, "limit": 25,"query": search_info, "notNullFields": ("id", "name", "photo")}
    elif search_type == "random":
        params = {"notNullFields": ("id", "name", "poster.url", "description", "year", "countries.name", "genres.name", "rating.kp")}
    return params