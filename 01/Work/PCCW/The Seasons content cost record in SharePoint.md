---
Type:
Created: 2026-09-02 19:17
---
You can’t just update content list. You shall also update contract list at the same time. Otherwise, in the future, when someone update contract list of that item, you will accidentally create additional record in content list because no. of lines is 2 not 1. Or when you correct something in contract list, and expect it would be synced to content list, it would not, because contract type is VO Production.