from tkinter import *
import backend.py

#### Main
window=Tk()
window.title("Stock Management System")


#### Inventory Buttons on the left side
view_stk_b = Button(window, text= "View Stock", width=12)
view_stk_b.grid(row=1, column=0)

add_stk_b = Button(window, text= "Add Stock", width=12)
add_stk_b.grid(row=2, column=0)

remove_stk_b = Button(window, text= "Remove Stock", width=12)
remove_stk_b.grid(row=3, column=0)


#### Road works Buttons on the right side
view_wrks_b = Button(window, text= "View Road Works", width=12)
view_wrks_b.grid(row=1, column=6)

new_r_wrks_b = Button(window, text= "New Road Works", width=12)
new_r_wrks_b.grid(row=2, column=6)

calculate_job = Button(window, text= "Calculate Job", width=12)
calculate_job.grid(row=3, column=6)



#### Search bar at the top with an entry box to type into
search_label = Label(window, text= "Search job #")
search_label.grid(row=0, column=1)

search_text = StringVar()
e1=Entry(window, textvariable= search_text)
e1.grid(row=0, column=2)



#### Main view box listing items with scroll bar...
list1 = Listbox(window, height=6,width=35)
list1.grid(row =1, column =1, rowspan = 6, columnspan = 3)

sb1= Scrollbar(window)
sb1.grid(row=2 ,column=4, rowspan = 4)

### Verticle scroll set to sb1
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)


window.mainloop()
