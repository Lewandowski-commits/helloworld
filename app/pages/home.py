import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from tools.reusable_elements import generate_timeline
from tools.db_connectivity import job_history_table

dash.register_page(__name__, path="/")

job_history_list = job_history_table.scan()['Items']
job_history_list.reverse()

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
                            className="lead text-success",
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
                        html.H1('About me', id='about-section', className='display-2'),
                        html.P('I\'m a former English-Russian-Polish Translator & Interpreter turned into experienced Data Analyst with a demonstrated history of working in the pharmaceuticals industry. Skilled in PowerBI, Python, Business Analytics, Customer Service, Performance Dashboards, and Emotional Intelligence. Strong information technology enthusiast with a Postgraduate Degree focused in Big Data - Analytics & Society from Collegium Da Vinci.'),
                        generate_timeline(
                            job_history_list,
                            date = 'start_date'
                        )
                    ],
                className='col-10'),
            ],
            className='vh-100 justify-content-center'
        )
    ],
)
