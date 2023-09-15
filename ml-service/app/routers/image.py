from typing import Any, Dict
from fastapi import APIRouter

image = APIRouter(tags=['Image'])

@image.post('/training')
async def training() -> Dict[Any, Any]:
    return {'model': 'under construction'}

@image.post('/predict')
async def predict() -> Dict[Any, Any]:
    return {'model': 'under construction'}

@image.get('/model')
async def model() -> Dict[Any, Any]:
    return {'model': 'under construction'}



