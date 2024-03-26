#!/bin/sh
docker build -t tjipenk/pylocation:latest .

docker stop pylocation && docker rm pylocation

docker run -d --name pylocation -p 8080:80 tjipenk/pylocation:latest


