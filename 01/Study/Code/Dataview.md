---
alias: "document" 
last-reviewed: 2021-08-17 
thoughts: 
	rating: 8 
	reviewable: false 
---

# Overview
### Basic Usage
Dataview has two major components: _annotation_ and _querying_. Each operates largely independently and are described below.

#### Annotation
The dataview **index** is responsible for constantly parsing markdown files and other metadata in your vault, creating an in-memory index which allows for fast queries over your data. Annotation is done at the _markdown page_, _section_, and _task_ level, where you can either use:

1.  **Frontmatter**, a common Markdown extension which allows for adding arbitrary YAML at the top of a document) (at the top) 
2. **Inline Fields**, a Dataview-specific way to provide metadata in an intuitive `Key:: Value` syntax:
	- abc **completion**:: 2022-06-18
- [x] I am a task with [metadata::value]! [completion:: 2022-06-18]
  - [X] I am another task with completed::2020-09-15

You can combine both methods if desired. Dataview also adds a significant number of "implicit" fields, like `file.name` for the file name, `file.size` for the size, and so on; you can find more details in the [data annotation documentation](https://blacksmithgu.github.io/obsidian-dataview/data-annotation).

#### Querying
Once you have some pages that you've annotated, all that's left to do is query them to create dynamic table, list, or JavaScript views. There are four ways to do this:

1.  **Dataview Query Language (DQL)**: A pipeline-based, vaguely SQL-looking expression language which can support basic use cases. See the [guide](https://blacksmithgu.github.io/obsidian-dataview/writing-dql) for an overview of how to use DQL, or check out the [reference material](https://blacksmithgu.github.io/obsidian-dataview/query/queries/) for details.
    
    ```dataview
    TABLE file.name AS "File", rating AS "Rating" FROM #book 
    ```

2.  **Inline Expressions**: DQL expressions which you can embed directly inside markdown and which will be evaluated in preview mode. See the [documentation](https://blacksmithgu.github.io/obsidian-dataview/query/expressions/) for allowable queries.
    
    We are on page `= this.file.name`.
    
3.  **DataviewJS**: A high-powered JavaScript API which gives full access to the Dataview index and some convienent rendering utilities. Highly recommended if you know JavaScript, since this is far more powerful than the query language. Check the [documentation](https://blacksmithgu.github.io/obsidian-dataview/api/intro/) for more details.
    -> [[Task (by page)]]

4.  **Inline JS Expressions**: The JavaScript equivalent to inline expressions, which allow you to execute arbitary JS inline:
    
    This page was last modified at `$= dv.current().file.mtime`

# Data Annotation
Dataview is a data index first and foremost, so it supports relatively rich ways of adding metadata to your knowledge base. Dataview tracks information at the _markdown page_ and _markdown task_ levels, where each page/task can have an arbitrary amount of complex (numbers, objects, lists) _fields_ associated with it. Each _field_ is a named value with a certain type (like "number" or "text").

### Pages
You can add fields to a markdown page in three different ways:

1.  **Frontmatter**: Frontmatter is a common Markdown extension which allows for YAML metadata to be added to the top of a page. All YAML fields will be available as Dataview fields:
2. **Inline Fields**: For those wanting a more natural-looking annotation, Dataview supports "inline" fields, which offer a simple `Key:: Value` syntax that you can embed directly in your file:
	If you want to embed metadata inside sentences, or multiple fields on the same line, you can use the bracket syntax:
	I would rate this a [rating:: 9]! It was [mood:: acceptable].
3. **Implicit**: Dataview annotates pages with a large amount of metadata automatically, like the day the file was created (`file.cday`), any associated dates (`file.day`), links in the file (`file.outlinks`), tags (`file.tags`), and so on.

[[Implicit Fields]]

### Tasks
You can also annotate your _tasks_ (I.e., lines of the form `- [ ] blah blah blah`) with metadata using inline field syntax:

`- [ ] Hello, this is some [metadata:: value]! - [X] I finished this on [completion::2021-08-15].`

#### Field Shorthands

For supporting "common use cases", Dataview understands a few shorthands for common data you may want to annotate task with:

Syntax

-   Due Date: `🗓️YYYY-MM-DD`
-   Completed Date: `✅YYYY-MM-DD`
-   Created Date: `➕YYYY-MM-DD`

Example

-   Do this saturday 🗓️2021-08-29.
-   Completed last saturday ✅2021-08-22.
-   I made this on ➕1990-06-14.

Note that, if you do not like emojis, you can still annotate these fields textually (`[due:: ]`, `[created:: ]`, `[completion:: ]`).

#### Implicit Fields

As with pages, Dataview adds a number of implicit fields to each task:

-   Tasks inherit _all fields_ from their parent page - so if you have a `rating` field in your page, you can also access it on your task.
-   `status`: The completion status of this task, as determined by the character inside the `[ ]`brackets. Generally a space `" "` for incomplete tasks and an X `"X"` for complete tasks, but allows for plugins which support alternative task statuses.
-   `checked`: Whether or not this task has been checked in any way (i.e., it's status is not incomplete/empty).
-   `completed`: Whether or not this _specific_ task has been completed; this does not consider the completion/non-completion of any child tasks. A task is explicitly considered "completed" if it has been marked with an 'X'.
-   `fullyCompleted`: Whether or not this task and **all** of its subtasks are completed.
-   `text`: The text of this task.
-   `line`: The line this task shows up on.
-   `lineCount`: The number of Markdown lines that this task takes up.
-   `path`: The full path of the file this task is in.
-   `section`: A link to the section this task is contained in.
-   `tags`: Any tags inside of the text task.
-   `outlinks`: Any links defined in this task.
-   `link`: A link to the closest linkable block near this task; useful for making links which go to the task.
-   `children`: Any subtasks or sublists of this task.
-   `task`: If true, this is a task; otherwise, it is a regular list element.
-   `completion`: The date a task was completed; set by `[completion:: ...]` or shorthand syntax.
-   `due`: The date a task is due, if it has one. Set by `[due:: ...]` or shorthand syntax.
-   `created`: The date a task was created; set by `[created:: ...]` or shorthand syntax.
-   `annotated`: True if the task has any custom annotations, and false otherwise.
-   `parent`: The line number of the task above this task, if present; will be null if this is a root-level task.
-   `blockId`: The block ID of this task / list element, if one has been defined with the `^blockId` syntax; otherwise null.


### Field Types
All fields in dataview have a _type_, which determines how dataview will render, sort, and operate on that field. Dataview understands several distinct field types to cover common use cases:

-   **Text**: The default catch-all. If a field doesn't match a more specific type, it is just plain text.
    
    `Example:: This is some normal text.`
    
-   **Number**: Numbers like '6' and '3.6'.
    
    `Example:: 6 Example:: 2.4 Example:: -80`
    
-   **Boolean**: true/false, as the programming concept.
    
    `Example:: true Example:: false`
    
-   **Date**: ISO8601 dates of the general form `YYYY-MM[-DDTHH:mm:ss.nnn+ZZ]`. Everything after the month is optional.
    
    Example:: 2021-04-18 
    Example:: 2021-04-18T04:19:35.000 
    Example:: 2021-04-18T04:19:35.000+06:30`
    
-   **Duration**: Durations of the form `<time> <unit>`, like `6 hours` or `4 minutes`. Common english abbreviations like `6hrs` or `2m` are accepted. You can specify multiple units using an optional comma separator: `6 hours, 4 minutes` or `6hr4min`.
    Example:: 7 hours 
    Example:: 4min 
    Example:: 16 days 
    Example:: 9 years, 8 months, 4 days, 16 hours, 2 minutes 
    Example:: 9 yrs 8 min`
    
-   **Link**: Plain Obsidian links like `[[Page]]` or `[[Page|Page Display]]`.
    -   If you reference a link in frontmatter, you need to quote it, as so: `key: "[[Link]]"`. This is default Obsidian-supported behavior.
        
        Example:: [[A Page]] 
        Example:: [[Some Other Page|Render Text]]`
        
-   **List**: Lists of other dataview fields. In YAML, these are defined as normal YAML lists; for inline fields, they are just comma-separated lists.
    
    Example:: 1, 2, 3 
    Example:: "yes", "or", "no"
    
-   **Object**: A map of name to dataview field. These can only be defined in YAML frontmatter, using the normal YAML object syntax:
    field:
       value1: 1
       value2: 2   
       ...`

# Data Querying

Once you've added useful data to relevant pages, you'll want to actually display it somewhere or operate on it. Dataview allows this in four different ways, all of which are written in codeblocks directly in your Markdown and live-reloaded when your vault changes.

## Dataview Query Language (DQL)

The dataview [query language](https://blacksmithgu.github.io/obsidian-dataview/query/queries) is a simplistic, SQL-like language for quickly creating views. It supports basic arithmetic and comparison operations, and is good for basic applications. You create dataview queries using `dataview`-annotated codeblocks:

` ```dataview TABLE rating AS "Rating", summary AS "Summary" FROM #games SORT rating DESC ``` `

```dataview
TABLE file.name AS "File", file.mtime as modified, completion FROM #Tax    
SORT file.mtime DESC
```

The details of how to write a query are explained in the [query language reference](https://blacksmithgu.github.io/obsidian-dataview/query/queries); if you learn better by example, take a look at the [query examples](https://blacksmithgu.github.io/obsidian-dataview/query/examples).

## Inline DQL

The query language also provides inline queries, which allow you to embed single values directly inside a page - for example, todays date via `= date(today)`, or a field from another page via `= [[Page]].value`. You create inline queries using inline codeblocks:

`` `= this.file.name` ``

`= this.file.name`
`= date(today)`
`=[[MOOV x Circle K = Billing issues (CAB)]].file.mtime`

Inline DQL expressions are written using the [query language expression language](https://blacksmithgu.github.io/obsidian-dataview/query/expressions). You can configure inline queries to use a different prefix (like `dv:` or `~`) in the Dataview settings.

## Dataview JS

The dataview [JavaScript API](https://blacksmithgu.github.io/obsidian-dataview/api/intro) gives you the full power of JavaScript and provides a DSL for pulling Dataview data and executing queries, allowing you to create arbitrarily complex queries and views. Similar to the query language, you create Dataview JS blocks via a `dataviewjs`-annotated codeblock:

```-dataviewjs 
let pages = dv.pages("#books and -#books/finished").where(b => b.rating >= 7); 
for (let group of pages.groupBy(b => b.genre)) {
	dv.header(group.key);
	dv.list(group.rows.file.name); } 
```
```dataviewjs 
let pages = dv.pages("#Content and -#Content/Acq"); 
for (let group of pages.groupBy(b => b.Title)) {
	dv.header(group.key);
	dv.list(group.rows.file.name); } 
```

Inside of a JS dataview block, you have access to the full dataview API via the `dv` variable. For an explanation of what you can do with it, see the [API documentation](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference), or the [API examples](https://blacksmithgu.github.io/obsidian-dataview/api/code-examples).

## Inline Dataview JS

Similar to the query language, you can write JS inline queries, which let you embed a computed JS value directly. You create JS inline queries via inline code blocks:

 `$= dv.current().file.mtime` `

In inline DataviewJS, you have access to the `dv` variable, as in `dataviewjs` codeblocks, and can make all of the same calls. The result should be something which evaluates to a JavaScript value, which Dataview will automatically render appropriately.

# Query Language Reference

## Queries
The dataview query language is a simple, structured, custom query language for quickly creating views on your data. It supports:

-   Fetching pages associated with tags, folders, links, and so on.
-   Filtering pages / data by simple operations on fields, like comparison, existence checks, and so on.
-   Sorting results based on fields.

The query language supports the following view types, described below:

1.  **TABLE**: The traditional view type; one row per data point, with several columns of field data.
2.  **LIST**: A list of pages which match the query. You can output a single associated value for each page.
3.  **TASK**: A list of tasks whose pages match the given query.

### General Format

The general format for queries is:

````-dataview 
TABLE|LIST|TASK <field> [AS "Column Name"], <field>, ..., <field> FROM <source> 
WHERE <expression> 
SORT <expression> [ASC/DESC] 
... other data commands 
````

Only the table/list/task statement is required - if the "from" statement is omitted, the query runs for all files in your vault. You can specify data commands like `WHERE` multiple times; they will simply run in the order they are written.

### Query Types
#### List Queries

Lists are the simplest view, and simply render a list of pages (or custom fields) which match the query. To obtain a list of pages matching the query, simply use:

**Syntax**

`LIST FROM <source>`

**Query**

`LIST FROM #games/mobas OR #games/crpg`

**Output**

-   [League of Legends](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#)
-   [Pillars of Eternity 2](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#)

You can render a single computed value in addition to each matching file, by adding an expression after `LIST`:

**Syntax**

`LIST <expression> FROM <source>`

**Query**

`LIST "File Path: " + file.path FROM "4. Archive"`

**Output**

-   [2020-12-18 DN](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#): File path: 4. Archive/Daily Notes/2020-12-18 DN.md
-   [2020-12-16 DN](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#): File path: 4. Archive/Daily Notes/2020-12-16 DN.md
-   [2020-12-17 DN](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#): File path: 4. Archive/Daily Notes/2020-12-17 DN.md
-   [2020-12-15 DN](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#): File path: 4. Archive/Daily Notes/2020-12-15 DN.md

##### LIST WITHOUT ID

If you don't want the file name / group key included in the list view, you can use `LIST WITHOUT ID`:

**Syntax**

`LIST WITHOUT ID <expression> FROM <source>`

**Query**

`LIST WITHOUT ID file.path FROM "4. Archive"`

**Output**

-   1.  Archive/Daily Notes/2020-12-18 DN.md
-   1.  Archive/Daily Notes/2020-12-16 DN.md
-   1.  Archive/Daily Notes/2020-12-17 DN.md
-   1.  Archive/Daily Notes/2020-12-15 DN.md

---

#### Table Queries

Tables support tabular views of page data. You construct a table by giving a comma separated list of the YAML frontmatter fields you want to render, as so:

`TABLE file.day, file.mtime FROM <source>`

You can choose a heading name to render computed fields by using the `AS` syntax:

`TABLE (file.mtime + dur(1 day)) AS next_mtime, ... FROM <source>`

An example table query:

Query
```dataview
TABLE
	time-played AS "Time Played",   
	length AS "Length",
	rating AS "Rating" 
FROM #game 
SORT rating DESC
```

##### TABLE WITHOUT ID

If you don't want the default "File" or "Group" field in your output (either to replace it or because it is unneeded), you can use `TABLE WITHOUT ID`:

Query
```dataview
TABLE WITHOUT ID
	time-played AS "Time Played",
	length AS "Length",
	rating AS "Rating" 
FROM #game 
SORT rating DESC
```
---
### Task Queries

Task views render all tasks whose pages match the given predicate.

Syntax

`TASK FROM <source>`

Query

`TASK FROM "dataview"`

Output

[dataview/Project A](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#)

-   I am a task.
-   I am another task.

[dataview/Project A](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#)

-   I could be a task, though who knows.
    -   Determine if this is a task.
-   I'm a finished task.

You can filter (`WHERE`), group (`GROUP BY`), sort (`SORT`) tasks in these queries as desired using typical dataview statements:

Syntax

`TASK FROM <source> WHERE <predicate> ...`

Query

`TASK FROM "dataview" WHERE !completed GROUP BY file.folder`

Output

Folder 1

-   I am a task.
-   I am another task.
-   I am yet another task in another file in the same folder.

Folder 2

-   I could be a task, though who knows.

Folder 3

-   What even is a task, anyway?

### Calendar Queries

Calendar views render all pages which match the query in a calendar view, using the given date expression to chose which date to render a page on.

Syntax

`CALENDAR <date> FROM <source>`

Query

`CALENDAR file.mtime FROM "dataview"`

```-dataview
CALENDAR file.mtime 
FROM "Journal"
```

Output

The output will be a calendar that displays a dot per file in the dataview directory. The dot will be placed on the date that the file was modified on.

## Data Commands

The different commands that dataview queries can be made up of. Commands are executed in order, and you can have duplicate commands (so multiple `WHERE` blocks or multiple `GROUP BY`blocks, for example).

### FROM

The `FROM` statement determines what pages will initially be collected and passed onto the other commands for further filtering. You can select from any [source](https://blacksmithgu.github.io/obsidian-dataview/query/sources), which currently means by folder, by tag, or by incoming/outgoing links.

-   **Tags**: To select from a tag (and all its subtags), use `FROM #tag`.
-   **Folders**: To select from a folder (and all its subfolders), use `FROM "folder"`.
-   **Single Files**: To select from a single file, use `FROM "path/to/file"`.
-   **Links**: You can either select links TO a file, or all links FROM a file.
-   To obtain all pages which link TO `[[note]]`, use `FROM [[note]]`.
-   To obtain all pages which link FROM `[[note]]` (i.e., all the links in that file), use `FROM outgoing([[note]])`.

You can compose these filters in order to get more advanced sources using `and` and `or`.

-   For example, `#tag and "folder"` will return all pages in `folder` and with `#tag`.
-   `[[Food]] or [[Exercise]]` will give any pages which link to `[[Food]]` OR `[[Exercise]]`.

You can also "negate" sources to obtain anything that does NOT match a source using `-`:

-   `-#tag` will exclude files which have the given tag.
-   `#tag and -"folder"` will only include files tagged `#tag` which are NOT in `"folder"`.

### WHERE

Filter pages on fields. Only pages where the clause evaluates to `true` will be yielded.

`WHERE <clause>`

1.  Obtain all files which were modified in the last 24 hours:
    
    `LIST WHERE file.mtime >= date(today) - dur(1 day)`
    
2.  Find all projects which are not marked complete and are more than a month old:
```dataview
    LIST FROM #projects 
    WHERE !completed AND file.ctime <= date(today) - dur(1 month)`
   
``` 

### SORT

Sorts all results by one or more fields.

`SORT date [ASCENDING/DESCENDING/ASC/DESC]`

You can also give multiple fields to sort by. Sorting will be done based on the first field. Then, if a tie occurs, the second field will be used to sort the tied fields. If there is still a tie, the third sort will resolve it, and so on.

`SORT field1 [ASCENDING/DESCENDING/ASC/DESC], ..., fieldN [ASC/DESC]`

### GROUP BY

Group all results on a field. Yields one row per unique field value, which has 2 properties: one corresponding to the field being grouped on, and a `rows` array field which contains all of the pages that matched.

`GROUP BY field GROUP BY (computed_field) AS name`

In order to make working with the `rows` array easier, Dataview supports field "swizzling". If you want the field `test` from every object in the `rows` array, then `rows.test` will automatically fetch the `test` field from every object in `rows`, yielding a new array. You can then apply aggregation operators like `sum()` over the resulting array.

### FLATTEN

Flatten an array in every row, yielding one result row per entry in the array.
```
FLATTEN field 
FLATTEN (computed_field) AS name
```
For example, flatten the `authors` field in each literature note to give one row per author:

Query
```
TABLE authors FROM #LiteratureNote 
FLATTEN authors
```
Output

![[Pasted image 20220618232637.png]]

### LIMIT

Restrict the results to at most N values.

`LIMIT 5`

Commands are processed in the order they are written, so the following sorts the results _after_they have already been limited:
```
LIMIT 5 
SORT date ASCENDING
```

## Expressions
Dataview query language _expressions_ are anything that yields a value - all fields are expressions, as are literal values (like `6`), as are computed values (like `field - 9`). For a very high level summary:
# Literals
	true/false          (boolean)
	"text"              (text)
	date(2021-04-18)    (date)
	dur(1 day)          (duration)
	[[Link]]            (link)
	[1, 2, 3]           (list)
	{ a: 1, b: 2 }      (object)

# Lambdas
	(x1, x2) => ...     (lambda)

# References
	field               (directly refer to a field)
	simple-field        (refer to fields with spaces/punctuation in them like "Simple Field!")
	a.b                 (if a is an object, retrieve field named 'b')
	a[expr]             (if a is an object or array, retrieve field with name specified by expression 'expr')
	f(a, b, ...)        (call a function called `f` on arguments a, b, ...)

# Arithmetic
	a + b               (addition)
	a - b               (subtraction)
	a * b               (multiplication)
	a / b               (division)
	a % b               (modulo / remainder of division)

# Comparison
	a > b               (check if a is greater than b)
	a < b               (check if a is less than b)
	a = b               (check if a equals b)
	a != b              (check if a does not equal b)
	a <= b              (check if a is less than or equal to b)
	a >= b              (check if a is greater than or equal to b)

# Special Operations

	[[Link]].value      (fetch `value` from page `Link`)

## Expression Types

### Fields as Expressions

The simplest expression is one that just directly refers to a field. If you have a field called "field", then you can refer to it directly by name - `field`. If the field name has spaces, punctuation, or other non-letter/number characters, then you can refer to it using Dataview's simplified name, which is all lower case with spaces replaced with "-". For example, `this is a field` becomes `this-is-a-field`; `Hello!` becomes `hello`, and so on.

### Literals

Constant values - things like `1` or `"hello"` or `date(som)` ("start of month"). There are literals for each data type that dataview supports; you can see the reference above for examples of what each literal type looks like.

### Arithmetic

You can use standard arithmetic operators to combine fields: addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`). For example `field1 + field2` is an expression which computes the sum of the two fields.

### Comparisons

You can compare most values using the various comparison operators: `<`, `>`, `<=`, `>=`, `=`, `!=`. This yields a boolean true or false value which can be used in `WHERE` blocks in queries.

### Array/Object Indexing

You can retrieve data from arrays via the index operator `array[<index>]`, where `<index>` is any computed expression. Arrays are 0-indexed, so the first element is index 0, the second element is index 1, and so on. For example `list(1, 2, 3)[0] = 1`.

You can retrieve data from objects (which map text to data values) also using the index operator, where indexes are now strings/text instead of numbers. You can also use the shorthand `object.<name>`, where `<name>` is the name of the value to retrieve. For example `object("yes", 1).yes = 1`.

### Function Calls

Dataview supports various functions for manipulating data, which are described in full in the [functions documentation](https://blacksmithgu.github.io/obsidian-dataview/query/functions). They have the general syntax `function(arg1, arg2, ...)` - i.e., `lower("yes")` or `regexmatch("text", ".+")`.

### Lambdas

Lambdas are advanced literals which let you define a function that takes some number of inputs, and produces an output. They have the general form:
```
(arg1, arg2, arg3, ...) => <expression using args>
```
Lambdas are used in several advanced operators like `reduce` and `map` to allow for complex transformations of data. A few examples:

	(x, y) => x + y                 (sum x and y)
	(x) => 2 * x                    (double x)
	(value) => length(value) = 4    (return true if value is length 4)

## Type-specific Interactions & Values

Most dataview types have special interactions with operators, or have additional fields that can be retrieved using the index operator.

### Dates

You can retrieve various components of a date via indexing: `date.year`, `date.month`, `date.day`, `date.hour`, `date.minute`, `date.second`, `date.week`, `date.weekyear`. You can also add durations to dates to get new dates.

### Durations

Durations can be added to each other or to dates. You can retrieve various components of a duration via indexing: `duration.years`, `duration.months`, `duration.days`, `duration.hours`, `duration.minutes`, `duration.seconds`.

### Links

You can "index through" a link to get values on the corresponding page. For example `[[Link]].value` would get the value `value` from page `Link`.

Link Indexing in Expressions

If your link is a field that you defined in an inline field or in front-matter, like `Key:: [[Link]]`, then you should index into it by just writing `Key.value`; Using `[[Key]].value` would look up the page literally called `Key`, which is probably not what you want!


## Literals
Dataview query language _literals_ are expressions which represent constant values like `"hello"` or `1337`.

The following is an extensive, but non-exhaustive list of possible literals in DQL.
### General
![[Pasted image 20220618233250.png]]
### Dates

Note that `date()` is also a [function](https://blacksmithgu.github.io/obsidian-dataview/query/functions/#dateany), which can be called on text to extract dates.
![[Pasted image 20220618233321.png|500]]
### Durations
#### Seconds
![[Pasted image 20220618233346.png|300]]
#### Minutes


| Literal          | Description   |
| ---------------- | ------------- |
| `dur(1 m)`       | one minute    |
| `dur(3 m)`       | three minutes |
| `dur(1 min)`     | one minute    |
| `dur(3 mins)`    | three minutes |
| `dur(1 minute)`  | one minute    |
| `dur(3 minutes)` | three minutes | 

#### Hours

| Literal        | Description |
| -------------- | ----------- |
| `dur(1 h)`     | one hour    |
| `dur(3 h)`     | three hours |
| `dur(1 hr)`    | one hour    |
| `dur(3 hrs)`   | three hours |
| `dur(1 hour)`  | one hour    |
| `dur(3 hours)` | three hours | 

#### Days
![[Pasted image 20220618235157.png|300]]

#### Weeks

| Literal        | Description |
| -------------- | ----------- |
| `dur(1 w)`     | one week    |
| `dur(3 w)`     | three weeks |
| `dur(1 wk)`    | one week    |
| `dur(3 wks)`   | three weeks |
| `dur(1 week)`  | one week    |
| `dur(3 weeks)` | three weeks | 

#### Months

| Literal         | Description  |
| --------------- | ------------ |
| `dur(1 mo)`     | one month    |
| `dur(3 mo)`     | three month  |
| `dur(1 month)`  | one month    |
| `dur(3 months)` | three months |

#### Years

| Literal        | Description |
| -------------- | ----------- |
| `dur(1 yr)`    | one year    |
| `dur(3 yrs)`   | three years |
| `dur(1 year)`  | one year    |
| `dur(3 years)` | three years |

#### Combinations

| Literal                | Description                              |
| ---------------------- | ---------------------------------------- |
| `dur(1 s, 2 m, 3 h)`   | three hours, two minutes, and one second |
| `dur(1 s 2 m 3 h)`     | three hours, two minutes, and one second |
| `dur(1s 2m 3h)`        | three hours, two minutes, and one second |
| `dur(1second 2min 3h)` | three hours, two minutes, and one second |
|                        |                                          |

## Sources
A dataview "source" is something that identifies a set of files, tasks, or other data object. Sources are indexed internally by Dataview, so they are fast to query. Dataview currently supports four source types:

1.  **Tags**: Sources of the form `#tag`. These match all files / sections / tasks with the given tag.
2.  **Folders**: Sources of the form `"folder"`. These match all files / sections / tasks contained in the given folder.
3.  **Specific Files**: You can select from a specific file by specifying it's full path: `"folder/File"`.
    -   If you have both a file and a folder with the exact same path, Dataview will prefer the folder. You can force it to read from the file by specifying an extension: `folder/File.md`.
4.  **Links**: You can either select links **to** a file, or all links **from** a file.
    -   To obtain all pages which link **to** `[[note]]`, use `[[note]]`.
    -   To obtain all pages which link **from** `[[note]]` (i.e., all the links in that file), use `outgoing([[note]])`.
    -   You can implicitly reference the current file via `[[#]]` or `[[]]`.

You can compose these filters in order to get more advanced sources using `and` and `or`.

-   For example, `#tag and "folder"` will return all pages in `folder` and with `#tag`.
-   Querying from `#food and !#fastfood` will only return pages that contain `#food` but does not contain `#fastfood`.
-   `[[Food]] or [[Exercise]]` will give any pages which link to `[[Food]]` OR `[[Exercise]]`.

Sources are used in both the [FROM query statement](https://blacksmithgu.github.io/obsidian-dataview/query/queries#from), as well as various JavaScript API query calls.


## Functions
Dataview functions provide more advanced ways to manipulate data.

### Function Vectorization

Most functions can be applied either to single values (like `number`, `string`, `date`, etc.) OR to lists of those values. If a function is applied to a list, it also returns a list after the function is applied to each element in the list. For example:

`lower("YES") = "yes" lower(["YES", "NO"]) = ["yes", "no"]  replace("yes", "e", "a") = "yas" replace(["yes", "ree"], "e", "a") = ["yas", "raa"]`

### Constructors
Constructors which create values.

### `object(key1, value1, ...)`

Creates a new object with the given keys and values. Keys and values should alternate in the call, and keys should always be strings/text.

`object() => empty object object("a", 6) => object which maps "a" to 6 object("a", 4, "c", "yes") => object which maps a to 4, and c to "yes"`

### `list(value1, value2, ...)`

Creates a new list with the given values in it.

`list() => empty list list(1, 2, 3) => list with 1, 2, and 3 list("a", "b", "c") => list with "a", "b", and "c"`

### `date(any)`

Parses a date from the provided string, date, or link object, if possible, returning null otherwise.

`date("2020-04-18") = <date object representing April 18th, 2020> date([[2021-04-16]]) = <date object for the given page, refering to file.day>`

### `dur(any)`

Parses a duration from the provided string or duration, returning null on failure.

`dur(8 minutes) = <8 minutes> dur("8 minutes, 4 seconds") = <8 minutes, 4 seconds> dur(dur(8 minutes)) = dur(8 minutes) = <8 minutes>`

### `number(string)`

Pulls the first number out of the given string, returning it if possible. Returns null if there are no numbers in the string.

`number("18 years") = 18 number(34) = 34 number("hmm") = null`

### `string(any)`

Converts any value into a "reasonable" string representation. This sometimes produces less pretty results than just directly using the value in a query - it is mostly useful for coercing dates, durations, numbers, and so on into strings for manipulation.

`string(18) = "18" string(dur(8 hours)) = "8 hours" string(date(2021-08-15)) = "August 15th, 2021"`

### `link(path, [display])`

Construct a link object from the given file path or name. If provided with two arguments, the second argument is the display name for the link.

`link("Hello") => link to page named 'Hello' link("Hello", "Goodbye") => link to page named 'Hello', displays as 'Goodbye'`

### `embed(link, [embed?])`

Convert a link object into an embedded link; support for embedded links is somewhat spotty in Dataview views, though embedding of images should work.

`embed(link("Hello.png")) => embedded link to the "Hello.png" image, which will render as an actual image.`

### `elink(url, [display])`

Construct a link to an external url (like `www.google.com`). If provided with two arguments, the second argument is the display name for the link.

`elink("www.google.com") => link element to google.com elink("www.google.com", "Google") => link element to google.com, displays as "Google"`

### `typeof(any)`

Get the type of any object for inspection. Can be used in conjunction with other operators to change behavior based on type.

`typeof(8) => "number" typeof("text") => "string" typeof([1, 2, 3]) => "array" typeof({ a: 1, b: 2 }) => "object" typeof(date(2020-01-01)) => "date" typeof(dur(8 minutes)) => "duration"`

---

### Numeric Operations

### `round(number, [digits])`

Round a number to a given number of digits. If the second argument is not specified, rounds to the nearest whole number; otherwise, rounds to the given number of digits.

`round(16.555555) = 7 round(16.555555, 2) = 16.56`

--

### Objects, Arrays, and String Operations

Operations that manipulate values inside of container objects.

### `contains(object|list|string, value)`

Checks if the given container type has the given value in it. This function behave slightly differently based on whether the first argument is an object, a list, or a string.

-   For objects, checks if the object has a key with the given name. For example,
    
    `contains(file, "ctime") = true contains(file, "day") = true (if file has a date in its title, false otherwise)`
    
-   For lists, checks if any of the array elements equals the given value. For example,
    
    `contains(list(1, 2, 3), 3) = true contains(list(), 1) = false`
    
-   For strings, checks if the given value is a substring (i.e., inside) the string.
    
    `contains("hello", "lo") = true contains("yes", "no") = false`
    

### `extract(object, key1, key2, ...)`

Pulls multiple fields out of an object, creating a new object with just those fields.

`extract(file, "ctime", "mtime") = object("ctime", file.ctime, "mtime", file.mtime) extract(object("test", 1)) = object()`

### `sort(list)`

Sorts a list, returning a new list in sorted order.

`sort(list(3, 2, 1)) = list(1, 2, 3) sort(list("a", "b", "aa")) = list("a", "aa", "b")`

### `reverse(list)`

Reverses a list, returning a new list in reversed order.

`reverse(list(1, 2, 3)) = list(3, 2, 1) reverse(list("a", "b", "c")) = list("c", "b", "a")`

### `length(object|array)`

Returns the number of fields in an object, or the number of entries in an array.

`length(list()) = 0 length(list(1, 2, 3)) = 3 length(object("hello", 1, "goodbye", 2)) = 2`

### `sum(array)`

Sums all numeric values in the array

`sum(list(1, 2, 3)) = 6`

### `all(array)`

Returns `true` only if ALL values in the array are truthy. You can also pass multiple arguments to this function, in which case it returns `true` only if all arguments are truthy.

`all(list(1, 2, 3)) = true all(list(true, false)) = false all(true, false) = false all(true, true, true) = true`

### `any(array)`

Returns `true` if ANY of the values in the array are truthy. You can also pass multiple arguments to this function, in which case it returns `true` if any of the arguments are truthy.

`any(list(1, 2, 3)) = true any(list(true, false)) = true any(list(false, false, false)) = false all(true, false) = true all(false, false) = false`

### `none(array)`

Returns `true` if NONE of the values in the array are truthy.

`none([]) = true none([false, false]) = true none([false, true]) = false none([1, 2, 3]) = false`

### `join(array)`

Joins elements in an array into a single string (i.e., rendering them all on the same line). If provided with a second argument, then each element will be separated by the given separator.

`join(list(1, 2, 3)) = "1, 2, 3" join(list(1, 2, 3), " ") = "1 2 3" join(6) = "6" join(list()) = ""`

### `filter(array, predicate)`

Filters elements in an array according to the predicate, returning a new list of the elements which matched.

`filter([1, 2, 3], (x) => x >= 2) = [2, 3] filter(["yes", "no", "yas"], (x) => startswith(x, "y")) = ["yes", "yas"]`

### `map(array, func)`

Applies the function to each element in the array, returning a list of the mapped results.

`map([1, 2, 3], (x) => x + 2) = [3, 4, 5] map(["yes", "no"], (x) => x + "?") = ["yes?", "no?"]`

---

### String Operations

### `regexmatch(pattern, string)`

Checks if the given string matches the given pattern (using the JavaScript regex engine).

`regexmatch("\w+", "hello") = true regexmatch(".", "a") = true regexmatch("yes|no", "maybe") = false`

### `regexreplace(string, pattern, replacement)`

Replaces all instances where the _regex_ `pattern` matches in `string`, with `replacement`. This uses the JavaScript replace method under the hood, so you can use special characters like `$1`to refer to the first capture group, and so on.

`regexreplace("yes", "[ys]", "a") = "aea" regexreplace("Suite 1000", "\d+", "-") = "Suite -"`

### `replace(string, pattern, replacement)`

Replace all instances of `pattern` in `string` with `replacement`.

`replace("what", "wh", "h") = "hat" replace("The big dog chased the big cat.", "big", "small") = "The small dog chased the small cat." replace("test", "test", "no") = "no"`

### `lower(string)`

Convert a string to all lower case.

`lower("Test") = "test" lower("TEST") = "test"`

### `upper(string)`

Convert a string to all upper case.

`upper("Test") = "TEST" upper("test") = "TEST"`

### `split(string, delimiter, [limit])`

Split a string on the given delimiter string. If a third argument is provided, it limits the number of splits that occur. The delimiter string is interpreted as a regular expression. If there are capture groups in the delimiter, matches are spliced into the result array, and non-matching captures are empty strings.

`split("hello world", " ") = list("hello", "world") split("hello  world", "\s") = list("hello", "world") split("hello there world", " ", 2) = list("hello", "there") split("hello there world", "(t?here)") = list("hello ", "there", " world") split("hello there world", "( )(x)?") = list("hello", " ", "", "there", " ", "", "world")`

### `startswith(string, prefix)`

Checks if a string starts with the given prefix.

`startswith("yes", "ye") = true startswith("path/to/something", "path/") = true startswith("yes", "no") = false`

### `endswith(string, suffix)`

Checks if a string ends with the given suffix.

`endswith("yes", "es") = true endswith("path/to/something", "something") = true endswith("yes", "ye") = false`

### `padleft(string, length, [padding])`

Pads a string up to the desired length by adding padding on the left side. If you omit the padding character, spaces will be used by default.

`padleft("hello", 7) = "  hello" padleft("yes", 5, "!") = "!!yes"`

### `padright(string, length, [padding])`

Equivalent to `padleft`, but pads to the right instead.

`padright("hello", 7) = "hello  " padright("yes", 5, "!") = "yes!!"`

### Utility Functions

### `default(field, value)`

If `field` is null, return `value`; otherwise return `field`. Useful for replacing null values with defaults. For example, to show projects which haven't been completed yet, use `"incomplete"`as their defualt value:

`default(dateCompleted, "incomplete")`

Default is vectorized in both arguments; if you need to use default explicitly on a list argument, use `ldefault`, which is the same as default but is not vectorized.

`default(list(1, 2, null), 3) = list(1, 2, 3) ldefault(list(1, 2, null), 3) = list(1, 2, null)`

### `choice(bool, left, right)`

A primitive if statement - if the first argument is truthy, returns left; otherwise, returns right.

`choice(true, "yes", "no") = "yes" choice(false, "yes", "no") = "no" choice(x > 4, y, z) = y if x > 4, else z`

### `striptime(date)`

Strip the time component of a date, leaving only the year, month, and day. Good for date comparisons if you don't care about the time.

`striptime(file.ctime) = file.cday striptime(file.mtime) = file.mday`

### `localtime(date)`

Converts a date in a fixed timezone to a date in the current timezone.

### `meta(link)`

Get an object containing metadata of a link. When you access a property on a link what you get back is the property value from the linked file. The `meta` function makes it possible to access properties of the link itself.

There are several properties on the object returned by `meta`:

#### `meta(link).display`

Get the display text of a link, or null if the link does not have defined display text.

`meta([[2021-11-01|Displayed link text]]).display = "Displayed link text" meta([[2021-11-01]]).display = null`

#### `meta(link).embed`

True or false depending on whether the link is an embed. Those are links that begin with an exclamation mark, like `![[Some Link]]`.

#### `meta(link).path`

Get the path portion of a link.

`meta([[My Project]]).path = "My Project" meta([[My Project#Next Actions]]).path = "My Project" meta([[My Project#^9bcbe8]]).path = "My Project"`

#### `meta(link).subpath`

Get the subpath of a link. For links to a heading within a file the subpath will be the text of the heading. For links to a block the subpath will be the block ID. If neither of those cases applies then the subpath will be null.

`meta([[My Project#Next Actions]]).subpath = "Next Actions" meta([[My Project#^9bcbe8]]).subpath = "9bcbe8" meta([[My Project]]).subpath = null`

This can be used to select tasks under specific headings.

` ```dataview task where meta(section).subpath = "Next Actions" ``` `

#### `meta(link).type`

Has the value "file", "header", or "block" depending on whether the link links to an entire file, a heading within a file, or to a block within a file.

`meta([[My Project]]).type = "file" meta([[My Project#Next Actions]]).type = "header" meta([[My Project#^9bcbe8]]).type = "block"`


## Examples

## Frequently Asked Questions

A collection of frequently asked questions for Dataview queries and the expression language.

### How do I use fields with the same name as keywords (like "from", "where")?

Dataview provides a special "fake" field called `row` which can be indexed into to obtain fields which conflict with Dataview keywords:

`row.from /* Same as "from" */ row.where /* Same as "where" */`

### How do I access fields with spaces in the name?

There are two ways:

1.  Use the normalized Dataview name for such a field - just convert the name to lowercase and replace whitespace with dashes ("-"). Something like `Field With Space In It`becomes `field-with-space-in-it`.
2.  Use the implicit `row` field:
    
    `row["Field With Space In It"]`


# JavaScript Reference
## Overview

The Dataview JavaScript API allows for executing arbitrary JavaScript with access to the dataview indices and query engine, which is good for complex views or interop with other plugins. The API comes in two flavors: plugin facing, and user facing (or 'inline API usage').

### Inline Access

You can create a "DataviewJS" block via:

` ```dataviewjs dv.pages("#thing")... ``` `

Code executed in such codeblocks have access to the `dv` variable, which provides the entirety of the codeblock-relevant dataview API (like `dv.table()`, `dv.pages()`, and so on). For more information, check out the [codeblock API reference](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference/).

### Plugin Access

You can access the Dataview Plugin API (from other plugins or the console) through `app.plugins.plugins.dataview.api`; this API is similar to the codeblock reference, with slightly different arguments due to the lack of an implicit file to execute the queries in. For more information, check out the [Plugin API reference](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference/).

## Data Arrays

The general abstraction for lists of results in Dataview is the `DataArray`, which is a proxied array with additional functionality. Data arrays support indexing and iteration (via `for` and `for ... of` loops) as per normal arrays, but also include many data manipulation operators like `sort`, `groupBy`, `distinct`, `where`, and so on to make mainpulating tabular data easy.

### Creation

Data arrays are returned by most Dataview APIs that can return multiple results, such as `dv.pages()`. You can also explicitly convert a normal JavaScript array into a Dataview array using `dv.array(<array>)`. If you want to convert a Data array back to a normal array, use `DataArray#array()`.

### Indexing and Swizzling

Data arrays support regular indexing just like normal arrays (like `array[0]`), but importantly, they also support query-language-style "swizzling": if you index into a data array with a field name (like `array.field`), it automatically maps every element in the array to `field`, flattening `field` if it itself is also an array.

For example, `dv.pages().file.name` will return a data array of all file names in your vault;`dv.pages("#books").genres` will return a flattened list of all genres in your books.

### Raw Interface
```
The full interface for the data array implementation is provided below for reference:
/** A function which maps an array element to some value. */
export type ArrayFunc<T, O> = (elem: T, index: number, arr: T[]) => O;

/** A function which compares two types. */
export type ArrayComparator<T> = (a: T, b: T) => number;

/**
 * Proxied interface which allows manipulating array-based data. All functions on a data array produce a NEW array
 * (i.e., the arrays are immutable).
 */
export interface DataArray<T> {
    /** The total number of elements in the array. */
    length: number;

    /** Filter the data array down to just elements which match the given predicate. */
    where(predicate: ArrayFunc<T, boolean>): DataArray<T>;
    /** Alias for 'where' for people who want array semantics. */
    filter(predicate: ArrayFunc<T, boolean>): DataArray<T>;

    /** Map elements in the data array by applying a function to each. */
    map<U>(f: ArrayFunc<T, U>): DataArray<U>;
    /** Map elements in the data array by applying a function to each, then flatten the results to produce a new array. */
    flatMap<U>(f: ArrayFunc<T, U[]>): DataArray<U>;
    /** Mutably change each value in the array, returning the same array which you can further chain off of. */
    mutate(f: ArrayFunc<T, any>): DataArray<any>;

    /** Limit the total number of entries in the array to the given value. */
    limit(count: number): DataArray<T>;
    /**
     * Take a slice of the array. If `start` is undefined, it is assumed to be 0; if `end` is undefined, it is assumbed
     * to be the end of the array.
     */
    slice(start?: number, end?: number): DataArray<T>;
    /** Concatenate the values in this data array with those of another iterable / data array / array. */
    concat(other: Iterable<T>): DataArray<T>;

    /** Return the first index of the given (optionally starting the search) */
    indexOf(element: T, fromIndex?: number): number;
    /** Return the first element that satisfies the given predicate. */
    find(pred: ArrayFunc<T, boolean>): T | undefined;
    /** Find the index of the first element that satisfies the given predicate. Returns -1 if nothing was found. */
    findIndex(pred: ArrayFunc<T, boolean>, fromIndex?: number): number;
    /** Returns true if the array contains the given element, and false otherwise. */
    includes(element: T): boolean;

    /**
     * Return a string obtained by converting each element in the array to a string, and joining it with the
     * given separator (which defaults to ', ').
     */
    join(sep?: string): string;

    /**
     * Return a sorted array sorted by the given key; an optional comparator can be provided, which will
     * be used to compare the keys in leiu of the default dataview comparator.
     */
    sort<U>(key: ArrayFunc<T, U>, direction?: "asc" | "desc", comparator?: ArrayComparator<U>): DataArray<T>;

    /**
     * Return an array where elements are grouped by the given key; the resulting array will have objects of the form
     * { key: <key value>, rows: DataArray }.
     */
    groupBy<U>(key: ArrayFunc<T, U>, comparator?: ArrayComparator<U>): DataArray<{ key: U; rows: DataArray<T> }>;

    /**
     * Return distinct entries. If a key is provided, then rows with distinct keys are returned.
     */
    distinct<U>(key?: ArrayFunc<T, U>, comparator?: ArrayComparator<U>): DataArray<T>;

    /** Return true if the predicate is true for all values. */
    every(f: ArrayFunc<T, boolean>): boolean;
    /** Return true if the predicate is true for at least one value. */
    some(f: ArrayFunc<T, boolean>): boolean;
    /** Return true if the predicate is FALSE for all values. */
    none(f: ArrayFunc<T, boolean>): boolean;

    /** Return the first element in the data array. Returns undefined if the array is empty. */
    first(): T;
    /** Return the last element in the data array. Returns undefined if the array is empty. */
    last(): T;

    /** Map every element in this data array to the given key, and then flatten it.*/
    to(key: string): DataArray<any>;
    /**
     * Recursively expand the given key, flattening a tree structure based on the key into a flat array. Useful for handling
     * heirarchical data like tasks with 'subtasks'.
     */
    expand(key: string): DataArray<any>;

    /** Run a lambda on each element in the array. */
    forEach(f: ArrayFunc<T, void>): void;

    /** Convert this to a plain javascript array. */
    array(): T[];

    /** Allow iterating directly over the array. */
    [Symbol.iterator](): Iterator<T>;

    /** Map indexes to values. */
    [index: number]: any;
    /** Automatic flattening of fields. Equivalent to implicitly calling `array.to("field")` */
    [field: string]: any;
}
```

# Plugin Developers





#dataview 

### Dataview JS
```dataviewjs
let pages = dv.pages("#task and -#task/finished").where(b => b.file.mtime >= "2022-05-20");
for (let group of pages.groupBy(b => b.file.name)) {
   dv.header(group.key);
   dv.list(group.rows.file.name);
}
```

### Inline Dataview JS
`$= dv.current().file.mtime`

```dataviewjs
for (let group of dv.pages("#book").groupBy(p => p.genre)) {
    dv.header(3, group.key);
    dv.table(["Name", "Time Read", "Rating"],
        group.rows
            .sort(k => k.rating, 'desc')
            .map(k => [k.file.link, k["time-read"], k.rating]))
}
```

Find all Direct and Indirectly Linked Pages
```dataviewjs
let page = dv.current().file.path;
let pages = new Set();

let stack = [page];
while (stack.length > 0) {
    let elem = stack.pop();
    let meta = dv.page(elem);
    if (!meta) continue;

    for (let inlink of meta.file.inlinks.concat(meta.file.outlinks).array()) {
        console.log(inlink);
        if (pages.has(inlink.path)) continue;
        pages.add(inlink.path);
        stack.push(inlink.path);
    }
}

// Data is now the file metadata for every page that directly OR indirectly links to the current page.
let data = dv.array(Array.from(pages)).map(p => dv.page(p));
```