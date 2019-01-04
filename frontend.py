from tkinter import *
import backend_roadworks

# Click a item in the main window
def get_selected_row(event):
    global selected_roadworks
    index = list1.curselection()[0]
    selected_roadworks = list1.get(index)
    Location_Entry.delete(0, END)
    Location_Entry.insert(END, selected_roadworks[1])
    Client_Entry.delete(0, END)
    Client_Entry.insert(END, selected_roadworks[2])
    Start_Date_Entry.delete(0, END)
    Start_Date_Entry.insert(END, selected_roadworks[3])
    End_Date_Entry.delete(0, END)
    End_Date_Entry.insert(END, selected_roadworks[4])
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
    list1.delete(0, END)
    for row in backend_roadworks.view():
        list1.insert(END, row)

### Adds info in the Entry boxes to the database
def Add_To_Roadworks():
    backend_roadworks.insert(Location_Text.get(), Client_Text.get(),
                            Start_Date_Text.get(), End_Date_Text.get())
    list1.delete(0, END)
    list1.insert(END, (Location_Text.get(), Client_Text.get(),
                            Start_Date_Text.get(), End_Date_Text.get()))


###
def Update_Roadworks():
    backend_roadworks.update(selected_roadworks[0],Location_Text.get(),
            Client_Text.get(), Start_Date_Text.get(), End_Date_Text.get())
    list1.delete(0, END)
    for row in backend_roadworks.view():
        list1.insert(END, row)



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

del_r_wrks_b = Button(window, text= "Del Road Works", width=12,
                command = delete_roadworks)
del_r_wrks_b.grid(row= 6, column = 0)


### center button under main view box NOW ON LEFT
calculate_job = Button(window, text = "Calc Job", width=12)
calculate_job.grid(row = 7, column = 0, columnspan = 1)





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
sb1.grid(row=3 ,column=16, rowspan = 4)

list1.bind('<<ListboxSelect>>', get_selected_row)

### Verticle scroll set to sb1
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)




### data entry to use add roadworks using labels instead of buttons
### so we can rig all of them up to the "Add to database" button
HEYlisten_ADD = Label(window, text="""
                        Fill in the fields, press ADD makes a new entry in road_works.db""")
HEYlisten_ADD.grid(row=16 , column= 0, columnspan = 4)


Location_Text = StringVar()

Location_Label = Label(window, text="Location")
Location_Label.grid(row= 17, column=0)
Location_Entry = Entry(window, textvariable= Location_Text)
Location_Entry.grid(row= 17, column=1 )

Client_Text = StringVar()

Client_Label = Label(window, text= "Client")
Client_Label.grid(row = 18, column =0 )
Client_Entry = Entry(window, textvariable= Client_Text)
Client_Entry.grid(row = 18, column =1 )


Start_Date_Text = StringVar()

Start_Date_Label = Label(window, text="Start Date \nYY-MM-DD 00:00")
Start_Date_Label.grid(row = 17, column = 2)
Start_Date_Entry = Entry(window, textvariable = Start_Date_Text)
Start_Date_Entry.grid(row= 17, column = 3)

End_Date_Text = StringVar()

End_Date_Label = Label(window, text="End Date \nYY-MM-DD 00:00")
End_Date_Label.grid(row = 18, column = 2)
End_Date_Entry = Entry(window, textvariable = End_Date_Text)
End_Date_Entry.grid(row= 18, column = 3)

new_r_wrks_b = Button(window, text= "Add to Database",
                            command = Add_To_Roadworks)
new_r_wrks_b.grid(row = 17, column = 4)

### PLUS Data Update using the same boxes as add to database.
Update_Database = Button(window, text= "Update Database",
                            command = Update_Roadworks)
Update_Database.grid(row = 18, column = 4)

###
HEYlisten_UPDATE = Label(window, text=
        "EDIT the fields and press the Update button to edit the selected")
HEYlisten_UPDATE.grid(row = 19, column = 0, columnspan = 4)

window.mainloop()
