from flask import Flask, render_template, url_for
from funPars import get_data_xls, data_create
from datetime import datetime

app = Flask(__name__)
data = get_data_xls()


@app.route('/')
def index():

    return render_template('index.html', data=data, create=data_create, year=str(datetime.today()).split('-')[0])


if __name__ == '__main__':
    app.run(debug=True)
