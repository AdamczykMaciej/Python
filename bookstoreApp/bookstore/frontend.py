from tkinter import *
from backend import Database

database=Database("books.db")

class BookStore:

    def __init__(self, window):
        self.window=window
        self.window.wm_title("BookStore")

        l1=Label(window, text="Title")
        l1.grid(row=0, column=0)
        l2=Label(window, text="Author")
        l2.grid(row=0, column=2)
        l3=Label(window, text="Year")
        l3.grid(row=1, column=0)
        l4=Label(window, text="ISBN")
        l4.grid(row=1, column=2)

        self.e1_value=StringVar()
        self.e1=Entry(window, textvariable=self.e1_value)
        self.e1.grid(row=0, column=1)
        self.e2_value=StringVar()
        self.e2=Entry(window, textvariable=self.e2_value)
        self.e2.grid(row=0, column=3)
        self.e3_value=StringVar()
        self.e3=Entry(window, textvariable=self.e3_value)
        self.e3.grid(row=1, column=1)
        self.e4_value=StringVar()
        self.e4=Entry(window, textvariable=self.e4_value)
        self.e4.grid(row=1, column=3)

        self.b1=Button(window, text="View all", width=12, command=self.view_command)
        self.b1.grid(row=2, column=3)
        self.b2=Button(window, text="Search entry", width=12, command=self.search_command)
        self.b2.grid(row=3, column=3)
        self.b3=Button(window, text="Add entry", width=12, command=self.insert_command)
        self.b3.grid(row=4, column=3)
        self.b4=Button(window, text="Update", width=12, command=self.update_command)
        self.b4.grid(row=5, column=3)
        self.b5=Button(window, text="Delete", width=12, command=self.delete_command)
        self.b5.grid(row=6, column=3)
        self.b6=Button(window, text="Close", width=12, command=self.window.destroy)
        self.b6.grid(row=7, column=3)

        self.lb=Listbox(window, height=6, width=35)
        self.lb.grid(row=2, column=0, rowspan=6, columnspan=2)
        self.lb.bind('<<ListboxSelect>>', self.get_selected_row)

        sb=Scrollbar(window)
        sb.grid(row=2, column=2, rowspan=6)

        self.lb.configure(yscrollcommand=sb.set)
        sb.configure(command=self.lb.yview)



    def get_selected_row(self,event):
        # I wrote this if, because if not then an error is thrown in my console when clicking or actually dragging cursor on one of my entries
        # after a selection of an item
        if(len(self.lb.curselection())>0):
            index=self.lb.curselection()[0]
            self.selected_tuple=self.lb.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, self.selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END, self.selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END, self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, self.selected_tuple[4])
            print(self.lb.curselection()[0])


    def view_command(self):
        self.lb.delete(0,END)
        for row in database.view():
            self.lb.insert(END, row)

    def search_command(self):
        self.lb.delete(0, END)
        for row in database.search(self.e1_value.get(), self.e2_value.get(), self.e3_value.get(), self.e4_value.get()):
            self.lb.insert(END,row)

    def insert_command(self):
        self.lb.delete(0, END)
        database.insert(self.e1_value.get(), self.e2_value.get(), self.e3_value.get(), self.e4_value.get())
        self.lb.insert(END, (self.e1_value.get(), self.e2_value.get(), self.e3_value.get(), self.e4_value.get()))

    def update_command(self):
        if(len(self.lb.curselection())>0):

            database.update(self.selected_tuple[0], self.e1_value.get(),self.e2_value.get(),self.e3_value.get(),self.e4_value.get())
            list_of_itemsA=self.lb.get(0, self.lb.curselection()[0]-1)
            list_of_itemsB=self.lb.get(self.lb.curselection()[0]+1, END)
            #print(list_of_itemsA)
            #print(list_of_itemsB)
            self.lb.delete(0, END)
            for row in list_of_itemsA:
                self.lb.insert(END, row)
            self.lb.insert(END, (self.selected_tuple[0], self.e1_value.get(),self.e2_value.get(),self.e3_value.get(),self.e4_value.get()))
            for row in list_of_itemsB:
                self.lb.insert(END, row)


    def delete_command(self):
        if(len(self.lb.curselection())>0):
            #we can't delete nothing
            list_of_itemsA=self.lb.get(0, self.lb.curselection()[0]-1)
            list_of_itemsB=self.lb.get(self.lb.curselection()[0]+1, END)
            #print(list_of_itemsA)
            #print(list_of_itemsB)
            self.lb.delete(0, END)
            database.delete(self.selected_tuple[0])
            for row in list_of_itemsA:
                self.lb.insert(END, row)
            for row in list_of_itemsB:
                self.lb.insert(END, row)
window=Tk()
bookstore=BookStore(window)
window.mainloop()
