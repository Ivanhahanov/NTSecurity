import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import statsic_analysis, sandbox, files

logging.basicConfig(level=logging.DEBUG)
ip = '192.168.88.29'
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
mqtt_answer = ''

app.include_router(statsic_analysis.router, prefix="/static_analysis", tags=['Static Analysis'])
app.include_router(sandbox.router, prefix="/sandbox", tags=['Sandbox'])
app.include_router(files.router, prefix="/file", tags=['File'])

@app.get("/")
def index():
    return {"Hello": "World"}


