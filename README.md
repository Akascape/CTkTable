# CTkTable

Here is a quick and simple table widget having all the basic features. 

![Screenshot](https://user-images.githubusercontent.com/89206401/233420929-bf210cb3-5b5f-49b2-ba7a-f01d187e72cf.jpg)

## Features:
- Add columns/rows
- Delete columns/rows
- Edit rows/columns at once
- Insert values to specific block
- delete values from specific block
- update all values at once
- customize each block and fg-colors
- lightweight widget class

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
- **.edit_row(row_num, other_options)**: edit one row at once
- **.edit_column(column_num, other_options)**: edit one column at once
- **.delete_row(index)**
- **.delete_column(index)**
- **.update_values(values)**: update all values at once
- **.insert(row, column, value, other_options)**: change specific index data
- **.delete(row, column, other_options)**: delete the data from specific index
- **.get()**: get all values
- **.get_value(row, column)**: get specific value
- **.configure(...)**: change other table attributes

_here, **other_options** means ctkbutton parameters_

## Arguments
| Parameter | Description |
|-----------| ------------|
| **master** | parent widget  |
| **values** | the default values for table |
| row | **optional**, set number of default rows |
| column | **optional**, set number of default columns |
| padx | set padding in x between the blocks |
| pady | set padding in y between the blocks |
| colors | set two fg_colors for the table (list) |
| color_phase | set color phase based on rows or columns |
| header_color | define the topmost row color |
| corner_radius | define the corner roundness of the table |
| **other button parameters* | all other ctk button parameters can be passed |
