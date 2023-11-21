# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})


def create_dash_application(flask_app):
    dash_app = dash.Dash(server=flask_app,name = "Dashboard", url_base_pathname="/dash/")
    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    dash_app.layout = html.Div(children=[
        html.H1(children='BMT Analytics'),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])
    return dash_app
