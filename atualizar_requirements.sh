#!/bin/bash

#Atualiza todos os arquivos de requirements
docker-compose run --rm web bash -c "pip-compile --generate-hashes /usr/src/requirements/base.in && pip-compile --generate-hashes /usr/src/requirements/dev.in && pip-compile --generate-hashes /usr/src/requirements/prod.in && pip-compile --generate-hashes /usr/src/requirements/homologacao.in"

docker-compose build
