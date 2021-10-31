#!/bin/bash
docker network create --driver bridge  etworkame
docker-compose up --build
$SHELL