
```dataview
TASK FROM ("01/Work" or "01/Journal" or "Zettel")
WHERE !completed
GROUP BY file.cday
sort file.cday desc
```
