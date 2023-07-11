from flask import Flask, render_template, session, request, jsonify
app = Flask(__name__)
app.config['SECRET_KEY'] = b'|?`\x9d\xf4\x9dTf\x10\xeak\xbctG\x87\xba'


@app.route("/")
def index():
    count = 0
    if "count" in session:
        count = session["count"]
    return render_template("index.html", count=count)


@app.route("/update", methods=['POST'])
def update():
    session["count"] = request.form['count']
    return jsonify(result='OK')


app.run()
