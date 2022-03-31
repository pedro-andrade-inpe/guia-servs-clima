[![pipeline status](https://git21.znc.com.br/necto/guia-servs-clima/badges/main/pipeline.svg)](https://git21.znc.com.br/necto/guia-servs-clima/-/commits/main)
[![coverage report](https://git21.znc.com.br/necto/guia-servs-clima/badges/main/coverage.svg)](https://git21.znc.com.br/necto/guia-servs-clima/-/commits/main)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-397/)
[![docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://docs.docker.com/)
[![postgres](https://badgen.net/badge/icon/postgresql?icon=postgresql&label)](https://www.postgresql.org//)

# INPE Guia de Serviços Climáticos

Sistema baseado na web para acessar as instituições provedoras de informações climáticas no Brasil.

## Objetivo Geral

Desenvolver e implementar um sistema baseado na web para promover o contato entre
provedores de informações climáticas e usuários dessas informações. O sistema permitirá aos usuários
encontrarem instituições que forneçam os dados e informações de acordo com suas necessidades
específicas. O sistema, sem operação transacional, será aberto para todos os usuários, os quais poderão
contar com um mecanismo de filtragem na busca por instituições, serviços e dados climáticos.

Uma vez que o usuário identifique a(s) instituição(ões) que oferece(m) aquilo que ele(a) procura, serão
disponibilizadas informações de contato e serviços da instituição para que o usuário faça o contato. É um
processo de “Match-Making” que busca integrar a demanda e o fornecimento entre usuários e
instituições provedoras. Além disso, com o intuito de fomentar uma comunidade, será implementado um
fórum virtual para que qualquer ator do ecossistema ou pessoa interessada possa participar de
discussões, fazer anúncios, divulgar eventos, pedir referências, enviar solicitações e tirar dúvidas.

# Instalação do Ambiente de Desenvolvimento

## Pré-requisitos

- [Docker](https://docs.docker.com/install/)
- [Docker-compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com)
- [PostgresSQL](https://www.postgresql.org/)

## Como executar

```bash
# Criar a pasta do projeto:
$ mkdir guia_servs_clima
```

```bash
# Acessar a pasta do projeto:
$ cd guia_servs_clima
```

```bash
# Clonar repositório:
$ git clone ssh://git@git21.znc.com.br:2224/necto/guia-servs-clima.git
```

```bash
# Acessar repositório:
$ cd guia-servs-clima
```

```bash
# Criar arquivo *.env* baseado no *.env-sample*:
$ cp .env-sample .env
```

**_IMPORTANTE: Lembre de adicionar/alterar os valores nas variáveis no novo arquivo .env
com os valores pertinentes._**

```bash
# Executar o build da imagem docker:
$ docker-compose build
```

```bash
# Gerar uma chave secreta:
docker-compose run --rm web python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

Obs.: Substitua o valor da variável *SECRET_KEY* que está dentro do arquivo *.env*, pelo valor gerado através do comando acima.
Não é necessário por entre aspas o valor gerado.
```

```bash
# Subir banco de dados:
$ docker-compose up -d db
```

```bash
# Criar migrações iniciais:
$ docker-compose run --rm web python manage.py makemigrations
```

```bash
# Aplicar migrações:
$ docker-compose run --rm web python manage.py migrate
```

```bash
# Carregar dados no banco de dados:
$ docker-compose run --rm web python manage.py loaddata guia_servicos_initial_fixtures.json

Obs: As fixtures do projeto se encontram na pasta guia_servs_clima/guia_servs_clima/core/fixtures/
```

```bash
# Executar o servidor web:
$ docker-compose run --rm --service-ports web

Obs.: O servidor será executado na porta indicada no arquivo .env
```

```bash
# Executar os testes:
$ docker-compose run --rm web pytest
```

```bash
# Verificar se não há inconsistências com a PEP8:
$ docker-compose run --rm web flake8 .
```

```bash
# Verificar os imports estão ordenados:
$ docker-compose run --rm -u $(id -u ${USER}):$(id -g ${USER}) web isort
```

## Links do Projeto

- [Deploy](http://guiaservsclima.testes.necto.com.br/)
- [Documentos](https://drive.google.com/drive/folders/1kRtxAs1qTaCePnsyfcglWDn7suZNysiL)
