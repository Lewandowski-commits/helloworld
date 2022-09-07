from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash
from os import getenv

BOOTSTRAP_THEME = '/static/style/bootstrap4-neon-glow.css'

app = Dash(__name__, use_pages=True, external_stylesheets=[BOOTSTRAP_THEME])

server = app.server

app.layout = html.Div([
    dbc.ListGroup(
        [
            dbc.ListGroupItem(
                dcc.Link(
                    page['name'], href=page['relative_path']
                )
            )
            for page in dash.page_registry.values()
        ]
    ),
    dash.page_container
],
)

if __name__ == '__main__':
	app.run_server(debug=getenv('DASH_DEBUG_MODE', True), host='0.0.0.0', port='8050')