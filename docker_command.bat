@echo off

REM Pull Docker images
docker pull postgres:alpine
docker pull dbgate/dbgate:alpine

REM Create Docker volumes
docker volume create dbgate_data

REM Import Volumes of Postgresql
docker run --rm `
  -v ${PWD}/data_engineer_assignment_postgresql_data.tar.gz:/backup/data_engineer_assignment_postgresql_data.tar.gz `
  -v data_engineer_assignment_postgresql_data:/data `
  busybox `
  sh -c "tar xvf /backup/data_engineer_assignment_postgresql_data.tar.gz -C /data"

REM Run Docker containers
docker-compose up
