
```dataview
    TABLE dateformat(file.mtime, "dd-MM-yy HH:mm") as "Last modified", dateformat(file.ctime, "dd-MM-yy") as "Created date", Type FROM -"templates"
    SORT file.mtime DESC
    WHERE file.mtime >= date(today) - dur(1 week)
    WHERE file.ctime >= date(today) - dur(1 week)
```
