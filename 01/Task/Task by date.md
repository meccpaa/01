
```dataview
TASK FROM ("Work" or "Journal" or "Zettel")
WHERE !completed
GROUP BY file.cday
sort file.cday desc
```
