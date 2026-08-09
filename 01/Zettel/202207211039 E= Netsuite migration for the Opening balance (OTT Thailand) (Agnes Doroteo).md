**Attachment**:: 
**Date**:: 2022-07-21T10:39:00
**Action**::  
**Topics**:: [[Netsuite Migration]], [[v.TH]]
**Type**:: [[Email]]
**Remarks**:: 
**Person**:: [[Agnes Doroteo]]
**Link**:: [AppLink](outlook:000000003F422DF24198BB43AE0AB2183C680E770700D4D2347232E0A0478424CFB59F08075F000019BBEE560000A8FE1A0899C12544BB5C3069D18441490000B90999820000), [WebLink](https://outlook.office365.com/owa/?ItemID=AAMkADliODdmMzUzLTllZmMtNGU1Yy1iMWQzLTQ1N2ZiNGM4NjJkMgBGAAAAAAA-Qi3yQZi7Q64Kshg8aA53BwDU0jRyMuCgR4Qkz7WfCAdfAAAZu_5WAACo-hoImcElRLtcMGnRhEFJAAC5CZmCAAA=&exvsurl=1&viewmodel=ReadMessageItem)
**Thread**:: [[Netsuite migration for the Opening balance (OTT Thailand)]]

---
## Notes

Vuclip migration for the Opening balance (OTT Thailand)
	
Option 1	If January 1, 2022 is the cutoff date
1	Import TB as of Jan 1 (use the Opening Balance account for AR,AP)
2	Import Opening AR, AP as of Jan 1
3	Enter any catchup transactions from January 1 (to be entered manually in UI)
	
	To reverse the imported AR, AP as of Jan 31
4	Create reversal Journal Entry (vendor, customer should be tagged on the JE lines)
5	Use the reversal journal to close the imported open AR, AP as of Jan 31 (Make Payment, Accept Payment)
	
Option 2	If January 31, 2022 is the cutoff date
1	Import TB as of January 31, 2022 (use the Opening Balance account for AR,AP)
