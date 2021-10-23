from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)


@app.route("/")
def main():
    # get connection
    conn_pg = psycopg2.connect(
        host=os.environ.get('MB_DB_HOST'),
        database=os.environ.get('MB_DB_DBNAME'),
        user=os.environ.get('MB_DB_USER'),
        password=os.environ.get('MB_DB_PASS'),
        port=int(os.environ.get('MB_DB_PORT'))
    )
    cur = conn_pg.cursor()

    return jsonify({"status": 200, "db":"connected"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
