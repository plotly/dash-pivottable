<!--
Thanks for your interest in Plotly's Dash Pivottable Component!

Note that GitHub issues in this repo are reserved for bug reports and feature
requests. Implementation questions should be discussed in our
[Dash Community Forum](https://community.plotly.com/c/dash).

Before opening a new issue, please search through existing issues (including
closed issues) and the [Dash Community Forum](https://community.plotly.com/c/dash).

When reporting a bug, please include a reproducible example! We recommend using
the [latest version](https://github.com/plotly/dash-pivottable/blob/master/CHANGELOG.md)
as this project is frequently updated. Issues can be browser-specific so
it's usually helpful to mention the browser and version that you are using.

-->

#### Description

#### Steps/Code to Reproduce
<!--
Example:
```python
import dash_pivottable
import dash
import dash_core_components as dcc
from data import data
from dash.dependencies import Input, Output
import dash_html_components as html

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
    dcc.Markdown(
        id='output'
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
```
If the code is too long, feel free to put it in a public gist and link
it in the issue: https://gist.github.com
-->

#### Expected Results
<!-- Please paste or describe the expected results.-->

#### Actual Results
<!-- Please paste or specifically describe the actual output or traceback. -->

#### Versions
<!--
Please run the following snippet and paste the output below:

from __future__ import print_function
import dash; print("Dash", dash.__version__)
import dash_html_components; print("Dash Core Components", dash_html_components.__version__)
import dash_core_components; print("Dash HTML Components", dash_core_components.__version__)
import dash_renderer; print("Dash Renderer", dash_renderer.__version)
import dash_pivottable; print("Dash HTML Components", dash_cytoscape.__version__)
-->


<!-- 
Thanks for taking the time to help up improve this component. Dash Pivottable 
would not be possible without awesome contributors like you!
 -->
