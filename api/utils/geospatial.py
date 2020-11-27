import h3


def get_h3_cells(geojson_in, resolution):
    hexids = list(h3.polyfill(geojson_in, res=resolution, geo_json_conformant=True))

    return hexids
