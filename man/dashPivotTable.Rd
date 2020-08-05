% Auto-generated: do not edit by hand
\name{dashPivotTable}

\alias{dashPivotTable}

\title{PivotTable component}

\description{
Pivot tables are useful for interactive presentation of   summary statistics computed for data contained in another table.  This function provides a convenient Dash interface  to the `react-pivottable` component, which makes it easy to embed pivot tables into Dash for R applications.  Within React, the interactive component provided by `react-pivottable` is `PivotTableUI`, but output rendering is delegated to the non-interactive  `PivotTable` component, which accepts a subset of its properties. `PivotTable` in turn delegates to a specific renderer component, such as the default `TableRenderer`, which accepts a subset of the same properties. Finally, most renderers will create non-React PivotData objects to handle the actual computations, which also accept a subset of the same properties as the rest of the stack.  The arguments for this function correspond to properties of the component; a full list is provided below.  `react-pivottable` was developed by Nicolas Kruchten; source for this component is available from https://github.com/plotly/react-pivottable.
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

\examples{
# Input data for dashPivottable may be passed in the "list-of-lists"
# format -- scroll down to see an example which demonstrates how
# to pass a data.frame into dashPivottable directly.
if (interactive() && require(dash)) {
  library(dash)
  library(dashPivottable)
  library(dashHtmlComponents)

  app <- Dash$new()
  app$title("Summary statistics for tips data")

  app$layout(
    htmlDiv(
      list(
        dashPivotTable(
          id = "table",
          data = tips,
          cols = list("Day of Week"),
          colOrder = "key_a_to_z",
          rows = list("Party Size"),
          rowOrder = "key_a_to_z",
          rendererName = "Grouped Column Chart",
          aggregatorName = "Average",
          vals = list("Total Bill"),
          valueFilter = list("Day of Week"=list("Thursday"=FALSE))
        ),
        htmlDiv(
          id = "output"
        )
      )
    )
  )

  app$callback(output = output(id="output", property="children"),
              params = list(input(id="table", property="cols"),
                            input(id="table", property="rows"),
                            input(id="table", property="rowOrder"),
                            input(id="table", property="colOrder"),
                            input(id="table", property="aggregatorName"),
                            input(id="table", property="rendererName")),
              function(cols, rows, row_order, col_order, aggregator, renderer) {
                return(
                  list(
                    htmlP(cols, id="columns"),
                    htmlP(rows, id="rows"),
                    htmlP(row_order, id="row_order"),
                    htmlP(col_order, id="col_order"),
                    htmlP(aggregator, id="aggregator"),
                    htmlP(renderer, id="renderer")
                  )
                )
              }
  )

  app$run_server(debug=TRUE)

  # This example illustrates the use of `df_to_list` to format a data.frame
  # for use with dashPivottable
  library(dashTable)

  app <- Dash$new()
  app$title("Summary statistics for iris data")

  app$layout(
    htmlDiv(
      list(
        dashPivotTable(
          id = "table",
          data = df_to_list(Loblolly),
          cols = list("Seed"),
          colOrder = "key_a_to_z",
          rows = list("age"),
          rowOrder = "key_a_to_z",
          rendererName = "Grouped Column Chart",
          aggregatorName = "Average",
          vals = list("height")
        ),
        htmlDiv(
          id = "output"
        )
      )
    )
  )

  app$callback(output = output(id="output", property="children"),
              params = list(input(id="table", property="cols"),
                            input(id="table", property="rows"),
                            input(id="table", property="rowOrder"),
                            input(id="table", property="colOrder"),
                            input(id="table", property="aggregatorName"),
                            input(id="table", property="rendererName")),
              function(cols, rows, row_order, col_order, aggregator, renderer) {
                return(
                  list(
                    htmlP(cols, id="columns"),
                    htmlP(rows, id="rows"),
                    htmlP(row_order, id="row_order"),
                    htmlP(col_order, id="col_order"),
                    htmlP(aggregator, id="aggregator"),
                    htmlP(renderer, id="renderer")
                  )
                )
              }
  )

  app$run_server(debug=TRUE)
}
}
