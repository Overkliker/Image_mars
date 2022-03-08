from flask import Flask, render_template

app = Flask(__name__)


@app.route('/image_mars')
def nextlvl():
    return render_template('image_mars.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)