import os
from fastapi import FastAPI
from .routers.image import image as image_route
from .routers.fraud import fraud as fraud_route
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

PG_USERNAME = os.getenv('PG_USERNAME')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_HOST = os.getenv('PG_HOST')
PG_PORT = os.getenv('PG_PORT')
PG_DB = os.getenv('PG_DB')

POSTGRES_URL = f"postgresql://{PG_USERNAME}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

engine = create_engine(POSTGRES_URL, echo = True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


app = FastAPI(title='Sample ML Service', 
              version='0.1.0', 
              openapi_url='/api/docs')

@app.get("/")
def root():
    return {'message': 'Hello, ML Service here!'}
    
app.include_router(image_route, prefix='/api/v1/image')
app.include_router(fraud_route, prefix='/api/v1/fraud')
