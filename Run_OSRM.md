# OSRM docker
## download maps
```sh
wget http://download.geofabrik.de/europe/germany/berlin-latest.osm.pbf

wget http://download.geofabrik.de/asia/indonesia-latest.osm.pbf
```

## extract maps
```sh
# 1
docker run -t -v "${PWD}:/data" ghcr.io/project-osrm/osrm-backend osrm-extract -p /opt/car.lua /data/berlin-latest.osm.pbf || echo "osrm-extract failed"
## IND
docker run -t -v "${PWD}:/data" ghcr.io/project-osrm/osrm-backend osrm-extract -p /opt/car.lua /data/indonesia-latest.osm.pbf || echo "osrm-extract failed"

# 2
docker run -t -v "${PWD}:/data" ghcr.io/project-osrm/osrm-backend osrm-partition /data/indonesia-latest.osrm || echo "osrm-partition failed"
docker run -t -v "${PWD}:/data" ghcr.io/project-osrm/osrm-backend osrm-customize /data/indonesia-latest.osrm || echo "osrm-customize failed"


# run service
docker run -t -i -p 5000:5000 -v "${PWD}:/data" ghcr.io/project-osrm/osrm-backend osrm-routed --algorithm mld /data/indonesia-latest
```

## Make requests against the HTTP server
```sh
curl "http://127.0.0.1:5000/route/v1/driving/13.388860,52.517037;13.385983,52.496891?steps=true"
```

## Optionally start a user-friendly frontend on port 9966, and open it up in your browser
```sh
docker run -p 9966:9966 osrm/osrm-frontend
xdg-open 'http://127.0.0.1:9966'
```