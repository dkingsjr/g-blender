from tkinter import*

splash_root = Tk()
splash_root.title("g-blender\n By: Pressure Junkies")
splash_root.geometry("1000x500")

splash_label = Label(splash_root, text="g-blender\n By: Pressure Junkies", font=("helvetica", 18))
splash_label.pack(pady=20)



def main_window():
	splash_root.destroy()
	root = Tk()
	root.title("g-blender by Pressure Junkies")
	root.iconbitmap()
	root.geometry("1000x500")

def open():
	top = Toplevel()
	lbl = Label(top, text="hello world").pack
	btn2 = Button(top, text="Open Second Window", command=open).pack

btn = Button(splash_root, text="Open Second Window", command=open).pack

splash_root.after(3000, main_window)

mainloop()







"""
splash_root =Tk()
splash_root.title("Splash Screen!")
splash_root.geometry("500x300")

splash_label = Label(splash_root, text="g-blender\n By: Pressure Junkies", font=("helvetica", 18))
splash_label.pack

def mainframe():
	splash_root.destroy()
	root = Tk()
	root.title('New Project 1.0')
#root.iconbitmap('insert path')
	root.geometry("500x300")
	root.configure(bg='#384048')
#Removes frame from the window. Commented out for now due to development.
#root.overrideredirect(True)

#window dimensions(auto size)
#RWidth=root.winfo_screenwidth()
#RHeight=root.winfo_screenheight()
#root.geometry(("%dx%d")%(RWidth,RHeight))

#img = ImageTK.PhotoImage(image.open(path))
#panel = tk.Label(mainframe, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")

	mainframe = LabelFrame(root, bg='#384048', padx=15, pady=15, relief=SUNKEN)
	mainframe.pack(fill="both", expand=True, padx=15, pady=15)
	mainframe.columnconfigure(0, weight=2)
	mainframe.columnconfigure(1, weight=2)
	mainframe.columnconfigure(2, weight=2)


#Frame containing the app within the window.


#splash screen timer
splash_root.after(3000, mainframe)
mainloop()"""
