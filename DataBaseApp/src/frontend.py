from tkinter import *

from src import backend as bd


def get_select(event):
    try:
        global selected_tuple
        index = listbox.curselection()[0]
        selected_tuple = listbox.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])

    except:
        pass


def view_command():
    listbox.delete(0, END)
    for i in bd.view():
        listbox.insert(END, i)


def search_command():
    listbox.delete(0, END)
    for i in bd.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        listbox.insert(END, i)


def addentry_command():
    listbox.delete(0, END)
    bd.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    listbox.insert(END, "ENTRY ADDED TO DATABASE")


def delete_command():
    bd.delete(selected_tuple[0])


def update_command():
    bd.upadte(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


window = Tk()

window.wm_title("Book Store")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

listbox = Listbox(window, height=10, width=40)
listbox.grid(row=2, column=0, rowspan=7, columnspan=2)

sbar = Scrollbar(window)
sbar.grid(row=2, column=2, rowspan=7)

listbox.configure(yscrollcommand=sbar.set)
sbar.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>', get_select)

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=addentry_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
