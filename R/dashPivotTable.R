# AUTO GENERATED FILE - DO NOT EDIT

dashPivotTable <- function(id=NULL, data=NULL, hiddenAttributes=NULL, hiddenFromAggregators=NULL, hiddenFromDragDrop=NULL, menuLimit=NULL, unusedOrientationCutoff=NULL, cols=NULL, colOrder=NULL, rows=NULL, rowOrder=NULL, aggregatorName=NULL, vals=NULL, valueFilter=NULL, rendererName=NULL) {
    
    props <- list(id=id, data=data, hiddenAttributes=hiddenAttributes, hiddenFromAggregators=hiddenFromAggregators, hiddenFromDragDrop=hiddenFromDragDrop, menuLimit=menuLimit, unusedOrientationCutoff=unusedOrientationCutoff, cols=cols, colOrder=colOrder, rows=rows, rowOrder=rowOrder, aggregatorName=aggregatorName, vals=vals, valueFilter=valueFilter, rendererName=rendererName)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'PivotTable',
        namespace = 'dash_pivottable',
        propNames = c('id', 'data', 'hiddenAttributes', 'hiddenFromAggregators', 'hiddenFromDragDrop', 'menuLimit', 'unusedOrientationCutoff', 'cols', 'colOrder', 'rows', 'rowOrder', 'aggregatorName', 'vals', 'valueFilter', 'rendererName'),
        package = 'dashPivottable'
        )

    structure(component, class = c('dash_component', 'list'))
}
