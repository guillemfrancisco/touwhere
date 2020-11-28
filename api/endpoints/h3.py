from fastapi import APIRouter, Query
from pydantic.types import Json

from api.schemas.h3 import H3, H3GeoJSON
from api.utils import geospatial

router = APIRouter()


@router.get("/ids", response_model=H3)
def get_h3(
    geofence_in: Json = Query(..., description='Geofence GeoJSON format')
):
    h3_ids = geospatial.get_h3_cells(geojson_in=geofence_in["geometry"], resolution=11)
    ans = dict()
    ans["ids"] = h3_ids

    return ans


@router.get("/geojson", response_model=H3GeoJSON)
def get_h3_geojson(
    geofence_in: Json = Query(..., description='Geofence GeoJSON format')
):
    h3_ids = geospatial.get_h3_cells(geojson_in=geofence_in["geometry"], resolution=11)
    collection = geospatial.ids_to_geojson(h3_ids)

    print(collection)

    return collection
