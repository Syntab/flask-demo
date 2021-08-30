from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/somepage')
def somepage():
    return render_template('somepage.html')

@app.route('/')
def homepage():
    return render_template('index.html')
    # these templates should be in the "templates" directory

if __name__ == '__main__':
    app.run()
