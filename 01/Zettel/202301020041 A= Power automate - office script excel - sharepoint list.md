**Attachment**:: 
**Date**:: 2023-01-02T00:41:00
**Action**::  
**Topics**:: 
**Type**:: [[Activity]]
**Remarks**:: 
**Person**:: 
**Link**:: 
**Thread**:: 

---
## Notes
https://www.youtube.com/watch?v=4g8Lh0gzEnc
Download sample script [https://github.com/DamoBird365/PowerA...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbmxLTkc5WWd3bDVpMDRIZ0E2QUk3LVV3d01zd3xBQ3Jtc0ttdTJ4dEwxZVF6R2pic3NyOTB6WWo4UTJSWHVzTjdQcHc4Zkx2WDFFX1g4YTYxVmR5bHAtMC1YTV9xVnBWejF1bHZWNDFsYWVQTzI4N2JpUTdKZTNmXzg5Y1Y3VVkxQTVaSngtM1BNZk1WZERoZjlpZw&q=https%3A%2F%2Fgithub.com%2FDamoBird365%2FPowerAutomate%2Fblob%2Fmain%2FOfficeScripts%2FCreateNewTable%2520Office%2520Script.txt&v=4g8Lh0gzEnc)

```vb
function main(workbook: ExcelScript.Workbook,
  arrayfromflow: arrayofdata[],
  sheetname: string 
) {
  let selectedSheet = workbook.getActiveWorksheet();

  // Set range A1:F1 on selectedSheet
  selectedSheet.getRange("A1:F1").setValues([["ID", "FirstName", "LastName", "Address", "PostCode", "Email"]]);

  // Add a new table at range A1:F1 on selectedSheet
  // Optional if you want to use ADD Row Into Table
  let newTable = workbook.addTable(selectedSheet.getRange("A1:F1"), true);
  newTable.setName('MyTableName')

  selectedSheet.setName(sheetname);

  //Populate rows below Header Row with Array Variable 
  const starterrow = 2; //starting row for "table" data

  for (let i = 0; i < arrayfromflow.length; i++) {
    const currentObject = arrayfromflow[i];

    const formattedrow = [[currentObject.ID, currentObject.FirstName, currentObject.LastName, currentObject.Address, currentObject.PostCode, currentObject.Email]];

    const rowRange = `A${starterrow + i}:F${starterrow + i}`;
    selectedSheet.getRange(rowRange).setValues(formattedrow);
  }
}

//Defining Interfaces for MultiVar and Array

interface arrayofdata {
ID: string,
FirstName: string,
LastName: string,
Address: string,
PostCode: string,
Email: string
}

```