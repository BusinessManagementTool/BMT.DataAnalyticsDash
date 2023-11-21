import flask
from flask import Flask

from SaleAnalysisEngine import SaleAnalysisEngine
from DashAnalytics import create_dash_application
app = Flask(__name__)
create_dash_application(app)


@app.route("/GetPerDaySaleChart")
def getPerDaySaleChart():
    SaleAnalysisEngine().perMonthSaleData()


@app.route("/")
def hello():
    return "hello world!"


if __name__ == '__main__':
    app.run()
