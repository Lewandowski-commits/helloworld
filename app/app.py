from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash
from os import getenv

BOOTSTRAP_THEME = "/static/style/bootstrap4-neon-glow.css"

app = Dash(__name__, use_pages=True, external_stylesheets=[BOOTSTRAP_THEME])

server = app.server

navbar = dbc.NavbarSimple(
            children=[
                dbc.DropdownMenu(
                    children=[
                        dbc.NavItem(dcc.Link(page["name"], href=page["relative_path"]))
                        for page in dash.page_registry.values() if 'portfolio' in page["relative_path"]
                    ],
                    nav=True,
                    in_navbar=True,
                    label='Portfolio'
                )
            ],
            color='primary',
            brand='Michał Lewandowski',
            brand_href='/',
            dark=False,
            sticky='top'
            )

app.layout = html.Div(
    [
        dash.page_container,
        navbar,
    ],
)

if __name__ == "__main__":
    app.run_server(debug=getenv("DASH_DEBUG_MODE", True), host="0.0.0.0", port="8050")
