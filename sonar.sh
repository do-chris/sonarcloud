#!/bin/bash

# Generate pylint and coverage xml
docker run -it --rm \
  -v ${PWD}:/src \
  -w /src \
  -e host_uid=${UID} \
  python bash python-test.sh

# Create sonar scanner settings
echo "
# Local sonar-scanner settings
sonar.projectKey=local
sonar.sources=.
sonar.python.coverage.reportPaths=coverage.xml
sonar.python.pylint.reportPaths=pylint-report.txt
sonar.host.url=http://10.1.1.201:9000
" > sonar-project.properties

# Run solar-scanner cli via docker
docker run --rm \
  -e SONAR_HOST_URL="http://10.1.1.201:9000" \
  -e SONAR_LOGIN="ae4c07529b09c567ac92e74bd504f1799d82939a" \
  -v "${PWD}:/usr/src" \
  sonarsource/sonar-scanner-cli

# Cleanup
rm -rf \
  pylint-report.txt \
  .coverage coverage.xml \
  sonar-project.properties \
  __py*
