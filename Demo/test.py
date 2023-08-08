import tkinter as tk
import customtkinter

from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk
import customtkinter
import tkinter
from PIL import ImageTk, Image
from sklearn.metrics.pairwise import cosine_similarity
import requests
from io import BytesIO


import pandas as pd

customtkinter.set_appearance_mode('light')
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom



root=tk.Tk()
root.geometry("1600x782")
# app=FullScreenApp(root)





books = pd.read_csv(r"D:\\học kỳ 1 năm 4\\recomender Systems\\Do An Cuoi Ky\\demo.csv")
list_name = list(books.title)
list_img = list(books.img)
list_name1 = list(books.name)
list_price = list(books.price)
list_description = list(books.description)

folder_img = 'D:\học kỳ 1 năm 4\\recomender Systems\Do An Cuoi Ky\\figure\\anh{}.jpg'



# van hoc
category_vanhoc = 'Nhà sách tiki/sách tiếng việt/sách văn học/tiểu thuyết'
index_vanhoc = list(books[books.category == category_vanhoc].index)
#kinh te

index_kinhte = list(books[books.category == 'Nhà sách tiki/sách tiếng việt/sách kinh tế/sách doanh nhân'].index)
#lich su

index_lichsu = list(books[books.category == 'Nhà sách tiki/sách tiếng việt/sách lịch sử/lịch sử việt nam'].index)
#thieu nhi

index_thieunhi = list(books[books.category == 'Nhà sách tiki/sách tiếng việt/sách thiếu nhi /truyện kể cho bé'].index)
#y te
index_yhoc = list(books[books.category == 'Nhà sách tiki/sách tiếng việt/sách y học'].index)



img_list = []
for i in range(1863):


    img = ImageTk.PhotoImage(Image.open(folder_img.format(i), 'r').resize((144,144)))
    img_list.append(img)
    
img_list_400 = []
for i in range(1863):


    img = ImageTk.PhotoImage(Image.open(folder_img.format(i), 'r').resize((400,400)))
    img_list_400.append(img)

# with CTK frmae
pickup_frame = customtkinter.CTkFrame(root)
pickup_frame.place(x=0, y=0, width=130, height=900)

pickup_frame.bind('<Button-1>', lambda e: print('with CKT FRAME'))
label1 = customtkinter.CTkLabel(pickup_frame, text = 'Danh mục')
label1.grid(row = 0,column  = 0, sticky = tk.W)


width_window = 590
height_window = 590
id = 0

def chose_category(value):
    global id, width_window, height_window, id_recsys
    # delivery_frame = Frame(root,  bg ="white")
    # delivery_frame.place(x=130, y=0, width=width_window/2, height=height_window)
    id_recsys = 0
    if value == 0:
        index_list = index_vanhoc
    elif value == 1:
        index_list = index_kinhte
    elif value == 2:
        index_list = index_thieunhi
    elif value == 3:
        index_list = index_lichsu
    else:
        index_list = index_yhoc 
    
    window1(id, index_list)
    # id += 6
    window2(id+6, index_list)
    
    




radio_var = tkinter.IntVar(value=10)
button1 = customtkinter.CTkRadioButton(pickup_frame, text = 'Sách văn học', variable = radio_var, value=0, command=lambda: chose_category(radio_var.get()))
button2 = customtkinter.CTkRadioButton(pickup_frame, text = 'Sách kinh tế', variable = radio_var, value=1, command=lambda: chose_category(radio_var.get()))
button3 = customtkinter.CTkRadioButton(pickup_frame, text = 'Sách thiếu nhi', variable = radio_var, value=2, command=lambda: chose_category(radio_var.get()))
button4 = customtkinter.CTkRadioButton(pickup_frame, text = 'Sách lịch sử', variable = radio_var, value=3, command=lambda: chose_category(radio_var.get()))
button5 = customtkinter.CTkRadioButton(pickup_frame, text = 'Sách y học', variable = radio_var, value=4, command=lambda: chose_category(radio_var.get()))


