
from tkinter import *
from tkinter import filedialog

path=''

def Encrypt_file():
	wp=Tk()
	wp.geometry('600x600')
	wp.title("File Encryptor")


	def choosefile():
		global path
		path=filedialog.askopenfile()
		if path!='':
			l1=Label(wp,text="File Choosen and ready to be encrypted",bg='yellow').place(x=100,y=80)
			l2=Label(wp,text="Enter Encyption key").place(x=100,y=120)
			e_key=Entry(wp,width=50).place(x=230,y=120)
			b_encrypt=Button(wp,text="Encrypt",bg='red',command=encryptor).place(x=150,y=150)
	def encryptor():
		global path

		f=open(path.name,'rb')
		file=f.read()
		f.close()
		file=bytearray(file)
		key=123
		for index , value in enumerate(file):
			file[index]=value^key
		f1=open('encrypted.jpg','wb')
		f1.write(file)
		f1.close()
	
			
	wp.config(bg='grey')
	b_open=Button(wp,text="choose file",width=30,command=choosefile).place(x=100,y=50)
	wp.mainloop()


def decrypt_file():
	wp=Tk()
	wp.geometry('600x600')
	wp.title("File Encryptor")


	def choosefile():
		global path
		path=filedialog.askopenfile()
		if path!='':
			l1=Label(wp,text="File Choosen and ready to be encrypted",bg='yellow').place(x=100,y=80)
			l2=Label(wp,text="Enter Encyption key").place(x=100,y=120)
			e_key=Entry(wp,width=50).place(x=230,y=120)
			b_encrypt=Button(wp,text="Decrypt",bg='red',command=decryptor).place(x=150,y=150)
	
	def decryptor():
		global path

		f=open(path.name,'rb')
		file=f.read()
		f.close()
		file=bytearray(file)
		key=123
		for index , value in enumerate(file):
			file[index]=value^key
		f1=open('decrypted.jpg','wb')
		f1.write(file)
		f1.close()
			
	wp.config(bg='grey')
	b_open=Button(wp,text="choose file",width=30,command=choosefile).place(x=100,y=50)
	wp.mainloop()

root=Tk()
root.geometry('600x600')
b_file=Button(root,text="Encrypt file",bg='sky blue',fg='white',command=Encrypt_file).place(x=120,y=120)
b_file=Button(root,text="decrypt file",bg='sky blue',fg='white',command=decrypt_file).place(x=120,y=160)
root.mainloop()
