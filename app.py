import json
import os


from dotenv import load_dotenv
from flask import Flask, render_template, request, flash, g

from init_db import get_db_connection

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = get_db_connection()
    return g.link_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

@app.route("/", methods=["POST", "GET"])
def index():
    db = get_db()
    if request.method == "POST":
        sumlen = 0
        for i in request.form:
            sumlen += len(request.form[i])
        if sumlen:
            cur = db.cursor()
            cur.execute(f"INSERT INTO note (inputs) VALUES('{json.dumps(request.form)}')")
            db.commit()
            cur.close()
            flash('данные отправлены', category="success")
        else:
            flash('форма пустая, ошибка отправки', category="error")
    return render_template("index.html")

@app.route("/show/<int:id_note>")
def show_note(id_note):
    db = get_db()
    cur = db.cursor()
    cur.execute(f"SELECT * FROM note WHERE id = {id_note};")
    note = cur.fetchone()
    if note:
        return render_template("show_note.html", note=note[1], pk=id_note)
    else:
        return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=False)