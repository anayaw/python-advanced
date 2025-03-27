from tkinter import *
root = Tk()

from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser


# messagebox.askokcancel(message=' yo this weird code need to be flipping saved \n\t ok to save ?')


# messagebox.showinfo(message='you have a syntax error (how u aint notice that)')
# messagebox.showinfo(message='you have a syntax error (how u aint notice that)')
# messagebox.showinfo(message='you have a syntax error (how u aint notice that)')
# messagebox.showinfo(message='you have a syntax error (how u aint notice that)')
# messagebox.showinfo(message='you have a syntax error (stop ignoring me or else)')
# messagebox.showinfo(message='you have a syntax error (yu js noticed something was diff)')
# messagebox.showinfo(message='you have a syntax error (or mybe now ?)')
# messagebox.showinfo(message='you have a syntax error (anyways fix it)')



menubar = Menu(root) # create a Menu object
menu_file = Menu(menubar) # another Menu object, but a child of Menubar
menu_edit = Menu(menubar)
# a 'cascade' is an option along the menu bar
menubar.add_cascade(menu=menu_file, label='file')
menubar.add_cascade(menu=menu_edit, label='edit')
# a 'command' is an option in a Menu's dropdown options
menu_file.add_command(label='new')
menu_file.add_command(label='open...')
menu_file.add_command(label='close')
root.config(menu = menubar) # set menubar as the menu attribute of this window!
root.mainloop()

# close = messagebox.showinfo(message = 'you cant do this werid code . its lowk horrible . bye ig')
# if close:
#     root.quit()

open_filename = filedialog.askopenfilename() # 1
save_filename = filedialog.asksaveasfilename()# 2
dirname = filedialog.askdirectory() # 3

rgb, hex = colorchooser.askcolor(initialcolor='#ff0000')
print(rgb) # RGB representation of selected colour
print(hex) # HEX code representation of selected colour

# showinfo -> gives an 'ok' option
# showwarning -> gives an 'ok' option, window looks slightly different
# showerror -> gives an 'ok' option, window looks slightly different
# askyesno -> gives 'yes' and 'no' options
# askretrycancel -> gives 'retry' 'cancel' options

# new_window = Toplevel(root)
# new_window.title('pop yp') # change the title
# current_title = new_window.title() # get the current title
# new_window.geometry('300x200-5+20')
# # window will be 300 pixels wide, 200 tall, with top left corner at (5,20)
# new_window.resizable(True, False) # can resize width, not height
# new_window.destroy()