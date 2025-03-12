"""CTkTable: example1"""

# ₿ python3.11 -m examples.example1

import sys

import tkinter
import customtkinter as ctk

from CTkTable import CTkTable


class App(ctk.CTk):
    """CTkTable: example1"""

    super_frame: ctk.CTkBaseClass

    def my_cell_generator2(self, master, row, column, **kwarg)->ctk.CTkBaseClass:
        """just a cell generator2"""
        frame = ctk.CTkFrame(master)
        label = ctk.CTkLabel(frame, text=f"{row}-{column}", fg_color=kwarg["fg_color"])
        original_text = kwarg["text"]
        del kwarg["text"]
        # label = ctk.CTkButton (frame, text=f"{row}-{column}", **kwarg)
        label.grid(sticky=ctk.NSEW)
        button = ctk.CTkButton(frame, text=original_text, **kwarg)
        button.grid(row=0, column=1)
        return frame

    def my_cell_generator3(self, master, row, column, **kwarg)->ctk.CTkBaseClass:
        """just a cell generator3"""
        if 0 == column:
            return ctk.CTkCheckBox(
                master, text=f"checkbox{row}", bg_color=kwarg["fg_color"]
            )
        return CTkTable.default_cell_generator(master, row, column, **kwarg)
        # return self.my_cell_generator2(master, row, column, **kwarg)

    def my_cell_generator4(self, master, row, column, **kwarg)->ctk.CTkBaseClass:
        """just a cell generator4"""
        return ctk.CTkEntry(
            master,
            textvariable=tkinter.StringVar(master, kwarg["text"]),
            fg_color=kwarg["fg_color"],
        )

    def redraw(self):
        """redraw"""
        values = []
        for i in range(3):
            row = []
            for j in range(2):
                row.append((i + 1) * (j + 1))
            values.append(row)
        if self.super_frame is not None:
            self.super_frame.destroy()
        self.super_frame = ctk.CTkFrame(self)
        self.super_frame.grid_rowconfigure(0, weight=1)
        self.super_frame.grid_columnconfigure(0, weight=1)
        self.table1 = CTkTable(self.super_frame, values=values)
        self.table1.grid(padx=4, pady=4)

        self.table2 = CTkTable(
            self.super_frame, values=values, cell_generator=self.my_cell_generator2
        )
        self.table2.grid(padx=4, pady=4)

        self.table3 = CTkTable(
            self.super_frame, values=values, cell_generator=self.my_cell_generator3
        )
        self.table3.grid(padx=4, pady=4)

        self.table4 = CTkTable(
            self.super_frame, values=values, cell_generator=self.my_cell_generator4
        )
        self.table4.grid(padx=4, pady=4)
        self.super_frame.grid()

    def __init__(self, title: str, geometry: str, **kwargs):
        super().__init__(**kwargs)
        self.super_frame = None
        print(sys.version)
        self.title(title)
        self.geometry(geometry)
        button = ctk.CTkButton(self, text="Redraw", command=self.redraw)
        button.grid()
        self.redraw()


if __name__ == "__main__":
    app = App(title="example1", geometry="400x500")
    app.update()
    app.mainloop()
