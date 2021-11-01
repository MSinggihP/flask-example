# Flask Example

Flask example projects

# Run without docker
Untuk menjalankan service ini kita harus mempunya service database postgres, Jika belum ada database postgres silakan run docker-compose dibawah ini:
```
version: '2'
services:
  postgres-db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: admin
      POSTGRES_USER: postgres
      PGDATA: /var/lib/postgresql/data
      POSTGRES_DB: metabase
    volumes:
    - postgres_data:/var/lib/postgresql/data  # docker volume create postgres_data
    ports:
    - 5433:5432/tcp
volumes:
    postgres_data:
        external: true
```
jangan lupa create volume postgres_data:
```docker volume create postgres_data```

and next step, you must create file with name `.env` (file sejajar dengan folder app, lihat gambar dibawah), copy and paste code:
```
MB_DB_HOST='your_localhost'
MB_DB_DBNAME='your_dbname'
MB_DB_USER='your_user'
MB_DB_PASS='your_password'
MB_DB_PORT='your_port'
```
[![Screenshot-from-2021-11-01-15-57-04.png](https://i.postimg.cc/BvFhfW1s/Screenshot-from-2021-11-01-15-57-04.png)](https://postimg.cc/SXyLcvrt)

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
