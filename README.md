# CTkTable

**Here is a quick and simple table widget having all the basic features.**

![Screenshot](https://user-images.githubusercontent.com/89206401/233420929-bf210cb3-5b5f-49b2-ba7a-f01d187e72cf.jpg)

## Features:
- Add columns/rows
- Delete columns/rows
- Edit rows/columns at once
- Insert values to specific cell
- delete values from specific cell
- update all values at once
- edit each cell value and options
- entry editing
- can be used with scrollable frame

## Installation
```
pip install CTkTable
```

### [<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Akascape/CTkTable?&color=white&label=Download%20Source%20Code&logo=Python&logoColor=yellow&style=for-the-badge"  width="400">](https://github.com/Akascape/CTkTable/archive/refs/heads/main.zip)

_Dont forget to leave a ⭐_

## Usage
```python
import customtkinter
from CTkTable import *

root = customtkinter.CTk()

value = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]

table = CTkTable(master=root, row=5, column=5, values=value)
table.pack(expand=True, fill="both", padx=20, pady=20)

root.mainloop()
```

## Methods
- **.add_row(index, values)**
- **.add_column(index, values)**
- **.edit_row(row_num, *args)**: edit one full row at once
- **.edit_column(column_num, *args)**: edit one full column at once
- **.delete_row(index)**: remove one row
- **.delete_column(index)**: remove one column
- **.delete_rows(indices)**: remove mutliple rows
- **.delete_columns(indices)**: remove multiple columns
- **.select(row, column)**: select one cell
- **.select_row(row)**: select a row
- **.deselect_row(row)**: deselect a row
- **.select_column(column)**: select a column
- **.deselect_column(column)**: deselect a column
- **.update_values(values)**: update all values at once
- **.insert(row, column, value, *args)**: change specific index data
- **.delete(row, column, *args)**: delete the data from specific index
- **.get()**: get all values
- **.get(row, column)**: get specific cell value
- **.get_row(row)**: get all values of a specific row
- **.get_column(column)**: get all values of a specific column
- **.configure(arguments)**: change other table attributes

_here, **args** means ctkbutton parameters which can also be passed_

**Note: treat all the table cells as a ctkbutton class**

## Arguments
| Parameter | Description |
|-----------| ------------|
| **master** | parent widget  |
| **values** | the default values for table |
| row | **optional**, set number of default rows |
| column | **optional**, set number of default columns |
| padx | add internal padding in x |
| pady | add internal padding in y |
| colors | set two fg_colors for the table (list), eg: `colors=["yellow", "green"]` |
| color_phase | set color phase based on rows or columns, eg: `color_phase="vertical"` |
| orientation | change the orientation of table, `vertical or horizontal` |
| header_color | define the topmost row color |
| corner_radius | define the corner roundness of the table |
| hover_color | enable hover effect on the cells |
| wraplength | set the width of cell text |
| **command** | specify a command when a table cell is pressed, [returns row, column, value] |
| **other button parameters* | all other ctk button parameters can be passed |

Note: This library is at early stage so there can be some performance issues. 
### Thanks for visiting! Hope it will help :)
