rebuild:
	docker-compose up --no-deps --build --force-recreate --no-start

start:
	docker-compose up

start-detached:
	docker-compose up -d

stop:
	docker-compose stop

enter:
	docker-compose exec app bash

test:
	docker-compose exec app python -m unittest

coverage:
	docker-compose exec app coverage run --source=src -m unittest discover tests

coverage-report:
	docker-compose exec app coverage report

coverage-html-report:
	docker-compose exec app coverage html
