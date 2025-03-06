# CTkTable

**A simple and feature-rich table widget for CustomTkinter.**

![Screenshot](https://user-images.githubusercontent.com/89206401/233420929-bf210cb3-5b5f-49b2-ba7a-f01d187e72cf.jpg)

## Features:
- Add and delete columns/rows
- Edit rows/columns at once
- Insert or remove values from specific cells
- Update all values dynamically
- Entry editing support
- Scrollable frame support
- Color customization and styling options

## Installation
```sh
git clone https://github.com/Akascape/CTkTable.git
```
Then, manually move the cloned folder to your script directory.

### [<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Akascape/CTkTable?&color=white&label=Download%20Source%20Code&logo=Python&logoColor=yellow&style=for-the-badge" width="400">](https://github.com/Akascape/CTkTable/archive/refs/heads/main.zip)

_Don't forget to leave a ⭐_

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
- **.insert(row, column, value, *args)**: Change specific cell data
- **.add_row(index, values)**: Add a new row at the specified index
- **.add_column(index, values)**: Add a new column at the specified index
- **.edit_row(row_num, *args)**: Edit an entire row at once
- **.edit_column(column_num, *args)**: Edit an entire column at once
- **.delete_row(index)**: Remove one row
- **.delete_column(index)**: Remove one column
- **.delete_rows(indices)**: Remove multiple rows
- **.delete_columns(indices)**: Remove multiple columns
- **.edit(row, column)**: Edit a specific cell without changing its value
- **.select(row, column)**: Select a cell
- **.select_row(row)**: Select a row
- **.get_selected_row()**: Get values of the selected row
- **.deselect_row(row)**: Deselect a row
- **.select_column(column)**: Select a column
- **.get_selected_column()**: Get values of the selected column
- **.deselect_column(column)**: Deselect a column
- **.update_values(values)**: Update all values at once
- **.delete(row, column, *args)**: Delete data from a specific index
- **.get()**: Get all table values
- **.get(row, column)**: Get value from a specific cell
- **.get_row(row)**: Get all values from a specific row
- **.get_column(column)**: Get all values from a specific column
- **.configure(arguments)**: Change table attributes dynamically

## Arguments
| Parameter | Description |
|-----------| ------------|
| **master** | Parent widget |
| **values** | Default values for the table |
| row | **Optional**, set the number of default rows |
| column | **Optional**, set the number of default columns |
| padx | Internal padding in x |
| pady | Internal padding in y |
| colors | Set foreground colors for the table (list), e.g., `colors=["yellow", "green"]` |
| color_phase | Set color phase based on rows or columns, e.g., `color_phase="vertical"` |
| orientation | Change table orientation (`vertical` or `horizontal`) |
| header_color | Define the topmost row color |
| corner_radius | Define the corner roundness of the table |
| hover_color | Enable hover effect on the cells |
| wraplength | Set the width of cell text |
| justify | Align text in table cells |
| **command** | Specify a function to be called when a cell is clicked ([returns row, column, value]) |
| **other button parameters** | All other `ctkbutton` parameters can be passed |

**Note:** This library is in its early stages, so there may be some performance issues.

### Additional Features
- `TableGenerator`: A powerful image-based table generator for rendering tables in PIL (**Recommended: Faster and more efficient**)
- `CTkTableMini`: A lightweight version for smaller applications


---
### Contributions by [MustafaHilmiYAVUZHAN](https://github.com/MustafaHilmiYAVUZHAN)

### Thanks for visiting! Hope it helps! 🚀

