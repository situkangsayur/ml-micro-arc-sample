from typing import Any, Dict
from fastapi import APIRouter

fraud = APIRouter(tags=['Fraud'])

@fraud.post('/training')
async def training() -> Dict[Any, Any]:
    return {'model': 'under construction'}

@fraud.post('/predict')
async def predict() -> Dict[Any, Any]:
    return {'model': 'under construction'}

@fraud.get('/model')
async def model() -> Dict[Any, Any]:
    return {'model': 'under construction'}



