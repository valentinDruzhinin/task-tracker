init_migrations:
	flask db init

upgrade:
	flask db upgrade

downgrade:
	flask db upgrade

run: export DB_NAME=task_tracker
run: export DB_USER=admin
run: export DB_PASSWORD=mypassword
run:
	docker-compose up

stop: export DB_NAME=task_tracker
stop: export DB_USER=admin
stop: export DB_PASSWORD=mypassword
stop:
	docker-compose down
