import datetime

import crud
import models
from dependancy import SessionDependency
from fastapi import FastAPI
from lifespan import lifespan
from models import Session
from schema import (CreateAdvirtesmentRequest, CreateAdvirtesmentResponse, DeleteAdvirtesmentResponse,
                    GetAdvirtesmentResponse, SearchAdvirtesmentResponse, UpdateAdvirtesmentRequest,
                    UpdateAdvirtesmentResponse)
from sqlalchemy import select


app = FastAPI(
    Description="Advertisements API",
    terms_of_service="",
    description="list of Advertisements",
    lifespan=lifespan,
)

@app.post("/advertisement", tags=['advertisment_post'], response_model=CreateAdvirtesmentResponse)
async def create_advertisement(advertisment: CreateAdvirtesmentRequest, session: SessionDependency):
    advertisment_dict = advertisment.model_dump(exclude_unset=True)
    advertisment_orm_obj = models.Advertisment(**advertisment_dict)
    await crud.add_item(session, advertisment_orm_obj)
    return advertisment_orm_obj.id_dict


@app.get("/advertisement/{advertisment_id}", tags=['advertisment_get'], response_model=GetAdvirtesmentResponse)
async def get_advertisement(advertisment_id: int, session: SessionDependency):
    advertisment_orm_obj = await crud.get_item_by_id(session, models.Advertisment, advertisment_id)
    return advertisment_orm_obj.dict


@app.patch("/advertisement/{advertisment_id}", tags=["advertisement_patch"], response_model=UpdateAdvirtesmentResponse)
async def update_advertisement(
    advertisment_id: int,
    updated_data: UpdateAdvirtesmentRequest,
    session: SessionDependency
):
    updated_data_dict = updated_data.model_dump(exclude_unset=True)
    advertisment_orm_obj = await crud.get_item_by_id(session, models.Advertisment, advertisment_id)
    for fields, value in updated_data_dict.items():
        setattr(advertisment_orm_obj, fields, value)
    await crud.add_item(session, advertisment_orm_obj)
    return {"status": "success"}

@app.delete("/advertisement/{advertisment_id}", tags=["advertisement_delete"], response_model=DeleteAdvirtesmentResponse)
async def delete_advertisement(advertisment_id: int, session: SessionDependency):
    advertisment_orm_obj = await crud.get_item_by_id(session, models.Advertisment, advertisment_id)
    await crud.delete_item(session, advertisment_orm_obj)
    return {"status": "success"}

@app.get("/advertisement", response_model=SearchAdvirtesmentResponse)
async def search_advirtesment(session: SessionDependency, title: str):
    query = (
        select(models.Advertisment)
        .where(models.Advertisment.title == title)
        .limit(10000)
    )
    advertisments = await session.scalars(query)
    return {"results": [advertisment.dict for advertisment in advertisments]}