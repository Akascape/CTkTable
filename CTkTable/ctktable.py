# CTkTable Widget by Akascape
# License: MIT
# Author: Akash Bora

import customtkinter

class CTkTable(customtkinter.CTkFrame):
    """ CTkTable Widget """
    
    def __init__(
        self,
        master: any = None,
        row: int = None,
        column: int = None,
        padx: int = 1, 
        pady: int = 0,
        values: list = [[None]],
        colors: list = [None, None],
        color_phase: str = "rows",
        header_color: str = None,
        corner_radius: int = 25,
        hover: bool = False,
        command = None,
        **kwargs):
        
        super().__init__(master, fg_color="transparent")

        self.master = master # parent widget
        self.rows = row if row else len(values) # number of default rows
        self.columns = column if column else len(values[0])# number of default columns
        self.padx = padx # internal padding between the rows/columns
        self.pady = pady
        self.command = command
        self.values = values # the default values of the table
        self.colors = colors # colors of the table if required
        self.header_color = header_color # specify the topmost row color
        self.phase = color_phase
        self.corner = corner_radius
        self.hover = hover
        # if colors are None then use the default frame colors:
        self.fg_color = customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"] if not self.colors[0] else self.colors[0]
        self.fg_color2 = customtkinter.ThemeManager.theme["CTkFrame"]["top_fg_color"] if not self.colors[1] else self.colors[1]
        
        self.frame = {}
        self.draw_table(**kwargs)
        
    def draw_table(self, **kwargs):
        """ draw the table """
        for i in range(self.rows):
            for j in range(self.columns):
                if self.phase=="rows":
                    if i%2==0:
                        fg = self.fg_color
                    else:
                        fg = self.fg_color2
                else:
                    if j%2==0:
                        fg = self.fg_color
                    else:
                        fg = self.fg_color2
                        
                if self.header_color:
                    if i==0:
                        fg = self.header_color
                        
                corner_radius = self.corner    
                if i==0 and j==0:
                    corners = ["", fg, fg, fg]
                elif i==self.rows-1 and j==self.columns-1:
                    corners = [fg ,fg, "", fg]
                elif i==self.rows-1 and j==0:
                    corners = [fg ,fg, fg, ""]
                elif i==0 and j==self.columns-1:
                    corners = [fg , "", fg, fg]
                else:
                    corners = [fg, fg, fg, fg]
                    corner_radius = 0
                    
                if self.values:
                    try:
                        value = self.values[i][j]
                    except IndexError: value = " "
                else:
                    value = " "
                    
                self.data = {"row": i, "column" : j, "value" : value}
                self.frame[i,j] = customtkinter.CTkButton(self, background_corner_colors=corners,
                                                          corner_radius=corner_radius,
                                                          fg_color=fg, hover=self.hover, text=value,
                                                          command=(lambda e=self.data: self.command(e)) if self.command else None, **kwargs)
                self.frame[i,j].grid(column=j, row=i, padx=self.padx, pady=self.pady, sticky="nsew")
                
                self.rowconfigure(i, weight=1)
                self.columnconfigure(j, weight=1)
    
    def edit_row(self, row, **kwargs):
        """ edit all parameters of a single row """
        for i in range(self.columns):
            self.frame[row, i].configure(**kwargs)
        
    def edit_column(self, column, **kwargs):
        """ edit all parameters of a single column """
        for i in range(self.rows):
            self.frame[i, column].configure(**kwargs)
            
    def update_values(self, values, **kwargs):
        """ update all values at once """
        for i in self.frame.values():
            i.destroy()
        self.frame = {}
        self.values = values
        self.draw_table(**kwargs)
        
    def add_row(self, values, index=None):
        """ add a new row """
        for i in self.frame.values():
            i.destroy()
        self.frame = {}
        if index is None:
            index = len(self.values)      
        self.values.insert(index, values)
        self.rows+=1
        self.draw_table()
        
    def add_column(self, values, index=None):
        """ add a new column """
        for i in self.frame.values():
            i.destroy()
        self.frame = {}
        if index is None:
            index = len(self.values[0])
        x = 0
        for i in self.values:
            i.insert(index, values[x])
            x+=1
        self.columns+=1
        self.draw_table()
    
    def delete_row(self, index=None):
        """ delete a particular row """
        if index is None or index>len(self.values):
            index = len(self.values)-1
        self.values.pop(index)
        for i in self.frame.values():
            i.destroy()
        self.rows-=1
        self.frame = {}
        self.draw_table()
        
    def delete_column(self, index=None):
        """ delete a particular column """
        if index is None or index>len(self.values[0]):
            index = len(self.values)-1
        for i in self.values:
            i.pop(index)
        for i in self.frame.values():
            i.destroy()
        self.columns-=1
        self.frame = {}
        self.draw_table()
    
    def insert(self, row, column, value, **kwargs):
        """ insert value in a specific block [row, column] """
        self.frame[row,column].configure(text=value, **kwargs)
    
    def delete(self, row, column, **kwargs):
        """ delete a value from a specific block [row, column] """
        self.frame[row,column].configure(text="", **kwargs)

    def get(self):
        return self.values
    
    def get_value(self, row, column):
        return self.frame[row,column].cget("text")
    
    def configure(self, **kwargs):
        """ configure table widget attributes"""
        
        if "colors" in kwargs:
            self.colors = kwargs.pop("colors")
            self.fg_color = self.colors[0]
            self.fg_color2 = self.colors[1]
        if "header_color" in kwargs:
            self.header_color = kwargs.pop("header_color")
        if "rows" in kwargs:
            self.rows = kwargs.pop("rows")
        if "columns" in kwargs:
            self.columns = kwargs.pop("columns")
        if "values" in kwargs:
            self.values = values
        if "padx" in kwargs:
            self.padx = kwargs.pop("padx")
        if "padx" in kwargs:
            self.pady = kwargs.pop("pady")
        
        self.update_values(self.values, **kwargs)
