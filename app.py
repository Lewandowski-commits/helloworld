from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash
from os import getenv

BOOTSTRAP_THEME = 'https://hackerthemes.com/bootstrap-themes/demo/theme-machine/neon-glow/css/bootstrap4-neon-glow.min.css'

app = Dash(__name__, use_pages=True, external_stylesheets=[BOOTSTRAP_THEME])

app.layout = html.Div([
	html.H1('Multi-page app with Dash Pages'),
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