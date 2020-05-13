from tkinter import *
from tkinter import filedialog

def En_file():
	wp=Tk()
	wp.geometry('600x600')
	wp.title("File Encryptor")


	def choosefile():
		path=filedialog.askopenfile()
		if path!='':
			l1=Label(wp,text="File Choosen and ready to be encrypted",bg='yellow').place(x=100,y=80)
			l2=Label(wp,text="Enter Encyption key").place(x=100,y=120)
			e_key=Entry(wp,width=50).place(x=230,y=120)
			b_encrypt=Button(wp,text="Encrypt File",bg='red').place(x=150,y=150)
			
	wp.config(bg='grey')
	b_open=Button(wp,text="choose file",width=30,command=choosefile).place(x=100,y=50)
	wp.mainloop()


root=Tk()
root.geometry('600x600')
b_file=Button(root,text="Encrypt file",bg='sky blue',fg='white',command=En_file).place(x=120,y=120)
root.mainloop()
