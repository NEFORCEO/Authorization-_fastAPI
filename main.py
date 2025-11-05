from fastapi import FastAPI
import uvicorn

from client.run import start_app
from routers.router import router

app = FastAPI(lifespan=start_app)
app.include_router(router=router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)