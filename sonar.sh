#!/bin/bash

pylint -ry *.py > pylint-report.txt
coverage run -m pytest *.py
coverage xml *.py
cat coverage.xml

sonar-scanner \
  -Dsonar.projectKey=localtest \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.python.coverage.reportPaths=coverage.xml \
  -Dsonar.python.pylint.reportPaths=pylint-report.txt \
  -Dsonar.login=5f3deea7af9e3fa788d8f423129aa60e433b81cf

rm -rf pylint-report.txt
rm -rf .coverage coverage.xml
rm -rf __py*
