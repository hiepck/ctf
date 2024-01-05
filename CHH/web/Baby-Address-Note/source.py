from flask import Flask, session, render_template, request, Response, render_template_string, g
import functools
import sqlite3
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(120)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('/tmp/address.db')
        db.isolation_level = None
        db.row_factory = sqlite3.Row
    return db


def query_db(query, args=(), one=False):
    with app.app_context():
        cur = get_db().execute(query, args)
        rv = [dict((cur.description[idx][0], str(value))
                   for idx, value in enumerate(row)) for row in cur.fetchall()]
        return (rv[0] if rv else None) if one else rv


@app.before_first_request
def init_db():
    with app.open_resource('schema.sql', mode='r') as f:
        sql = f.read()
        get_db().cursor().executescript(sql)


@ app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@ app.route('/')
def index():
    uid = request.args.get('uid')
    if uid:
        try:
            sql = f"SELECT * FROM users WHERE uid='{uid}';"
            result = query_db(sql, one=True)
            if result:
                return render_template("welcome.jinja2", uid=uid, result=result)
            else:
                return render_template("welcome.jinja2", uid=uid, result='')
        except Exception as e:
            return render_template("welcome.jinja2", uid=uid, result=e)
    else:
        return render_template("welcome.jinja2", uid=uid, result='')


@ app.route('/heath')
def heath():
    return "OK"


@ app.route('/debug')
def debug():
    return Response(open(__file__).read(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=False)
