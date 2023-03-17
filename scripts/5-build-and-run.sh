cd guia-servs-clima
cp .env-prod .env


docker-compose -f docker-compose-prod.yml build

docker-compose -f docker-compose-prod.yml up -d

docker exec guia_servs_clima_prod_web python manage.py migrate
docker exec guia_servs_clima_prod_web python manage.py collectstatic --noinput

docker exec guia_servs_clima_prod_web python manage.py loaddata guia_servicos_initial_fixtures.json
cd

