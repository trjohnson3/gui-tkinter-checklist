import tkinter
from tkinter import END, ANCHOR

#Define root window
root = tkinter.Tk()
root.title('Checklist')
root.iconbitmap('./images/check.ico')
root.geometry('400x400')
root.resizable(0,0)

#Define fonts and colors
my_font = ('Times New Roman', 12)
root_color = '#6c1cbc'
button_color = '#e2cff4'
root.config(bg=root_color)

#Define funcitons
def add_item():
    '''Add an individual to the list box'''
    if list_entry.get().strip():
        my_listbox.insert(END, list_entry.get().strip())
        list_entry.delete(0, END)
    elif not list_entry.get().strip():
        list_entry.delete(0, END)

def remove_item():
    '''Delete the selected item from a list box'''
    my_listbox.delete(ANCHOR)

def remove_all_items():
    '''Delete the selected (ANCHOR) item from a list box'''
    my_listbox.delete(0, END)

def save_list():
    '''Save list to .txt file'''
    with open('checklist.txt', 'w') as f:
        #Listbox.get() returns a tuple...
        list_tuple = my_listbox.get(0, END)
        for item in list_tuple:
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item + '\n')

def open_list():
    '''Open saved list upon start if it exists'''
    try:
        with open('checklist.txt', 'r') as f:
            for line in f:
                my_listbox.insert(END, line)
    except:
        return
    


#Define layout
#Create frames
input_frame = tkinter.Frame(root, bg=root_color)
output_frame = tkinter.Frame(root, bg=root_color)
button_frame = tkinter.Frame(root, bg=root_color)
input_frame.pack()
output_frame.pack()
button_frame.pack()

#Input frame layout
list_entry = tkinter.Entry(input_frame, width=35, borderwidth=3, font=my_font)
add_button = tkinter.Button(input_frame, text='Add Item', borderwidth=2, font=my_font,
                            bg=button_color, command=add_item)
list_entry.grid(row=0, column=0, padx=5, pady=5)
add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=5)

#Output frame
my_scrollbar = tkinter.Scrollbar(output_frame)
my_listbox = tkinter.Listbox(output_frame, width=45, height=15, borderwidth=3, font=my_font,
                             yscrollcommand=my_scrollbar.set)
#Link scrollbar to listbox
my_scrollbar.config(command=my_listbox.yview)
my_listbox.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky='NS')

#Button frame layout
remove_item_button = tkinter.Button(button_frame, text='Remove Item', borderwidth=2, font=my_font,
                            bg=button_color, command=remove_item)
remove_all_button = tkinter.Button(button_frame, text='Clear List', borderwidth=2, font=my_font,
                            bg=button_color, command=remove_all_items)
save_button = tkinter.Button(button_frame, text='Save List', borderwidth=2, font=my_font,
                            bg=button_color, command=save_list)
quit_button = tkinter.Button(button_frame, text='Quit', borderwidth=2, font=my_font,
                            bg=button_color, command=root.destroy)
remove_item_button.grid(row=0, column=0, padx=5, pady=5, ipadx=5)
remove_all_button.grid(row=0, column=1, padx=5, pady=5, ipadx=5)
save_button.grid(row=0, column=2, padx=5, pady=5, ipadx=5)
quit_button.grid(row=0, column=3, padx=5, pady=5, ipadx=5)

#Open previous list if available
open_list()

#Run app
root.mainloop()
