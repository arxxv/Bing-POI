def bing_query(long, lat, rad, entity, BING_MAPS_KEY, base_url):
    import requests

    query_components = "EntityID,DisplayName,Phone,Latitude,Longitude"

    query = "spatialFilter=nearby(" + lat + "," + long + "," + str(rad) + ")&$filter=EntityTypeID%20eq%20'" + str(entity) +  "'&key=" + BING_MAPS_KEY + "&$format=json"

    res = requests.get(base_url + query)
    return res.json()
