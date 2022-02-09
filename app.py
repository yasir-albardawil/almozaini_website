from flask import Flask, render_template, request, redirect, \
    jsonify, flash

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template(
        'index.html',
        title='Almozaini &#8211; The Real, Real Estate Developer'
    )


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000, threaded=False)
