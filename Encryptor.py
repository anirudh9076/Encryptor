import tkinter
from tkinter import *

from tkinter import filedialog

path=''
key=int()
root=Tk()

def Encrypt_file():
	wp=Tk()
	wp.geometry('600x600')
	wp.title("File Encryptor")


	def choosefile():
		global path
		path=filedialog.askopenfile()
		if path!='':
			l1=Label(wp,text="File Choosen and ready to be encrypted",bg='yellow').place(x=100,y=80)
			
	def encryptor():
		global path
		global key
		key=int(e_key.get())

		f=open(path.name,'rb')
		file=f.read()
		f.close()
		file=bytearray(file)
		for index , value in enumerate(file):
			file[index]=value^key
		f1=open('encrypted.jpg','wb')
		f1.write(file)
		f1.close()

	
	l2=Label(wp,text="Enter Encyption key").place(x=100,y=120)
	b_encrypt=Button(wp,text="Encrypt",bg='red',command=encryptor).place(x=150,y=150)
	e_key=Entry(wp,width=50)
	e_key.place(x=230,y=120)		
	
	wp.config(bg='grey')
	b_open=Button(wp,text="choose file",width=30,command=choosefile).place(x=100,y=50)
	b_back=Button(wp,text="Back",width=30,bg='red',command=wp.destroy).place(x=200,y=500)
	wp.mainloop()


def Decrypt_file():
	wp=Tk()
	wp.geometry('500x600')
	wp.title("File Decryptor")


	def choosefile():
		global path
		path=filedialog.askopenfile()
		if path!='':
			l1=Label(wp,text="File Choosen and ready to be encrypted",bg='yellow').place(x=100,y=80)
			
			


	def decryptor():
		global path
		global key
		key=int(e_key.get())
		f=open(path.name,'rb')
		file=f.read()
		f.close()
		file=bytearray(file)
		
		for index , value in enumerate(file):
			file[index]=value^key
		f1=open('decrypted.jpg','wb')
		f1.write(file)
		f1.close()
	
	l2=Label(wp,text="Enter Encyption key").place(x=100,y=120)
	b_encrypt=Button(wp,text="Decrypt",bg='red',command=decryptor).place(x=150,y=150)		
	e_key=Entry(wp,width=50)
	e_key.place(x=230,y=120)
			
	wp.config(bg='grey')
	b_open=Button(wp,text="choose file",width=30,command=choosefile).place(x=100,y=50)
	wp.mainloop()



root.geometry('500x600')
b_file=Button(root,text="Encrypt file",bg='sky blue',fg='white',command=Encrypt_file).place(x=120,y=120)
b_file=Button(root,text="decrypt file",bg='sky blue',fg='white',command=Decrypt_file).place(x=120,y=160)
root.mainloop()
