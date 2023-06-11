from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

import lokasi 

app = FastAPI()

origins = [
    # To restrict access use below examples instead of "*"
    # "http://localhost",
    # "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/lokasi")
async def func_lokasi(lat_src, lon_src, lat_dst, lon_dst):
    info_lokasi = lokasi.geo_lokasi(lat_src, lon_src, lat_dst, lon_dst)
    return info_lokasi
