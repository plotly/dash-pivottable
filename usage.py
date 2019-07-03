import dash_pivottable
import dash
import dash_core_components as dcc
from data import data
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

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
    dcc.Markdown(
        id='output'
    )
])


@app.callback(Output('output', 'children'),
              [Input('table', 'cols'),
               Input('table', 'rows'),
               Input('table', 'rowOrder'),
               Input('table', 'colOrder'),
               Input('table', 'aggregatorName'),
               Input('table', 'rendererName')])
def display_props(cols, rows, row_order, col_order, aggregator, renderer):
    return """
        Columns: {}
        
        rows: {}
        
        rowOrder: {}
        
        colOrder: {}
        
        aggregatorName: {}
        
        rendererName: {}
    """.format(str(cols), str(rows), row_order, col_order, aggregator, renderer)


if __name__ == '__main__':
    app.run_server(debug=True)
