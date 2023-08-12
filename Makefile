APP = restapi

test: 
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings

compose:
	@docker-compose build
	@docker-compose up

heroku:
	@heroku container:login
	@heroku container:push -a flask-restapi web
	@heroku container:release -a flask-restapi web