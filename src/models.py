from typing import Optional

from pydantic import BaseModel


class TrafficModel(BaseModel):
    id: Optional[int]
    customer_name: str
    ip: Optional[str]
    date: Optional[str]
    received_traffic: Optional[float]
