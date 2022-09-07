import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    dbc.Row(
        className='vh-100 d-flex justify-content-center align-items-center',
        children=[
	        html.H1('Michał Lewandowski'),
            ]
        )
])