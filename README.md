# cookie_cutter
default project repository template for future CF DS team

## How to use a template

Copy this template using the green button at the top of this github repo


## Intro to a Makefile

This repo contains a Makefile which you can use to simplify setting up the environment,
running the unit tests and running the linting.


## Adding tests

tests can be added to the `tests/` directory. An example exists as a template to use. For more details 
read [this](https://docs.pytest.org/en/stable/)


## Set up environments

This repo contains both a requirements.txt and a Pipfile. We recommend using pipenv still (only just)
if this is slow we would recommend using `pipenv install [package] --skip-lock`

The requirements.txt can be updated using `make sync_requirements` . This is recommended before pushing 
or creating a pull request

## Run style checks

We have an style guide that ensure that our code is written in a consistent way across projects.
To check that the code written with the src directory please run ` make style-check`.

## Run tests

Run tests using `pytest` or `make test`


## Set up docs

Initially run `sphinx-quickstart` from the docs directory.

Further detail can be found [here](https://www.sphinx-doc.org/en/master/index.html)

## Pushing to Github

This repo template uses Github actions to automate running the linting and tests.
If the push or pull request fails you will get an email and your pull request will not be accepted.
Do not just remove tests to make your tests work. That is a terrible way of working

