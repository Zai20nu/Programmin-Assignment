import tkinter as tk
import os
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("700x500")

tab_con = ttk.Notebook(root)

tab1= ttk.Frame(tab_con)
tab_con.add(tab1, text="Add Marks")
tab_con.pack(expand = 1 , fill= "both")

tab2 = ttk.Frame(tab_con)
tab_con.add(tab2, text="View Marks List")
tab_con.pack(expand = 1 , fill= "both")

tab3 = ttk.Frame(tab_con)
tab_con.add(tab3, text="Developer Info:")
tab_con.pack(expand = 1 , fill= "both")

text_wid = tk.Text(root)

def open_file():
    file_path = os.path.abspath(os.getcwd()) + "Student.txt"
    with open("Student.txt" , "r") as f:
        text_wid.delete("1.0", END)
        text_wid.insert("1.0",f.read())

root.title("All Student Marks List")
heading = Label(tab2,text = "All Student Marks List", font = ("calibri", 13))
heading.pack()


open_file_button = Button(tab2, text="Click", command=open_file)
text_wid.pack()
open_file_button.pack()


def my_reset():
	for widget in tab1.winfo_children():
		if isinstance(widget,Entry):
			widget.delete(0, 'end')

user = []
def save_info():
	name_info = name.get()
	sd_id = sid.get()
	sd_id = str(sd_id)

	module_name_info = module_name.get()
	module_grade_info = module_grade.get()
	print(name_info, sd_id, module_name_info, module_grade_info)

	file = open("Student.txt", "a")
	file.write(f"Name: {name_info}  ID: {sd_id}  Name: {module_name_info}  Grade: {module_grade_info}\n")
	print(" Dear Student ", name_info, " You are Successfully Submitted.")

name_text = Label(tab1,text = "Student Name : ",)
sid_text = Label(tab1,text = "Student ID : ",)
module_name_text = Label(tab1,text = "Module : ",)
module_grade_text = Label(tab1,text = "Grade: ",)
	 
name_text.place(x = 10, y = 50)
sid_text.place(x = 10, y = 125)
module_name_text.place(x = 10, y = 200)
module_grade_text.place(x = 10, y = 275)

name = StringVar()
sid = IntVar()
module_name = StringVar()
module_grade = StringVar() 

name_entry = Entry(tab1,textvariable = name)
sid_entry = Entry(tab1,textvariable = sid)
module_name_entry = Entry(tab1,textvariable = module_name)
module_grade_entry = Entry(tab1,textvariable = module_grade)

name_entry.place(x = 10, y = 75)
sid_entry.place(x = 10, y = 150)
module_name_entry.place(x = 10, y = 225)
module_grade_entry.place(x = 10, y = 300)

enter = Button(tab1, text = "Submit",command = save_info)
enter.place(x = 10, y = 350)
reset = Button(tab1, text = "Reset Records",command = lambda:my_reset())
reset.place(x = 95, y = 350)

about = Label(tab3, 
	text=" \n Developer Info:Shakeela  . \n Batch: CSD-18 2023 \n Programming Assignment. \n Email :ayasshahamed2000@gmail.com", 
	font = "Arial 22 bold" , justify="center")
about.pack()


root.mainloop()