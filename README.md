# solvestack_backend

## Docker
Make sure to run these commands from the root of the project.

### Initial setup
If you haven't created an .env file go ahead and make one from the example file:
`cp .envexample .env`

Make sure Docker is running, then do the following steps:
`docker-compose up --build`

After initial build and servers are running, in a separate terminal window run the following:

`docker-compose run web python manage.py migrate`
`docker-compose run web python manage.py createsuperuser`
`docker-compose run web python manage.py loaddata solvestack/fixtures/glossary.json`

All done!

### Running/Stopping
Start:
`docker-compose up`


End all processes:
`docker-compose down  --remove-orphans`

## Run it Locally (w/o Docker)

First time?

```bash
python3 -m venv env
```

On fresh updates, do the following:

```bash
source env/bin/activate
pip3 install -r requirements/requirements.txt
python3 manage.py migrate
python3 manage.py loaddata solvestack/fixtures/glossary.json
```

To start the backend:
```bash
source env/bin/activate
python3 manage.py runserver
```
