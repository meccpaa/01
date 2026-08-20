---
Type: Journal
Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
---
[[<% moment(tp.file.title, "YYYY-MM-DD").subtract(1, "days").format("YYYY-MM-DD") %>|← Yesterday]] | [[<% moment(tp.file.title, "YYYY-MM-DD").add(1, "days").format("YYYY-MM-DD") %>|Tomorrow →]]
## Journal




---
## Lesson learnt


## Due Tasks 
```tasks 
not done
due before {{date:YYYY-MM-DD}} 
sort by due 
```

## Coming Tasks
```tasks
not done
due after {{date:YYYY-MM-DD}}
due before {{date:YYYY-MM-DD+30d}}
sort by due
is not recurring
```
## Completed tasks today
```dataview 

TASK WHERE completion != null AND completion = date({{date:YYYY-MM-DD}})
```
