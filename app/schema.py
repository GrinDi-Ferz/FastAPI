import datetime
from typing import Literal

from pydantic import BaseModel


class IdResponse(BaseModel):
    id: int


class SuccessResponse(BaseModel):
    status: Literal["success"]


class CreateAdvirtesmentRequest(BaseModel):
    title: str
    description: str = None
    price: int = None
    author: str


class CreateAdvirtesmentResponse(IdResponse):
    pass


class UpdateAdvirtesmentRequest(BaseModel):
    title: str
    description: str = None
    price: int = None
    author: str

class UpdateAdvirtesmentResponse(SuccessResponse):
    pass


class GetAdvirtesmentResponse(BaseModel):
    id: int
    title: str
    description: str = None
    price: int = None
    author: str
    create_date: datetime.datetime


class SearchAdvirtesmentResponse(BaseModel):
    results: list[GetAdvirtesmentResponse]


class DeleteAdvirtesmentResponse(SuccessResponse):
    pass