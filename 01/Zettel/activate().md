```TypeScript
activate(): void;
```

```TypeScript
/**
 * This script switches the active view to a worksheet named "Data", if it exists.
 */
function main(workbook: ExcelScript.Workbook) {
  // Check if the "Data" worksheet exists.
  let dataWorksheet = workbook.getWorksheet("Data");
  if (dataWorksheet) {
    // Switch to the "Data" worksheet.
    dataWorksheet.activate();
  } else {
    console.log(`No worksheet named "Data" in this workbook.`);
  }
}
```