import tkinter

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

#Run app
root.mainloop()
