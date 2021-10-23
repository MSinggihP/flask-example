# Flask Example

Flask example project

# Run
first you must create file with name `.env`, copy and paste code:
```
MB_DB_HOST='your_localhost'
MB_DB_DBNAME='your_dbname'
MB_DB_USER='your_user'
MB_DB_PASS='your_password'
MB_DB_PORT='your_port'
```

## Run Ubuntu or Mac
```
pip install -r requirements.txt
export FLASK_APP=app/main.py
export FLASK_ENV=development
flask run
```
or
```
bash run.sh
```

## Run Windows
```
pip install -r requirements.txt
set FLASK_APP=app/main.py
set FLASK_ENV=development
flask run
```