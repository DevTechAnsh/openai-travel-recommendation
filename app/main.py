from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.activity import router as recommendations_router

app = FastAPI()
app.include_router(recommendations_router)

#used middleware to handle cors-origin error 
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
