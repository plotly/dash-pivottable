% Auto-generated: do not edit by hand
\name{dashPivotTable}

\alias{dashPivotTable}

\title{PivotTable component}

\description{
Pivot tables are useful for interactive presentation of   summary statistics computed for data contained in another table.  The `dashPivottable` function provides a convenient Dash interface  to the `react-pivottable` component, which makes it easy to embed pivot tables into Dash for R applications.  Within React, the interactive component provided by `react-pivottable` is `PivotTableUI`, but output rendering is delegated to the non-interactive  `PivotTable` component, which accepts a subset of its properties. `PivotTable` in turn delegates to a specific renderer component, such as the default `TableRenderer`, which accepts a subset of the same properties. Finally, most renderers will create non-React PivotData objects to handle the actual computations, which also accept a subset of the same properties as the rest of the stack.  The arguments for `dashPivottable` corresepond to properties of the component; a full list is provided below.  `react-pivottable` was developed by Nicolas Kruchten; source for this component is available from https://github.com/plotly/react-pivottable.
}

\usage{
dashPivotTable(id=NULL, data=NULL, hiddenAttributes=NULL,
hiddenFromAggregators=NULL, hiddenFromDragDrop=NULL,
menuLimit=NULL, unusedOrientationCutoff=NULL, cols=NULL,
colOrder=NULL, rows=NULL, rowOrder=NULL,
aggregatorName=NULL, vals=NULL, valueFilter=NULL,
rendererName=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks}

\item{data}{Unnamed list. data to be summarized}

\item{hiddenAttributes}{Unnamed list. contains attribute names to omit from the UI}

\item{hiddenFromAggregators}{Unnamed list. contains attribute names to omit from the aggregator arguments dropdowns}

\item{hiddenFromDragDrop}{Unnamed list. contains attribute names to omit from the drag'n'drop portion of the UI}

\item{menuLimit}{Numeric. maximum number of values to list in the double-click menu}

\item{unusedOrientationCutoff}{Numeric. If the attributes' names' combined length in characters exceeds this
value then the unused attributes area will be shown vertically to the
left of the UI instead of horizontally above it. 0 therefore means
'always vertical', and Infinity means 'always horizontal'.}

\item{cols}{Unnamed list. Which columns are currently in the column area}

\item{colOrder}{Character. the order in which column data is provided to the renderer, must be one
of "key_a_to_z", "value_a_to_z", "value_z_to_a", ordering by value
orders by column total}

\item{rows}{Unnamed list. Which rows is currently inside the row area.}

\item{rowOrder}{Character. the order in which row data is provided to the renderer, must be one
of "key_a_to_z", "value_a_to_z", "value_z_to_a", ordering by value
orders by row total}

\item{aggregatorName}{Character. Which aggregator is currently selected. E.g. Count, Sum, Average, etc.}

\item{vals}{Unnamed list. Vals for the aggregator.}

\item{valueFilter}{Named list. Value filter for each attibute name.}

\item{rendererName}{Character. Which renderer is currently selected. E.g. Table, Line Chart, Scatter
Chart, etc.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

