import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_pivottable

from data import data

app = dash.Dash(__name__)
app.title = 'My Dash example'

app.layout = html.Div([
    dash_pivottable.PivotTable(
        id='table',
        data=data,
        cols=['Day of Week'],
        colOrder="key_a_to_z",
        rows=['Party Size'],
        rowOrder="key_a_to_z",
        rendererName="Grouped Column Chart",
        aggregatorName="Average",
        vals=["Total Bill"],
        valueFilter={'Day of Week': {'Thursday': False}}
    ),
    html.Button('Toggle data', id='toggle-data-button', n_clicks=0),
    html.Div(
        id='output'
    )
])


@app.callback(Output('output', 'children'),
              [Input('table', 'cols'),
               Input('table', 'rows'),
               Input('table', 'rowOrder'),
               Input('table', 'colOrder'),
               Input('table', 'aggregatorName'),
               Input('table', 'rendererName'),
               Input('table', 'data')])
def display_props(cols, rows, row_order, col_order, aggregator, renderer, data_input):
    return [
        html.P(str(cols), id='columns'),
        html.P(str(rows), id='rows'),
        html.P(str(row_order), id='row_order'),
        html.P(str(col_order), id='col_order'),
        html.P(str(aggregator), id='aggregator'),
        html.P(str(renderer), id='renderer'),
        html.P(f'Data length: {len(data_input)}', id='data_length'),
    ]


@app.callback(Output('table', 'data'),
              [Input('toggle-data-button', 'n_clicks')],
              prevent_initial_call=True)
def toggle_data(n_clicks):
    if n_clicks % 2 == 0:
        return data
    return data[:len(data)//2]


if __name__ == '__main__':
    app.run_server(debug=True)
