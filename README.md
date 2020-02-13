# Brightwheel Technical Test
> Backend For Brightwheel.

## Contents
- [Tech-stack used](#tech-stack-used)
- [Getting Started](#getting-started)


## Tech-stack used

- Python 3.7
- Django 3.0


## Getting Started

Before cloning the repository ensure you have Docker, Python 3, Pipenv installed locally.

Install **Docker** using the download from https://docs.docker.com/docker-for-mac/install/

Install **Python 3** using homebrew as described https://docs.python-guide.org/starting/install3/osx/

Install **Pipenv** using homebrew as described https://pipenv.readthedocs.io/en/latest/

Clone the repository
```sh
git clone https://github.com/aabhas12/brightwheel.git

```

## Development Tools

#### Docker

Docker is used for local development of this project.

Managing the Docker containers for the project ...

```
# build the docker containers for the project
docker-compose build

# start docker containers in the background
docker-compose up -d

# follow the logs from a running docker container
docker-compose logs -f <optional specific service>

# stop docker when it's running in the background
docker-compose stop <optional specific service>

# start a stopped container
docker-compose start <optional specific service>

# destroy docker containers
docker-compose down

# available services for this project
brightwheel-django-local : django application container for development
```

With the Docker containers running ...

```
# run manage.py inside of the Docker environment
./docker/local/cli/manage <command arguments>

# run pipenv inside of the Docker environment
./docker/local/cli/pipenv <command arguments>

# run pytest inside of the Docker environment
./docker/local/cli/pytest <command arguments>
```
