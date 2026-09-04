---
Type:
Created: 2026-09-02 19:17
---
You can’t just update content list. You shall also update contract list at the same time. Otherwise, in the future, when someone update contract list of that item, you will accidentally create additional record in content list because no. of lines is 2 not 1. Or when you correct something in contract list, and expect it would be synced to content list, it would not, because contract type is VO Production.

---
For this syndication records, [The Season](https://pccw0.sharepoint.com/sites/OTTContract/Lists/Contract%20list/DispForm.aspx?ID=2980&e=aoXBdu), Number of lines of this record shall be 1. Otherwise, next time you update this contract record, it would check the content list again. If it find there is only 1 record linked to contract list, then it would create extra record again.

For this VO Production record, [The Season](https://pccw0.sharepoint.com/sites/OTTContract/Lists/Contract%20list/DispForm.aspx?ID=3100&e=YR4pv5), you shall input “add to content list” in the field “Remark of reference contract”. [@Ong, Nicole SH](mailto:Nicole.SH.Ong@pccw.com) as mentioned, for VO production, it is not supposed to create through contract list, if you have to create content record through contract list, you shall input “add to content list” in the field “Remark of reference contract”