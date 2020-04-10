from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/img/<path:img>')
def img(img):
    return send_from_directory('img/', img)

@app.route('/static/css/<string:css>')
def css(css):
    return send_from_directory('static/css/', css)

if __name__ == "__main__":
    app.run(threaded=True, port='5000')
