import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")

layout = html.Div(
    children=[
        dbc.Row(
            className="vh-100 d-flex justify-content-center align-items-center",
            children=[
                dbc.Col(
                    children=[
                        html.H1(
                            className="display-1",
                            children=[
                                "Michał Lewandowsk",
                                html.Span("i", className="vim-caret"),
                            ],
                        ),
                        html.H2(
                            "📈 BI Developer. 🐍 Python enthusiast.",
                            className="text-success",
                        ),
                        html.A('About', href='#about-section', className='ht-tm-element btn btn-shadow btn-primary')
                    ],
                    className="col-8",
                )
            ],
        ),
        dbc.Row(
            children=[
                dbc.Col(
                    [
                        html.H1('About me', id='about-section', className='display-2')
                    ],
                className='col-10'),
            ],
            className='vh-100 justify-content-center'
        )
    ],
)
