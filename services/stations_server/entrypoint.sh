#!/bin/sh

mkdir ./certificates

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./certificates/stations_server.key -out ./certificates/stations_server.crt -subj '/'

python3 run.py