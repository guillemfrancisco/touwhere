from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, validator
from geojson_pydantic.geometries import Polygon
from geojson_pydantic.features import FeatureCollection


class H3(BaseModel):
    ids: Optional[List[str]]


class Geofence(BaseModel):
    """Feature Model"""

    type: str = Field("Feature", const=True)
    geometry: Polygon
    properties: Optional[Dict[Any, Any]]

    class Config:
        """TODO: document"""
        use_enum_values = True

    @validator("geometry", pre=True, always=True)
    def set_geometry(cls, v):
        """set geometry from geo interface or input"""
        if hasattr(v, "__geo_interface__"):
            return v.__geo_interface__
        return v


class H3GeoJSON(FeatureCollection):
    """ H3 FeatureCollection """
