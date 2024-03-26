# Py location
Api info lokasi berdasarkan koordinat GIS dan peta dasar andministrasi (Source : GADM.ORG)

## build
```bash
docker build -t tjipenk/pylocation:latest .
```

## Run
``` bash
docker run -d --name pylocation -p 8080:80 tjipenk/pylocation:latest
```

## Stop
``` bash
docker stop pylocation && docker rm pylocation
```
