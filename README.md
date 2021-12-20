
# TO USE ENDPOINTS REMOVE SWAGGER SCHEMA AND USE POSTMAN AGENT

#  WMA-coding challenge
The project folder contains a Django project of a WMA-coding challenge for user subscription and renewal to access premium content


## Getting Started

To get a copy of the project up and running on your local machine for development and testing purposes.
-clone the project from Github on terminal
-Create a virtual environment using pipenv and use pipenv shell to activate for your folder
-See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Use the requirements.txt files to download pre-requisite packages needed to run the project

(WMA-coding challenge) $ pipenv lock -r > requirements.txt

### Setup
Rename the .env.sample file to .env and add all listed entries

Spawn a shell in a virtual environment
pipenv shell


Turn off a virtual environment
exit

### Installing
Install pipenv:
pip install pipenv

Check if pipenv is installed:
pipenv --version
>> pipenv, version 2018.11.26

Rename the .env.sample file to .env and add all listed entries

Install dependencies in piplock file
pipenv sync

Install new dependency
pipenv install <dependency name here>

Regenerate lock file after new dependency installations
pipenv lock

List all dependencies currently installed
pipenv lock -r

Uninstall dependency
pipenv uninstall <dependency name here>


## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Use (virtual) $ python3 manage.py test command to run tests

### And coding style tests

The tests will test the Profile,Follow,Comment,Image classes for errors

## Deployment

Deployment has been done on Heroku using the requirements.txt packages

## Built With

* Django 3.2.8
* Python 3.8
* Postgresql
* See requirements.txt for all packages.

## Authors

* **Andrew Indeche** - *Final work*
## ERRORS
None
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
