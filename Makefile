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
