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

@app.get("/lov_prov")
async def lov_prov():
    return {"message": "Hello World"}

@app.get("/lov_kab_kota")
async def lov_kab_kota():
    return {"message": "Hello World"}

@app.get("/lov_kec")
async def lov_kec():
    return {"message": "Hello World"}

@app.get("/lov_lokasi")
async def lov_lokasi():
    return lokasi.list_lokasi()


@app.post("/lokasi")
async def func_lokasi(lat_src, lon_src, lat_dst, lon_dst):
    info_lokasi = lokasi.geo_lokasi(lat_src, lon_src, lat_dst, lon_dst)
    return info_lokasi

@app.post("/get_adm")
async def func_getadm(lat, lon):
    info_lokasi = lokasi.get_adm(lat, lon)
    return info_lokasi