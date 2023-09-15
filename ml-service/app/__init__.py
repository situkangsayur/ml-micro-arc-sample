from fastapi import FastAPI
from .routers.image import image as image_route
from .routers.fraud import fraud as fraud_route


app = FastAPI(title='Sample ML Service', 
              version='0.1.0', 
              openapi_url='/api/docs')

@app.get("/")
def root():
    return {'message': 'Hello, ML Service here!'}
    
app.include_router(image_route, prefix='/api/v1/image')
app.include_router(fraud_route, prefix='/api/v1/fraud')
