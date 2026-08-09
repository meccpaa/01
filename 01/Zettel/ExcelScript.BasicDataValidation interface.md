```typescript
/**
 * This script creates a data validation rule for the range B1:B5.
 * All values in that range must be a positive number.
 * Attempts to enter other values are blocked and an error message appears.
 */
function main(workbook: ExcelScript.Workbook) {
  // Get the range B1:B5 in the active worksheet.
  const currentSheet = workbook.getActiveWorksheet();
  const positiveNumberOnlyCells = currentSheet.getRange("B1:B5");

  // Create a data validation rule to only allow positive numbers.
  const positiveNumberValidation: ExcelScript.BasicDataValidation = {
    formula1: "0",
    operator: ExcelScript.DataValidationOperator.greaterThan
  };
  const positiveNumberOnlyRule: ExcelScript.DataValidationRule = {
    wholeNumber: positiveNumberValidation
  };

  // Set the rule on the range.
  const rangeDataValidation = positiveNumberOnlyCells.getDataValidation();
  rangeDataValidation.setRule(positiveNumberOnlyRule);

  // Create an alert to appear when data other than positive numbers are entered.
  const positiveNumberOnlyAlert: ExcelScript.DataValidationErrorAlert = {
    message: "Positive numbers only",
    showAlert: true,
    style: ExcelScript.DataValidationAlertStyle.stop,
    title: "Invalid data"
  };
  rangeDataValidation.setErrorAlert(positiveNumberOnlyAlert);
}
```