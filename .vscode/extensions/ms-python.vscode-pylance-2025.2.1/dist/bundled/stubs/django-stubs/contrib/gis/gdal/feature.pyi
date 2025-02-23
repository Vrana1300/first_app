from typing import Any

from django.contrib.gis.gdal.base import GDALBase as GDALBase

class Feature(GDALBase):
    destructor: Any = ...
    ptr: Any = ...
    def __init__(self, feat: Any, layer: Any) -> None: ...
    def __getitem__(self, index: Any) -> Any: ...
    def __len__(self) -> Any: ...
    def __eq__(self, other: object) -> Any: ...
    @property
    def encoding(self) -> Any: ...
    @property
    def fid(self) -> Any: ...
    @property
    def layer_name(self) -> Any: ...
    @property
    def num_fields(self) -> Any: ...
    @property
    def fields(self) -> Any: ...
    @property
    def geom(self) -> Any: ...
    @property
    def geom_type(self) -> Any: ...
    def get(self, field: Any) -> Any: ...
    def index(self, field_name: Any) -> Any: ...
