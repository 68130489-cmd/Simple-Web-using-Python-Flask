from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
  

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/tee')
def tee():
    return render_template('tee.html')


if __name__ == '__main__':
    app.run(port=80,debug=True)