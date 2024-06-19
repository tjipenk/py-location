from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# import uvicorn

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
    query = "SELECT DISTINCT NAME_1 FROM prov_table"
    result = await execute_query(query)
    return [row["NAME_1"] for row in result]

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

# def main() -> None:
#     """Entrypoint to invoke when this module is invoked on the remote server."""
#     # See the official documentations on how "0.0.0.0" makes the service available on
#     # the local network - https://www.uvicorn.org/settings/#socket-binding
#     uvicorn.run("main:app", host="0.0.0.0")


# if __name__ == "__main__":
    # main()
