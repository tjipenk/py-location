curl -X 'POST' \
  'http://localhost:8000/get_adm?lat=-6.247006&lon=106.8532497' \
  -H 'accept: application/json' \
  -d ''


curl -X 'POST' \
  'http://localhost:8000/lokasi?lat_src=6.247006&lon_src=106.8532497&lat_dst=-6.247006&lon_dst=106.8532497' \
  -H 'accept: application/json' \
  -d ''

-6.247006,106.8532497