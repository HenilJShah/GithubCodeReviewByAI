import uvicorn
from fastapi import FastAPI

from routes.routes import router

app = FastAPI()

app.include_router(router=router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
