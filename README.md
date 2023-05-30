# CTkTable

Here is a quick and simple table widget having all the basic features. 

![Screenshot](https://user-images.githubusercontent.com/89206401/233420929-bf210cb3-5b5f-49b2-ba7a-f01d187e72cf.jpg)

## Features:
- Add columns/rows
- Delete columns/rows
- Edit rows/columns at once
- Insert values to specific cell
- delete values from specific cell
- update all values at once
- edit each cell value and options
- lightweight library
- can be used with scrollable frame

## Installation
### [<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Akascape/CTkTable?&color=white&label=Download%20Source%20Code&logo=Python&logoColor=yellow&style=for-the-badge"  width="400">](https://github.com/Akascape/CTkTable/archive/refs/heads/main.zip)

**Download the source code, paste the `CTkTable` folder in the directory where your program is present.**

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
- **.edit_row(row_num, other_options)**: edit one full row at once
- **.edit_column(column_num, other_options)**: edit one full column at once
- **.delete_row(index)**
- **.delete_column(index)**
- **.update_values(values)**: update all values at once
- **.insert(row, column, value, other_options)**: change specific index data
- **.delete(row, column, other_options)**: delete the data from specific index
- **.get()**: get all values
- **.get_value(row, column)**: get specific value
- **.configure(arguments)**: change other table attributes

_here, **other_options** means ctkbutton parameters_

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
| color_phase | set color phase based on rows or columns, eg: `color_phase="column"` |
| header_color | define the topmost row color |
| corner_radius | define the corner roundness of the table |
| hover | enable hover effect on the cells |
| **command** | specify a command when a table cell is pressed, [returns row, column, value] |
| **other button parameters* | all other ctk button parameters can be passed |

### Thanks for visiting! Hope it will help :)
