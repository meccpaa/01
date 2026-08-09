
```TypeScript
/**
 * This script creates a new worksheet named "Plum" and sets its tab color to purple.
 */
function main(workbook: ExcelScript.Workbook) {
  const newSheet = workbook.addWorksheet("Plum")
  newSheet.setTabColor("purple");
}
```

### Methods
[[addChart(type, sourceData, seriesBy)]] 
[[activate()]] 
[[addComment(cellAddress, content, contentType)]]