# button1.grid(row = 4, column = 0, sticky=tk.W)
button1.place(x = 10, y = 100)
button2.place(x = 10, y = 140)
button3.place(x = 10, y = 180)
button4.place(x = 10, y = 220)
button5.place(x = 10, y = 260)
# Without CKTFrame


id = 0
id_recsys = 0
list_book = []
def window1(id, index_list):
    global width_window, height_window
    delivery_frame = Frame(root,  bg ="white")
    delivery_frame.place(x=130, y=0, width=width_window*3, height=height_window)

    delivery_frame.bind('<Button-1>', lambda e: print('withOUt CKT FRAME'))


    book_1 = Label(delivery_frame, image=img_list[index_list[id]])
    book_1.grid(row = 0, column=0, pady=2, padx = 2)
    Label_book_1 = tk.Label(delivery_frame, text = list_name[index_list[id]],width = 2, height = 2, wraplength=90 , pady = 6)
    Label_book_1.grid(row = 1, column=0, sticky='nsew')
    
    book_2= tk.Label(delivery_frame, image=img_list[index_list[id+1]])
    book_2.grid(row = 2, column=0, pady=2)
    Label_book_2 = tk.Label(delivery_frame, text = list_name[index_list[id+1]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_2.grid(row = 3, column=0, sticky='nsew')
    
    book_3 = tk.Label(delivery_frame, image=img_list[index_list[id+2]])
    book_3.grid(row = 4, column=0, pady=2)
    Label_book_3 = tk.Label(delivery_frame, text = list_name[index_list[id+2]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_3.grid(row = 5, column=0, sticky='nsew')
    
    # 3 sách bên phải frame
    book_4 = Label(delivery_frame, image=img_list[index_list[id+3]])
    book_4.grid(row = 0, column=1, pady=2, padx = 2)
    Label_book_4 = tk.Label(delivery_frame, text = list_name[index_list[id+3]],width = 2, height = 2, wraplength=90 , pady = 6)
    Label_book_4.grid(row = 1, column=1, sticky='nsew')
    
    book_5= tk.Label(delivery_frame, image=img_list[index_list[id+4]])
    book_5.grid(row = 2, column=1, pady=2)
    Label_book_5 = tk.Label(delivery_frame, text = list_name[index_list[id+4]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_5.grid(row = 3, column=1, sticky='nsew')
    
    book_6 = tk.Label(delivery_frame, image=img_list[index_list[id+5]])
    book_6.grid(row = 4, column=1, pady=2)
    Label_book_6 = tk.Label(delivery_frame, text = list_name[index_list[id+5]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_6.grid(row = 5, column=1, sticky='nsew')
    
    # 3 sách bên phải frame-------------------------
    book_7 = Label(delivery_frame, image=img_list[index_list[id+6]])
    book_7.grid(row = 0, column=2, pady=2, padx = 2)
    Label_book_7 = tk.Label(delivery_frame, text = list_name[index_list[id+6]],width = 2, height = 2, wraplength=90 , pady = 6)
    Label_book_7.grid(row = 1, column=2, sticky='nsew')
    
    book_8= tk.Label(delivery_frame, image=img_list[index_list[id+7]])
    book_8.grid(row = 2, column=2, pady=2)
    Label_book_8 = tk.Label(delivery_frame, text = list_name[index_list[id+7]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_8.grid(row = 3, column=2, sticky='nsew')
    
    book_9 = tk.Label(delivery_frame, image=img_list[index_list[id+8]])
    book_9.grid(row = 4, column=2, pady=2)
    Label_book_9 = tk.Label(delivery_frame, text = list_name[index_list[id+8]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_9.grid(row = 5, column=2, sticky='nsew')
    
    # 3 sách bên phải frame
    book_10 = Label(delivery_frame, image=img_list[index_list[id+9]])
    book_10.grid(row = 0, column=3, pady=2, padx = 2)
    Label_book_10 = tk.Label(delivery_frame, text = list_name[index_list[id+9]],width = 2, height = 2, wraplength=90 , pady = 6)
    Label_book_10.grid(row = 1, column=3, sticky='nsew')
    
    book_11 = tk.Label(delivery_frame, image=img_list[index_list[id+10]])
    book_11.grid(row = 2, column=3, pady=2)
    Label_book_11 = tk.Label(delivery_frame, text = list_name[index_list[id+10]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_11.grid(row = 3, column=3, sticky='nsew')
    
    book_12 = tk.Label(delivery_frame, image=img_list[index_list[id+11]])
    book_12.grid(row = 4, column=3, pady=2)
    Label_book_12 = tk.Label(delivery_frame, text = list_name[index_list[id+11]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_12.grid(row = 5, column=3, sticky='nsew')
    
    # 3 sách bên phải frame
    book_13 = Label(delivery_frame, image=img_list[index_list[id+12]])
    book_13.grid(row = 0, column=4, pady=2, padx = 2)
    Label_book_13 = tk.Label(delivery_frame, text = list_name[index_list[id+12]],width = 2, height = 2, wraplength=90 , pady = 6)
    Label_book_13.grid(row = 1, column=4, sticky='nsew')
    
    book_14= tk.Label(delivery_frame, image=img_list[index_list[id+13]])
    book_14.grid(row = 2, column=4, pady=2)
    Label_book_14 = tk.Label(delivery_frame, text = list_name[index_list[id+13]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_14.grid(row = 3, column=4, sticky='nsew')
    
    book_15 = tk.Label(delivery_frame, image=img_list[index_list[id+14]])
    book_15.grid(row = 4, column=4, pady=2)
    Label_book_15 = tk.Label(delivery_frame, text = list_name[index_list[id+14]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_15.grid(row = 5, column=4, sticky='nsew')
    
    # 3 sách bên phải frame
    book_16 = Label(delivery_frame, image=img_list[index_list[id+15]])
    book_16.grid(row = 0, column=5, pady=2, padx = 2)
    Label_book_16 = tk.Label(delivery_frame, text = list_name[index_list[id+15]],width = 2, height = 2, wraplength=90 , pady = 6)
    Label_book_16.grid(row = 1, column=5, sticky='nsew')
    
    book_17= tk.Label(delivery_frame, image=img_list[index_list[id+16]])
    book_17.grid(row = 2, column=5, pady=2)
    Label_book_17 = tk.Label(delivery_frame, text = list_name[index_list[id+16]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_17.grid(row = 3, column=5, sticky='nsew')
    
    book_18 = tk.Label(delivery_frame, image=img_list[index_list[id+17]])
    book_18.grid(row = 4, column=5, pady=2)
    Label_book_18 = tk.Label(delivery_frame, text = list_name[index_list[id+17]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_18.grid(row = 5, column=5, sticky='nsew')
    
    # 3 sách bên phải frame
    book_19 = Label(delivery_frame, image=img_list[index_list[id+18]])
    book_19.grid(row = 0, column=6, pady=2, padx = 2)
    Label_book_19 = tk.Label(delivery_frame, text = list_name[index_list[id+18]],width = 2, height = 2, wraplength=90 , pady = 6)
    Label_book_19.grid(row = 1, column=6, sticky='nsew')
    
    book_20= tk.Label(delivery_frame, image=img_list[index_list[id+19]])
    book_20.grid(row = 2, column=6, pady=2)
    Label_book_20 = tk.Label(delivery_frame, text = list_name[index_list[id+19]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_20.grid(row = 3, column=6, sticky='nsew')
    
    book_21 = tk.Label(delivery_frame, image=img_list[index_list[id+20]])
    book_21.grid(row = 4, column=6, pady=2)
    Label_book_21 = tk.Label(delivery_frame, text = list_name[index_list[id+20]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_21.grid(row = 5, column=6, sticky='nsew')
    
    # 3 sách bên phải frame
    book_22 = Label(delivery_frame, image=img_list[index_list[id+21]])
    book_22.grid(row = 0, column=7, pady=2, padx = 2)
    Label_book_22 = tk.Label(delivery_frame, text = list_name[index_list[id+21]],width = 2, height = 2, wraplength=90 , pady = 6)
    Label_book_22.grid(row = 1, column=7, sticky='nsew')
    
    book_23= tk.Label(delivery_frame, image=img_list[index_list[id+22]])
    book_23.grid(row = 2, column=7, pady=2)
    Label_book_23 = tk.Label(delivery_frame, text = list_name[index_list[id+22]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_23.grid(row = 3, column=7, sticky='nsew')
    
    book_24 = tk.Label(delivery_frame, image=img_list[index_list[id+23]])
    book_24.grid(row = 4, column=7, pady=2)
    Label_book_24 = tk.Label(delivery_frame, text = list_name[index_list[id+23]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_24.grid(row = 5, column=7, sticky='nsew')
    
    # 3 sách bên phải frame
    book_25 = Label(delivery_frame, image=img_list[index_list[id+24]])
    book_25.grid(row = 0, column=8, pady=2, padx = 2)
    Label_book_25 = tk.Label(delivery_frame, text = list_name[index_list[id+24]],width = 2, height = 2, wraplength=90 , pady = 6)
    Label_book_25.grid(row = 1, column=8, sticky='nsew')
    
    book_26= tk.Label(delivery_frame, image=img_list[index_list[id+25]])
    book_26.grid(row = 2, column=8, pady=2)
    Label_book_26 = tk.Label(delivery_frame, text = list_name[index_list[id+25]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_26.grid(row = 3, column=8, sticky='nsew')
    
    book_27 = tk.Label(delivery_frame, image=img_list[index_list[id+26]])
    book_27.grid(row = 4, column=8, pady=2)
    Label_book_27 = tk.Label(delivery_frame, text = list_name[index_list[id+26]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_27.grid(row = 5, column=8, sticky='nsew')  
    
    
    
    
    
    # set event cho cac label
    book_1.bind('<Button-1>', lambda e: Calcosin(index_list[id]))
    book_2.bind('<Button-1>', lambda e: Calcosin(index_list[id+1]))
    book_3.bind('<Button-1>', lambda e: Calcosin(index_list[id+2]))
    book_4.bind('<Button-1>', lambda e: Calcosin(index_list[id+3]))
    book_5.bind('<Button-1>', lambda e: Calcosin(index_list[id+4]))
    book_6.bind('<Button-1>', lambda e: Calcosin(index_list[id+5]))
    #---
    book_7.bind('<Button-1>', lambda e: Calcosin(index_list[id+6]))
    book_8.bind('<Button-1>', lambda e: Calcosin(index_list[id+7]))
    book_9.bind('<Button-1>', lambda e: Calcosin(index_list[id+8]))
    book_10.bind('<Button-1>', lambda e: Calcosin(index_list[id+9]))
    book_11.bind('<Button-1>', lambda e: Calcosin(index_list[id+10]))
    book_12.bind('<Button-1>', lambda e: Calcosin(index_list[id+11]))
    book_13.bind('<Button-1>', lambda e: Calcosin(index_list[id+12]))
    book_14.bind('<Button-1>', lambda e: Calcosin(index_list[id+13]))
    book_15.bind('<Button-1>', lambda e: Calcosin(index_list[id+14]))
    book_16.bind('<Button-1>', lambda e: Calcosin(index_list[id+15]))
    book_17.bind('<Button-1>', lambda e: Calcosin(index_list[id+16]))
    book_18.bind('<Button-1>', lambda e: Calcosin(index_list[id+17]))
    book_19.bind('<Button-1>', lambda e: Calcosin(index_list[id+18]))
    book_20.bind('<Button-1>', lambda e: Calcosin(index_list[id+19]))
    book_21.bind('<Button-1>', lambda e: Calcosin(index_list[id+20]))
    book_22.bind('<Button-1>', lambda e: Calcosin(index_list[id+21]))
    book_23.bind('<Button-1>', lambda e: Calcosin(index_list[id+22]))
    book_24.bind('<Button-1>', lambda e: Calcosin(index_list[id+23]))
    book_25.bind('<Button-1>', lambda e: Calcosin(index_list[id+24]))
    book_26.bind('<Button-1>', lambda e: Calcosin(index_list[id+25]))
    book_27.bind('<Button-1>', lambda e: Calcosin(index_list[id+26]))


def window2(id, index_list):
    global width_window, height_window
    delivery_frame = Frame(root,  bg ="white")
    delivery_frame.place(x=130 , y=width_window, width=width_window*3, height=height_window)

    delivery_frame.bind('<Button-1>', lambda e: print('withOUt CKT FRAME'))

    book_7 = Label(delivery_frame, image=img_list[index_list[id]])
    book_7.grid(row = 0, column=0, pady=2, padx = 2)
    Label_book_7 = tk.Label(delivery_frame, text = list_name[index_list[id]], wraplength=90, width = 2, height = 2, pady = 6)
    Label_book_7.grid(row = 1, column=0, sticky='nsew')
    
    book_8 = tk.Label(delivery_frame, image=img_list[index_list[id+1]])
    book_8.grid(row = 0, column=1, pady=2, padx = 2)
    Label_book_8 = tk.Label(delivery_frame, text = list_name[index_list[id+1]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_8.grid(row = 1, column=1, sticky='nsew')
    
    book_9 = tk.Label(delivery_frame, image=img_list[index_list[id+2]])
    book_9.grid(row = 0, column=2, pady=2, padx = 2)
    Label_book_9 = tk.Label(delivery_frame, text = list_name[index_list[id+2]],  width = 2, height = 2, pady = 7, wraplength=90)
    Label_book_9.grid(row = 1, column=2, sticky='nsew')
    #----------------------------------------------------------------
    book_10 = Label(delivery_frame, image=img_list[index_list[id+3]])
    book_10.grid(row = 0, column=3, pady=2, padx = 2)
    Label_book_10 = tk.Label(delivery_frame, text = list_name[index_list[id+3]], wraplength=90, width = 2, height = 2, pady = 6)
    Label_book_10.grid(row = 1, column=3, sticky='nsew')
    
    book_11 = tk.Label(delivery_frame, image=img_list[index_list[id+4]])
    book_11.grid(row = 0, column=4, pady=2, padx = 2)
    Label_book_11 = tk.Label(delivery_frame, text = list_name[index_list[id+4]],  width = 2, height = 2, wraplength=90, pady = 6)
    Label_book_11.grid(row = 1, column=4, sticky='nsew')
    
    book_12 = tk.Label(delivery_frame, image=img_list[index_list[id+5]])
    book_12.grid(row = 0, column=5, pady=2, padx = 2)
    Label_book_12 = tk.Label(delivery_frame, text = list_name[index_list[id+5]],  width = 2, height = 2, pady = 6,wraplength=90)
    Label_book_12.grid(row = 1, column=5, sticky='nsew')
    #---------  --------
    book_13 = tk.Label(delivery_frame, image=img_list[index_list[id+6]])
    book_13.grid(row = 0, column=6, pady=2, padx = 2)
    Label_book_13 = tk.Label(delivery_frame, text = list_name[index_list[id+6]],  width = 2, height = 2, pady = 6,wraplength=90)
    Label_book_13.grid(row = 1, column=6, sticky='nsew')
    
    book_14 = tk.Label(delivery_frame, image=img_list[index_list[id+7]])
    book_14.grid(row = 0, column=7, pady=2, padx = 2)
    Label_book_14 = tk.Label(delivery_frame, text = list_name[index_list[id+7]],  width = 2, height = 2, pady = 6,wraplength=90)
    Label_book_14.grid(row = 1, column=7, sticky='nsew')
    
    book_15 = tk.Label(delivery_frame, image=img_list[index_list[id+8]])
    book_15.grid(row = 0, column=8, pady=2, padx = 2)
    Label_book_15 = tk.Label(delivery_frame, text = list_name[index_list[id+8]],  width = 2, height = 2, pady = 6,wraplength=90)
    Label_book_15.grid(row = 1, column=8, sticky='nsew')
    
    book_7.bind('<Button-1>', lambda e: Calcosin(index_list[id]))
    book_8.bind('<Button-1>', lambda e: Calcosin(index_list[id+1]))
    book_9.bind('<Button-1>', lambda e: Calcosin(index_list[id+2]))
    book_10.bind('<Button-1>', lambda e: Calcosin(index_list[id+3]))
    book_11.bind('<Button-1>', lambda e: Calcosin(index_list[id+4]))
    book_12.bind('<Button-1>', lambda e: Calcosin(index_list[id+5]))
    #---
    book_13.bind('<Button-1>', lambda e: Calcosin(index_list[id+6]))
    book_14.bind('<Button-1>', lambda e: Calcosin(index_list[id+7]))
    book_15.bind('<Button-1>', lambda e: Calcosin(index_list[id+8]))

def check(id):
   
    if id <= 0:
        return False
    return True



def Back():
    global id , id_recsys, list_recsys
    
    
    if check(id_recsys) == True:
        id_recsys -= 9
        window2(id_recsys, list_recsys)
    elif check(id) == True:
        id = id - 27
        chose_category(radio_var.get())
def Next():
    global id, id_recsys, list_recsys
    
    if check(id_recsys) != False:
        id_recsys += 27
        window2(id_recsys, list_recsys)
    else:
        id += 27
        chose_category(radio_var.get())
    
def showframe():
    delivery_frame2 = Frame(root,  bg ="blue")
    delivery_frame2.place(x=130, y=0, width=550*3, height=600)
    
    
    
    
    
button_back = customtkinter.CTkButton(pickup_frame, text = 'back', height=2, width=2, command=lambda: Back())
button_back.place(x = 10, y = 50)
button_next = customtkinter.CTkButton(pickup_frame, text = 'next', height=2, width=2, command = lambda: Next())
button_next.place(x = 70, y = 50)


# show ra các sách được khuyến nghị
# lấy ma trận cosin
vectors = pd.read_csv(r'D:\học kỳ 1 năm 4\recomender Systems\Do An Cuoi Ky\CB-wordembedding-demo.csv', header = None)
vectors = vectors.to_numpy()

# tính cosin của sách được chọn và cả ma trận
list_recsys = []
def Calcosin(id_book):
    global id_recsys, list_recsys
    similarity_matrix = cosine_similarity(vectors, vectors[id_book].reshape(1, -1))
    data = sorted(list(enumerate(similarity_matrix)), key=lambda x:x[1], reverse = True)
    data1 = [data[i][0] for i in range(len(data))]
    list_recsys = data1
    id_recsys = 1
    ShowRecSysWin1(0, list_recsys)
    window2(id_recsys, list_recsys)




# show thông tin cuốn sách được chọn
def ShowRecSysWin1(book_id, index_list):
    
    global width_window, height_window
    delivery_frame1 = Frame(root,  bg ="white")
    delivery_frame1.place(x=130, y=0, width=width_window*3, height=height_window)

    delivery_frame1.bind('<Button-1>', lambda e: print('withOUt CKT FRAME'))
    # ảnh
    thumnail_label = tk.Label(delivery_frame1, image=img_list_400[index_list[book_id]])
    thumnail_label.grid(row = 0, column=0, pady=2, padx = 2)
    # tiêu đề
    title = tk.Label(delivery_frame1, text = list_name1[index_list[book_id]], font=("Arial", 25),wraplength=900, bg = 'white')
    title.place(x = 450, y = 50)
    # giá 
    price = tk.Label(delivery_frame1, text = "Giá: {}đ".format(list_price[index_list[book_id]]), font=("Arial", 20), bg = 'white')
    price.place(x = 450, y = 160)   
    
    # mô tả sản phẩm 
    description = tk.Label(delivery_frame1, text = list_description[index_list[book_id]], font=("Arial", 10),wraplength=900, bg = 'white',  anchor='w', justify=LEFT)
    description.place(x = 450, y = 200)  
    # description.pack(fill='both')


    # button_mua
    button_mua = customtkinter.CTkButton(delivery_frame1,text ="Mua" )
    button_mua.place(x = 50, y = 450)
    # bỏ vào giỏ
    button_mua = customtkinter.CTkButton(delivery_frame1,text ="Bỏ vào giỏ" )
    button_mua.place(x = 200, y = 450)
root.mainloop()