# Brightwheel Technical Test
> Backend For Brightwheel.

## Contents
- [Tech-stack used](#tech-stack-used)
- [Getting Started](#getting-started)
- [Development Tools](#development-tools)
- [Request and Response](#request-and-response)


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

# run pytest inside of the Docker environment
./docker/local/cli/pytest <command arguments>
```

## Request and Response

#### Request

The URL of API is : ```/email/send_email/```

Method Type: ``` POST ```

Body: Request Should be json object like below
****All the fields are required****
<pre>
   {
          "to_email": "email of the to user",
          "from_email": "email of the from user",
          "to_name": "name",
          "from_name": "from name",
          "subject": "subject of the email",
          "body": "body of the email"
   }
</pre>

