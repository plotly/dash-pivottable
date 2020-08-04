# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class PivotTable(Component):
    """A PivotTable component.
Pivot tables are useful for interactive presentation of  
summary statistics computed for data contained in another table.

This function provides a convenient Dash interface 
to the `react-pivottable` component, which makes it easy to embed
pivot tables into Dash for R applications.

Within React, the interactive component provided by `react-pivottable`
is `PivotTableUI`, but output rendering is delegated to the non-interactive 
`PivotTable` component, which accepts a subset of its properties.
`PivotTable` in turn delegates to a specific renderer component, such as
the default `TableRenderer`, which accepts a subset of the same properties.
Finally, most renderers will create non-React PivotData objects to handle
the actual computations, which also accept a subset of the same properties
as the rest of the stack.

The arguments for this function correspond to properties of the component;
a full list is provided below.

`react-pivottable` was developed by Nicolas Kruchten; source
for this component is available from https://github.com/plotly/react-pivottable.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks
- data (list; optional): data to be summarized
- hiddenAttributes (list; optional): contains attribute names to omit from the UI
- hiddenFromAggregators (list; optional): contains attribute names to omit from the aggregator arguments dropdowns
- hiddenFromDragDrop (list; optional): contains attribute names to omit from the drag'n'drop portion of the UI
- menuLimit (number; default 500): maximum number of values to list in the double-click menu
- unusedOrientationCutoff (number; default 85): If the attributes' names' combined length in characters exceeds this
value then the unused attributes area will be shown vertically to the
left of the UI instead of horizontally above it. 0 therefore means
'always vertical', and Infinity means 'always horizontal'.
- cols (list; optional): Which columns are currently in the column area
- colOrder (string; optional): the order in which column data is provided to the renderer, must be one
of "key_a_to_z", "value_a_to_z", "value_z_to_a", ordering by value
orders by column total
- rows (list; optional): Which rows is currently inside the row area.
- rowOrder (string; optional): the order in which row data is provided to the renderer, must be one
of "key_a_to_z", "value_a_to_z", "value_z_to_a", ordering by value
orders by row total
- aggregatorName (string; optional): Which aggregator is currently selected. E.g. Count, Sum, Average, etc.
- vals (list; optional): Vals for the aggregator.
- valueFilter (dict; optional): Value filter for each attibute name.
- rendererName (string; optional): Which renderer is currently selected. E.g. Table, Line Chart, Scatter
Chart, etc."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, data=Component.UNDEFINED, hiddenAttributes=Component.UNDEFINED, hiddenFromAggregators=Component.UNDEFINED, hiddenFromDragDrop=Component.UNDEFINED, menuLimit=Component.UNDEFINED, unusedOrientationCutoff=Component.UNDEFINED, cols=Component.UNDEFINED, colOrder=Component.UNDEFINED, rows=Component.UNDEFINED, rowOrder=Component.UNDEFINED, aggregatorName=Component.UNDEFINED, vals=Component.UNDEFINED, valueFilter=Component.UNDEFINED, rendererName=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'data', 'hiddenAttributes', 'hiddenFromAggregators', 'hiddenFromDragDrop', 'menuLimit', 'unusedOrientationCutoff', 'cols', 'colOrder', 'rows', 'rowOrder', 'aggregatorName', 'vals', 'valueFilter', 'rendererName']
        self._type = 'PivotTable'
        self._namespace = 'dash_pivottable'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data', 'hiddenAttributes', 'hiddenFromAggregators', 'hiddenFromDragDrop', 'menuLimit', 'unusedOrientationCutoff', 'cols', 'colOrder', 'rows', 'rowOrder', 'aggregatorName', 'vals', 'valueFilter', 'rendererName']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(PivotTable, self).__init__(**args)
