from tkinter import *
root = Tk()
root.geometry("420x600")
root.title("Calculator - code with yash")

def clik(event):
	global scvalue
	text= event.widget.cget("text")
	if text == "=":
		if scvalue.get().isdigit():
			value = int(scvalue.get())
		else:
			try:

				value = eval(screen.get())

			except Exception as e:
				print(e)
				value = "Error.."
			scvalue.set(value)
			screen.update()

	elif text == "C":
		scvalue.set("")
		screen.update()
	else:
		scvalue.set(scvalue.get() + text)
		screen.update()

root.wm_iconbitmap("C:\\Users\\Admin\\Downloads\\iconfly.PNG")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue, font="lucida 40 bold",bg="gold")
screen.pack(fill=X,ipadx=8,padx=18,pady=10)

f = Frame(root, bg="grey")
b = Button(f, text="9",padx=20,pady=7,font="lucida 30 bold",bg="goldenrod")
b.pack(side=LEFT,padx=8,pady=3)
b.bind("<Button-1>",clik)
f.pack()
b = Button(f, text="8",padx=20,pady=7,font="lucida 30 bold",bg="goldenrod")
b.pack(side=LEFT,pady=3)
b.bind("<Button-1>",clik)
b = Button(f, text="7",padx=20,pady=7,font="lucida 30 bold",bg="goldenrod")
b.pack(side=LEFT,padx=8,pady=3)
b.bind("<Button-1>",clik)
b = Button(f, text="-",padx=10,pady=7,font="lucida 30 bold",bg="red")
b.pack(side=LEFT,padx=5,pady=3)
b.bind("<Button-1>",clik)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="6",padx=20,pady=7,font="lucida 30 bold",bg="goldenrod")
b.pack(side=LEFT,padx=8,pady=3)
b.bind("<Button-1>",clik)
f.pack()
b = Button(f, text="5",padx=20,pady=10,font="lucida 30 bold",bg="goldenrod")
b.pack(side=LEFT,pady=3)
b.bind("<Button-1>",clik)
b = Button(f, text="4",padx=20,pady=7,font="lucida 30 bold",bg="goldenrod")
b.pack(side=LEFT,padx=8,pady=3)
b.bind("<Button-1>",clik)
b = Button(f, text="*",padx=10,pady=7,font="lucida 30 bold",bg="red")
b.pack(side=LEFT,padx=4,pady=3)
b.bind("<Button-1>",clik)

f = Frame(root, bg="grey")
b = Button(f, text="3",padx=20,pady=7,font="lucida 30 bold",bg="goldenrod")
b.pack(side=LEFT,padx=7,pady=3)
b.bind("<Button-1>",clik)
f.pack()
b = Button(f, text="2",padx=20,pady=7,font="lucida 30 bold",bg="goldenrod")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",clik)
b = Button(f, text="1",padx=20,pady=7,font="lucida 30 bold",bg="goldenrod")
b.pack(side=LEFT,padx=5,pady=3)
b.bind("<Button-1>",clik)
b = Button(f, text="/",padx=10,pady=7,font="lucida 30 bold",bg="red")
b.pack(side=LEFT,padx=8,pady=3)
b.bind("<Button-1>",clik)

f = Frame(root, bg="grey")
b = Button(f, text="0",padx=38,pady=7,font="lucida 30 bold",bg="goldenrod")
b.pack(side=LEFT,padx=5,pady=3)
b.bind("<Button-1>",clik)
f.pack()
b = Button(f, text="=",padx=10,pady=7,font="lucida 30 bold",bg="red")
b.pack(side=LEFT,padx=4,pady=3)
b.bind("<Button-1>",clik)
b = Button(f, text="C",padx=10,pady=7,font="lucida 30 bold",bg="red")
b.pack(side=LEFT,padx=5,pady=3)
b.bind("<Button-1>",clik)
b = Button(f, text="-",padx=10,pady=7,font="lucida 30 bold",bg="red")
b.pack(side=LEFT,padx=5,pady=3)
b.bind("<Button-1>",clik)
f.pack()

f = Frame(root, bg="grey")
f.pack()
b = Button(f, text="%",padx=2,pady=7,font="lucida 30 bold",bg="red")
b.pack(side=RIGHT,padx=3,pady=3)
b.bind("<Button-1>",clik)
b = Button(f, text="+",padx=12,pady=7,font="lucida 30 bold",bg="red")
b.pack(side=RIGHT,padx=3,pady=3)
b.bind("<Button-1>",clik)
b = Button(f, text=".",padx=15,pady=7,font="lucida 30 bold",bg="red")
b.pack(side=RIGHT,padx=3,pady=3)
b.bind("<Button-1>",clik)
b = Button(f, text="00",padx=30,pady=7,font="lucida 30 bold",bg="red")
b.pack(side=RIGHT,padx=5,pady=3)
b.bind("<Button-1>",clik)

root.mainloop()