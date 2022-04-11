import sqlite3
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template

app = Flask(__name__)
bootstrap = Bootstrap5(app)


def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


@app.route('/')
def index():  # put application's code here
    conn = get_db_connection()
    breweries = conn.execute('SELECT * FROM breweries').fetchall()
    conn.close()
    return render_template('index.html', breweries=breweries)


if __name__ == '__main__':
    app.run()
