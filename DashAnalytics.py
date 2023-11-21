# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from SQLDataLoader import SalesSQLRepository


# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

class SaleAnalytics:
    def __init__(self):
        # Create an instance of ClassA within ClassB
        self.SalesSQLRepositoryInstance = SalesSQLRepository()

    # This is to create dash application inside flask
    def create_dash_application(self, flask_app):
        dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash/")
        sales = self.SalesSQLRepositoryInstance.fetchSales()
        # Sample data (replace this with your actual data)
        orderIds = [item[0] for item in sales]
        orderdates = [item[1] for item in sales]
        data = {
            'OrderID': orderIds,
            'OrderDate': orderdates
        }
        # Convert 'OrderDate' to datetime
        df = pd.DataFrame(data)
        df['OrderDate'] = pd.to_datetime(df['OrderDate'])

        # Calculate per-day sales
        daily_sales = df.groupby('OrderDate')['OrderID'].count()
        fig = px.line(x=daily_sales.index, y=daily_sales.values, markers=True, title='Per-Day Sales')

        dash_app.layout = html.Div(children=[
            html.H1(children='BMT Analytics'),

            dcc.Graph(
                id='line-plot',
                figure=fig
            )
        ])
        return dash_app
