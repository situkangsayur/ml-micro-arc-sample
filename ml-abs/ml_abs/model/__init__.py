import datetime
from typing import Any, Dict, List
from pydantic import BaseModel

from pydantic.types import UUID5

class Model(BaseModel):

    id_model: UUID5 | None
    dataset_name: str | None
    method_detail: Dict[Any, Any] | None
    pipeline: List[Dict[Any, Any]] | None
    feature_seq: List[str] | None
    version: str | None
    created_at: datetime.datetime = datetime.datetime.now()


