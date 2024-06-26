from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# import uvicorn
import json
import lokasi
from lokasi import peta_kec

# Load the wilayah_sci.json data
with open('maps/wilayah_sci.json', 'r') as f:
    wilayah_sci = json.load(f)

wilayah_mapping = {data['LOKASI']: data['KODE_WILAYAH'] for data in wilayah_sci}

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


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: str = "OK"

@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    """
    ## Perform a Health Check
    Endpoint to perform a healthcheck on. This endpoint can primarily be used Docker
    to ensure a robust container orchestration and management is in place. Other
    services which rely on proper functioning of the API service will not deploy if this
    endpoint returns any other HTTP status code except 200 (OK).
    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck(status="OK")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/lov_prov")
async def lov_prov():
    # Get the unique list of province names and trimmed CC_3 codes from the peta_kec GeoDataFrame
    provinces = peta_kec[['NAME_1', 'CC_3']].drop_duplicates('NAME_1').values.tolist()
    provinces = [{'name': name, 'code': code[:2]} for name, code in provinces]
    return provinces


@app.get("/lov_kab_kota")
async def lov_kab_kota():
    # Get the unique list of kabupaten/kota names and trimmed CC_3 codes from the peta_kec GeoDataFrame
    kab_kota = peta_kec[['NAME_2', 'CC_3']].drop_duplicates('NAME_2').values.tolist()
    kab_kota = [{'name': name, 'code': code[:4]} for name, code in kab_kota]
    return kab_kota

@app.get("/lov_kec")
async def lov_kec():
    # Get the unique list of kecamatan names and trimmed CC_3 codes from the peta_kec GeoDataFrame
    kecamatan = peta_kec[['NAME_3', 'CC_3']].drop_duplicates('NAME_3').values.tolist()
    kecamatan = [{'name':name, 'code': code} for name, code in kecamatan]
    return kecamatan

@app.get("/lov_lokasi")
async def lov_lokasi():
    lokasi = peta_kec[['CC_3','NAME_1','NAME_2','NAME_3']]
    lokasi = lokasi.values.tolist()
    lokasi_with_keys = []
    for row in lokasi:
        kode_area, provinsi, kabupaten, kecamatan = row
        kode_wilayah = wilayah_mapping.get(provinsi, 'W3')  # Default to 'W3' if not found
        lokasi_with_keys.append({
            'kode_area': kode_area,
            'provinsi': provinsi,
            'kabupaten': kabupaten,
            'kecamatan': kecamatan,
            'kode_wilayah': kode_wilayah
        })
    return {"lokasi": lokasi_with_keys}

@app.post("/lokasi")
async def func_lokasi(lat_src, lon_src, lat_dst, lon_dst):
    info_lokasi = lokasi.geo_lokasi(lat_src, lon_src, lat_dst, lon_dst)
    return info_lokasi

@app.post("/get_adm")
async def func_getadm(lat, lon):
    info_lokasi = lokasi.get_adm(lat, lon)
    return info_lokasi

# def main() -> None:
#     """Entrypoint to invoke when this module is invoked on the remote server."""
#     # See the official documentations on how "0.0.0.0" makes the service available on
#     # the local network - https://www.uvicorn.org/settings/#socket-binding
#     uvicorn.run("main:app", host="0.0.0.0")


# if __name__ == "__main__":
    # main()
