from PIL import Image, ImageDraw, ImageFont
from customtkinter import CTkLabel
from PIL import ImageTk
class TableGenerator:
    def __init__(self,
                 values,
                 cell_widths : list,
                 cell_height : int,
                 colors:list,
                 font_size : int =15,
                 text_color : str = "white",
                 rectangle_color :str = "white",
                 table_to_tkinter : bool = True,
                 master_for_tkinter : any = None,
        )-> None:
        self.values = values
        self.cell_widths = cell_widths
        self.cell_height = cell_height
        self.row_count = len(values)
        self.column_count = len(values[0])
        self.image_width = sum(self.cell_widths) + 1
        self.image_height = self.row_count * self.cell_height + 1
        self.image = Image.new("RGB", (self.image_width, self.image_height), "black")
        self.draw = ImageDraw.Draw(self.image)
        self.font_path = "arial.ttf"  # Font path
        self.get_table = table_to_tkinter
        self.text_color = text_color
        self.rectangle_color = rectangle_color
        self.colors = colors
        self.font = self.load_font(font_size)
        
        self.master = master_for_tkinter
        print(self.column_count)
        print(len(cell_widths))
        if len(cell_widths)<self.column_count:
            for a in range(self.column_count-len(cell_widths)):
                self.cell_widths.append(self.cell_widths[0])
        print(len(self.cell_widths))
        self.draw_table()
    def load_font(self, font_size):
        try:
            return ImageFont.truetype(self.font_path, font_size)
        except IOError:
            return ImageFont.load_default()

    def draw_table(self)-> None:
        self.position = {}
          # Sabit bir yazı boyutu
        for i in range(self.row_count):
            for j in range(self.column_count):
                try:
                    x = sum(self.cell_widths[:j])
                except Exception as e:
                    x = j * self.cell_widths[0]
                    
                    print(e)
                y = i * self.cell_height

                try:
                    text = self.values[i][j]
                except:
                    text = " "
                text=str(text)
                self.position[x,y] = text
                # Yazı hücreye sığana kadar karakter sil
                while True:
                    text_size = self.draw.textbbox(text=text, font=self.font, xy=(0, 0))
                    if text_size[2]+10 <= self.cell_widths[j]:
                        break  # Yazı hücreye sığıyor, döngüden çık

                    text = text[:-4]
                    text = text + "..."
                    print(text)
                    if len(text)<4:
                        break

                      # Son karakteri sil

                # Metni ortala ve çiz
                text_x = x + (self.cell_widths[j] - text_size[2]) / 2
                text_y = y + (self.cell_height - text_size[3]) / 2

                self.draw.rectangle([x, y, x + self.cell_widths[j], y + self.cell_height], outline=self.rectangle_color,fill = self.colors[0] if i==0 else self.colors[i%2+1])
                self.draw.text((text_x, text_y), text, fill=self.text_color, font=self.font)
        if self.get_table:
            self.get_image_label()
    def save_image(self, file_name="values.png"):
        self.image.save(file_name)

    def show_image(self):
        self.image.show()
    def get_value(self, x: int, y: int) -> dict:

        # Koordinatların hangi hücreye ait olduğunu bul
        for i in range(self.row_count):
            row_start_y = i * self.cell_height
            row_end_y = row_start_y + self.cell_height
            if row_start_y <= y < row_end_y:
                row = i
                break
        else:
            return {"error": "Koordinat satır sınırlarının dışında."}

        for j in range(self.column_count):
            col_start_x = sum(self.cell_widths[:j])
            col_end_x = col_start_x + self.cell_widths[j]
            if col_start_x <= x < col_end_x:
                col = j
                break
        else:
            return {"error": "Koordinat sütun sınırlarının dışında."}

        return {
            "row": row,
            "column": col,
            "value": self.values[row][col]
        }
    def get_image_label(self) :

        # Görseli PIL Image'dan ImageTk formatına dönüştür
        image_tk = ImageTk.PhotoImage(self.image)
        # CustomTkinter Label oluştur ve görseli ayarla
        image_label = CTkLabel(self.master,text="", image=image_tk)

        # Görselin bellekte kalmasını sağla (bu adım görselin kaybolmasını engeller)
        image_label.image = image_tk

        self.CTkTable = image_label
    def update_values(self,values):
        self.values=values
        if self.row_count !=len(values):
            self.row_count = len(values)
            self.image_height = self.row_count * self.cell_height + 1
            self.image = Image.new("RGB", (self.image_width, self.image_height), "black")
            self.draw = ImageDraw.Draw(self.image)
        self.get_table = False
        self.draw_table()
        self.get_table = True
        image_tk = ImageTk.PhotoImage(self.image)
        self.CTkTable.configure(image=image_tk)
        self.CTkTable.image = image_tk
        self.CTkTable.update()
if __name__=="__main__":
    import customtkinter as ctk
    # Örnek tablo
    win = ctk.CTk()  # Doğru yazımı

    values = [
        ["ID", "Name", "Surname    dffsd    dsf  df", "Age"],
        ["1", "Ali", "Yilmaz", "30"],
        ["2", "Ayse", "Demir", "25"],
        ["3", "Mehmet", "Kaya", "28"]
    ]
    
    # Sınıfı kullanarak tabloyu oluştur ve görüntüle
    Tab = TableGenerator(values=values,cell_widths=[20,200,300,250],cell_height=30,colors=["#3050DD","#303030","#101010"],rectangle_color="black")
    
    Tab.draw_table()
    Tab.save_image()
    print(Tab.get_value(0,0))

    #Tab.show_image()
