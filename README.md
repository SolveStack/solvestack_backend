# solvestack_backend

First time?

```bash
python3 -m venv env
```

On fresh updates, do the following:

```bash
source env/bin/activate
pip3 install -r dev-requirements.txt
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py loaddata solvestack/fixtures/glossary.json
```
