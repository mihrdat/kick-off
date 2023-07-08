# Django Cookiecutter Template

This is a Django project template created using Cookiecutter. It provides a solid foundation for building scalable and maintainable Django applications.

## Features

- Django 3.x
- PostgreSQL as the default database
- Django REST Framework for building APIs
- Docker and Docker Compose for development and production environments
- Celery for background tasks
- Redis for caching and Celery message broker
- Django Debug Toolbar for development
- and more

## Requirements

- Python 3.x
- Docker and Docker Compose

## Usage

To use this template, you'll need `cookiecutter` installed. Install cookiecutter using pip:
```
pip install cookiecutter
```

Then run the following command:
```
cookiecutter https://github.com/Mihrdat/kick-off.git
```

This will prompt you for some information about your project. Once you've provided all the necessary information, Cookiecutter will generate a new Django project for you based on this template.

Next, navigate to the project directory and start the Docker containers:
```
cd project_name
```
```
docker-compose -f docker-compose.dev.yml up
```

This will start the Django server, PostgreSQL, Redis, and Celery worker and beat processes in the background.

## Contributing

If you find any issues with this template or have suggestions for improvement, feel free to open an issue or pull request on GitHub.
