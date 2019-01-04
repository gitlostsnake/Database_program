from tkinter import *
import backend_roadworks

# Click a item in the list
def get_selected_row(event):
    global selected_roadworks
    index = list1.curselection()[0]
    selected_roadworks = list1.get(index)
    return(selected_roadworks)

### FUNCTIONS for buttons
def view_roadworks():
    # Deleteing from index 0 to the end so we dont duplicate items on dispay
    list1.delete(0, END)
    for row in backend_roadworks.view():
        list1.insert(END, row) # END means every new row is added at the end

### Currently only searches location column
def search_roadworks():
    list1.delete(0, END)
    for row in backend_roadworks.search(search_text.get()):
        list1.insert(END, row)

###
def delete_roadworks():
    backend_roadworks.delete(selected_roadworks[0])


#### Main
window=Tk()
window.title("TM Organiser")


#### Inventory Buttons on the left side
view_stk_b = Button(window, text= "View Stock", width=12)
view_stk_b.grid(row=1, column=0)

add_stk_b = Button(window, text= "Add Stock", width=12)
add_stk_b.grid(row=2, column=0)

remove_stk_b = Button(window, text= "Remove Stock", width=12)
remove_stk_b.grid(row=3, column=0)


#### Road works Buttons on the right side NOW ON LEFT
view_wrks_b = Button(window, text= "View Road Works", width=12,
                command = view_roadworks)
view_wrks_b.grid(row = 4, column = 0)

new_r_wrks_b = Button(window, text= "New Road Works", width=12)
new_r_wrks_b.grid(row = 5, column = 0)

del_r_wrks_b = Button(window, text= "Del Road Works", width=12,
                command = delete_roadworks)
del_r_wrks_b.grid(row= 6, column = 0)


### center button under main view box NOW ON LEFT
calculate_job = Button(window, text = "Calc Job", width=12)
calculate_job.grid(row = 9, column = 0, columnspan = 1)





#### Search bar at the top with an entry box to type into
# search_label = Label(window, text= "")
# search_label.grid(row=0, column=1)

search_text = StringVar()
e1=Entry(window, textvariable= search_text)
e1.grid(row=0, column=1)

search_button = Button(window, text= "Search", width = 8,
                    command = search_roadworks)
search_button.grid(row=0, column=2)

### Main view box listing items with scroll bar
list1 = Listbox(window, height=12,width=70)
list1.grid(row =1, column =1, rowspan = 15, columnspan = 15)

sb1= Scrollbar(window)
sb1.grid(row=4 ,column=16, rowspan = 1, columnspan = 2)

list1.bind('<<ListboxSelect>>', get_selected_row)

### Verticle scroll set to sb1
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)


window.mainloop()
