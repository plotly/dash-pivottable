import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_pivottable

from data import data

app = dash.Dash(__name__)
app.title = 'My Dash example'

VALUE_FILTER_DEFAULT = {'Day of Week': {'Thursday': False}}
VALUE_FILTER_ALT = {'Day of Week': {'Friday': False}}

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
        valueFilter=VALUE_FILTER_DEFAULT,
    ),
    html.Button('Toggle data', id='toggle-data-button', n_clicks=0),
    html.Button('Toggle filter', id='toggle-filter-button', n_clicks=0),
    html.Button('Toggle rows and cols', id='toggle-rows-cols-button', n_clicks=0),
    html.Button('Toggle order', id='toggle-order-button', n_clicks=0),
    html.Button('Toggle analysis', id='toggle-analysis-button', n_clicks=0),
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
               Input('table', 'data'),
               Input('table', 'valueFilter')])
def display_props(cols, rows, row_order, col_order, aggregator, renderer, data_input, value_filter):
    return [
        html.P(str(cols), id='columns'),
        html.P(str(rows), id='rows'),
        html.P(str(row_order), id='row_order'),
        html.P(str(col_order), id='col_order'),
        html.P(str(aggregator), id='aggregator'),
        html.P(str(renderer), id='renderer'),
        html.P(str(value_filter), id='value_filter'),
        html.P(f'Data length: {len(data_input)}', id='data_length'),
    ]


@app.callback(Output('table', 'data'),
              [Input('toggle-data-button', 'n_clicks')],
              prevent_initial_call=True)
def toggle_data(n_clicks):
    if n_clicks % 2 == 0:
        return data
    return data[:len(data)//2]


@app.callback(Output('table', 'valueFilter'),
              [Input('toggle-filter-button', 'n_clicks')],
              prevent_initial_call=True)
def toggle_filter(n_clicks):
    if n_clicks % 2 == 0:
        return VALUE_FILTER_DEFAULT
    return VALUE_FILTER_ALT


@app.callback([Output('table', 'rows'),
               Output('table', 'cols')],
              [Input('toggle-rows-cols-button', 'n_clicks')],
              [State('table', 'rows'),
               State('table', 'cols')],
              prevent_initial_call=True)
def toggle_rows_cols(_n_clicks, rows, cols):
    return cols, rows


@app.callback([Output('table', 'rowOrder'),
               Output('table', 'colOrder')],
              [Input('toggle-order-button', 'n_clicks')],
              [State('table', 'rowOrder'),
               State('table', 'colOrder')],
              prevent_initial_call=True)
def toggle_order(_n_clicks, row_order, col_order):

    def switch_order(order):
        if order == 'key_a_to_z':
            return 'value_z_to_a'
        return 'key_a_to_z'

    return switch_order(row_order), switch_order(col_order)


@app.callback([Output('table', 'rendererName'),
               Output('table', 'aggregatorName'),
               Output('table', 'vals')],
              [Input('toggle-analysis-button', 'n_clicks')],
              [State('table', 'rendererName'),
               State('table', 'aggregatorName'),
               State('table', 'vals')],
              prevent_initial_call=True)
def toggle_analysis(_n_clicks, renderer_name, aggregator_name, vals):
    renderer_name = 'Grouped Column Chart' if renderer_name == 'Line Chart' else 'Line Chart'
    aggregator_name = 'Average' if aggregator_name == 'Sum' else 'Sum'
    vals = ['Total Bill'] if vals == ['Party Size'] else ['Party Size']
    return renderer_name, aggregator_name, vals


if __name__ == '__main__':
    app.run_server(debug=True)
