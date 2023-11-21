from flask import Flask
from DashAnalytics import SaleAnalytics

app = Flask(__name__)
SaleAnalytics().create_dash_application(app)


@app.route("/")
def hello():
    return "hello world!"


if __name__ == '__main__':
    app.run()
