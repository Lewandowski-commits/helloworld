import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.H1(children='This is home page'),

    html.Div(children='''
        This is our Home page content.
    '''),
    dbc.Tabs(
        [
            dbc.Tab(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                ),
                label = page['name']
            )
            for page in dash.page_registry.values() if 'portfolio' in page['path']
        ]
    )
])