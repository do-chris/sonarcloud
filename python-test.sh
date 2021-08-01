#!bin/bash

pip install -r requirements.txt

pylint -ry *.py > pylint-report.txt

coverage run -m pytest *.py
coverage xml *.py

chown -R ${host_uid} ./*
