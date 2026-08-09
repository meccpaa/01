```TypeScript
addChart(
            type: ChartType,
            sourceData: Range,
            seriesBy?: ChartSeriesBy
        ): Chart;
```

```TypeScript
/**
 * This sample creates a column-clustered chart based on the current worksheet's data.
 */
function main(workbook: ExcelScript.Workbook) {
  // Get the current worksheet.
  let selectedSheet = workbook.getActiveWorksheet();

  // Get the data range.
  let range = selectedSheet.getUsedRange();

  // Insert a chart using the data on the current worksheet.
  let chart = selectedSheet.addChart(ExcelScript.ChartType.columnClustered, range);

  // Name the chart for easy access in other scripts.
  chart.setName("ColumnChart");
}
```