import h3
from geojson import Polygon, Feature, FeatureCollection


def get_h3_cells(geojson_in, resolution):
    hexids = list(h3.polyfill(geojson_in, res=resolution, geo_json_conformant=True))

    return hexids


def ids_to_geojson(h3_ids):
    features = []
    for hex in h3_ids:
        my_feature = Feature(geometry=Polygon([h3.h3_to_geo_boundary(h=hex, geo_json=True)]))
        features.append(my_feature)

    feature_collection = FeatureCollection(features)

    return feature_collection
