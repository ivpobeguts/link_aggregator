# Link aggregator API
This is Link aggregator API, a social link aggregator. At its core, it will be a place where users can submit internet links (URLs), and upvote/downvote ("Thumb up"/"Thumb down") each other's Links. The difference between Upvotes and Downvotes, for each Link, is their Score.
This is not a real API and is used for the sake of exercise.

## Prepare runtime
1. Install python 3.11.
2. [Install](https://python-poetry.org/docs/#installing-with-the-official-installer) poetry for python 3.11
3. Allow poetry to use its own virtual environment:
```shell script
poetry config virtualenvs.in-project true
```
4. Install the dependencies:
```shell script
poetry install
```
5. CD to the django_app folder where manage.py file is located.
6. Apply migrations:
```shell script
make migrate
```
7. Run the server:
```shell script
make run
```

## Tests
The tests could be run with the following command:
```shell script
make test
```

## Documentation
To be able to see documentation the server needs to be running.
API documentation can be found here: http://127.0.0.1:8000/docs