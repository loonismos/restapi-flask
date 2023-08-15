# Rest API Flask

The main idea of this project is to be a pratical combination of many technologies, something usual in Devops' daily life.

Simply run make compose, to build and run the docker container.
```make
  make compose
```
For this project the following is proposed:
- Build an API consists in three endpoints:
    /users to return all users (GET)
    /user/<cpf> to return a specific user (GET)
    /user to register a new user (POST)
- Persist data in a database.
- Config an app to run inside a docker container (Dockerfile).
- Create a docker-compose to 'compose' the API with the database (dev environment)
- Write Unit Test to the endpoints.
- Use a Makefile to automate the most common steps.
- Deploy of the app in any Paas plataform (in this case Heroku).
- Create a CI/CD pipeline using some "as a service" tool (GitHub Actions, Azure Devops, etc...).
