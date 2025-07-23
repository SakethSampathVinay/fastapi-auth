from fastapi import FastAPI
from routes.routes import router as auth_router
from routes.dashboad import router as dashboard_router

app = FastAPI()

app.include_router(auth_router, prefix = '/auth', tags = ['auth'])
app.include_router(dashboard_router, prefix = '/dashboard', tags = ['dashboard'])

@app.get('/')
def read_root():
    return {'message': "Welcome to the FastAPI Auth application!"}