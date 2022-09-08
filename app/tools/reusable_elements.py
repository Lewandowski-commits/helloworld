from dash import html, dcc
import dash_bootstrap_components as dbc

def generate_timeline(events: list[dict]):
    children = []
    for event in events:
        children.append(
            html.Div(children=[
                dbc.Card([
                    dbc.CardBody(children=[
                        dbc.CardHeader(
                            event['name']
                        ),
                        html.Span(children=[
                            html.I(className='fas fa-clock me-1'),
                            event['date']
                        ],
                        className='small text-muted'
                        ),
                        html.P(children=[
                            event['body']
                        ],
                        className='mt-2 mb-0')
                    ],
                    className='p-4')
                ])
            ],
            className='timeline-5 right-5')
        )
        pass

    layout = html.Section(
        children=[
            html.Div(children=[
                html.Div(children=children,
                className='main-timeline-5')
            ],
            className='container py-5')
        ],
        className='gradient-custom-5'
        )

    return layout

if __name__ == '__main__':
    pass