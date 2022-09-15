from dash import Dash, html


def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=[
            '/static/dist/css/styles.css',
        ]
    )

    # Create Dash Layout
    dash_app.layout = html.Div(id='dash-container', children='test')

    return dash_app.server