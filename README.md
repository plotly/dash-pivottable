# Dash Pivottable

Dash Pivottable is a Dash component wrapping the [react-pivottable library](https://github.com/plotly/react-pivottable/), created by Plotly. It lets you build interactive pivottable using purely Python.

## Getting Started

Make sure to clone this project, create a venv and install requirements:
```commandline
$ git clone https://github.com/xhlulu/dash_pivottable.git
$ cd dash_pivottable
$ virtualenv venv
$ venv/Scripts/activate
$ pip install -r requirements.txt
```

And simply run the example:
```commandline
python usage.py
```

## References

The following parameters can be modified:
- id (string; optional): The ID used to identify this component in Dash callbacks
- data (list; optional): The input data
- hiddenAttributes (list; optional): contains attribute names to omit from the UI
- hiddenFromAggregators (list; optional): contains attribute names to omit from the aggregator arguments dropdowns
- hiddenFromDragDrop (list; optional): contains attribute names to omit from the drag'n'drop portion of the UI
- menuLimit (number; optional): maximum number of values to list in the double-click menu
- unusedOrientationCutoff (number; optional): If the attributes' names' combined length in characters exceeds this
value then the unused attributes area will be shown vertically to the
left of the UI instead of horizontally above it. 0 therefore means
'always vertical', and Infinity means 'always horizontal'.

The following props can be used as an input to callbacks, but can't be modified:
- cols (list; optional): Which columns are currently in the column area
- colOrder (string; optional): the order in which column data is provided to the renderer, must be one
of "key_a_to_z", "value_a_to_z", "value_z_to_a", ordering by value
orders by column total
- rows (list; optional): Which rows is currently inside the row area.
- rowOrder (string; optional): the order in which row data is provided to the renderer, must be one
of "key_a_to_z", "value_a_to_z", "value_z_to_a", ordering by value
orders by row total
- aggregatorName (string; optional): Which aggregator is currently selected. E.g. Count, Sum, Average, etc.
- rendererName (string; optional): Which renderer is currently selected. E.g. Table, Line Chart, Scatter

Default Values:
* menuLimit: 500
* unusedOrientationCutoff: 85
* hiddenAttributes: []
* hiddenFromAggregators: []
* hiddenFromDragDrop: []
    
## Notice

 This is currently a community-maintained library, and is not an official Plotly product. If you would like to develop this, please reach out to me. If you would like to see official support, please reach out to [Plotly directly](https://plot.ly/products/consulting-and-oem/).
