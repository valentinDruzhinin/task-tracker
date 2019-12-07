![Heroku](https://heroku-badge.herokuapp.com/?app=task-tracker-manager)
# Demo
```http request
http://task-tracker-manager.herokuapp.com
```

# task-tracker
Task tracker system

## Local development
### Prerequisites
1. Install virtualenv `python3 -m venv env`
2. Enter into virtualenv `source env/bin/activate`
3. Install dependencies `pip install -r requirements.txt`
### Local run
Docker-compose is used for development.
- Run - `make run`
- Free resources - `make stop`
### Run Tests:
Run `export DB_NAME=test && export DB_USER=admin && export DB_PASSWORD=mypassword && docker-compose up && pytest && docker-compose down`
