@echo off

REM Pull Docker images
docker pull postgres:alpine
docker pull dbgate/dbgate:alpine

REM Create Docker volumes
docker volume create dbgate_data

REM Import Volumes of PostgreSQL
docker run --rm ^
  -v %cd%/data_engineer_assignment_postgresql_data_empty.tar.gz:/backup/data_engineer_assignment_postgresql_data_empty.tar.gz ^
  -v data_engineer_assignment_postgresql_data:/data ^
  busybox ^
  sh -c "tar xvf /backup/data_engineer_assignment_postgresql_data_empty.tar.gz -C /data"

REM Build the Docker image
docker build -t my-python-app .

REM Run the Docker container
docker run my-python-app

REM Run Docker containers
docker-compose up --build
