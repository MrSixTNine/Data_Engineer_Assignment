@echo off

REM Pull Docker images
docker pull postgres:alpine
docker pull dbgate/dbgate:alpine

REM Create Docker volumes
docker volume create dbgate_data

REM Build the Docker image
docker build -t my-python-app .

REM Run Docker containers
docker-compose up --build


