init_migrations:
	flask db init

upgrade:
	flask db upgrade

downgrade:
	flask db upgrade
