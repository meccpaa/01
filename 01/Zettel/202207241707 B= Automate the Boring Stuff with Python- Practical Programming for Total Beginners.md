**Attachment**:: 
**Date**:: 2022-07-24T17:07:00
**Action**::  
**Topics**:: [[Python]], [[openpyxl]]
**Type**:: [[Book]]
**Remarks**:: 
**Person**:: 
**Link**:: 
**Thread**:: 

---
## Notes

### Chapter 12. Working with Excel Spreadsheets
[[openpyxl]]
[[openpy.py]]
	- [[Excel openpy.xlsx]]
		- wb=openpyxl.load_workbook
		- wb.get_sheet_names()
		- get_sheet_by_name
		- sheet.title
		- type(sheet)
		- wb.get_active_sheet()
	- [[Openpy get cells.py]]
		- wb.get_sheet_by_name('Sheet1')
		- c= sheet['C2']
			- c.value, c.row, c.column, c.coordinate
			- sheet['C2'].value