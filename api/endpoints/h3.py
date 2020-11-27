from fastapi import APIRouter, Query
from pydantic.types import Json

from api.schemas import h3 as h3_schema
from api.utils import geospatial

router = APIRouter()


@router.get("/", response_model=h3_schema.H3)
def get_h3(
    geofence_in: Json = Query(..., description='Something something')
):
    h3_ids = geospatial.get_h3_cells(geojson_in=geofence_in["geometry"], resolution=11)
    ans = dict()
    ans["ids"] = h3_ids

    return ans
