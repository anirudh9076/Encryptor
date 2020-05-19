from tkinter import *

from tkinter import filedialog
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox
from email.mime.base import MIMEBase
from email import encoders
import os.path
import imaplib, email, os

path='' 	#to make the path accessible in any function
key=int()   # to make the accessible in every function
root=Tk()  # main window when program runs

def Encrypt_file():
	wp=Tk() #ecnryptor window
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
	b_back=Button(wp,text="Back",width=10,bg='sky blue',command=wp.destroy).place(x=200,y=400)
	wp.mainloop()


def Decrypt_file():
	wp=Tk() #decryptor window
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
	b_encrypt=Button(wp,text="Decrypt",bg='blue',command=decryptor).place(x=150,y=150)		
	e_key=Entry(wp,width=50)
	e_key.place(x=230,y=120)
			
	wp.config(bg='grey')
	b_open=Button(wp,text="choose file",width=30,command=choosefile).place(x=100,y=50)
	b_back=Button(wp,text="Back",width=10,bg='sky blue',command=wp.destroy).place(x=200,y=400)
	wp.mainloop()


def Emailing():
	
	wm=Tk() # window for mailing



	def choosefile():
		global path
		path=filedialog.askopenfile()
		if path!='':
			l1=Label(wm,text="File Choosen and ready to be encrypted",bg='yellow').pack()

	def sendmail():
		email=e1.get()
		password=e2.get()
		sendto=e3.get()
		sub1=e4.get()
		message1=e5.get()
		key=int(e6.get())
		subject=''
		message=''
		alphabet='abcdefghijklmnopqrstuvwxyz'
		for i in sub1:     #to encrypt subject
			position=alphabet.find(i)
			newposition=(position+key)%26
			subject+=alphabet[newposition]
		for i in message1:	# to encrypt message
			position=alphabet.find(i)
			newposition=(position+key)%26
			message+=alphabet[newposition]



		f=open(path.name,'rb')
		file=f.read()
		f.close()
		file=bytearray(file)
		for index , value in enumerate(file):
			file[index]=value^key

		f1=open('sendfile.jpg','wb')
		f1.write(file)
		f1.close()

		
		

		msg=MIMEMultipart()
		msg['From']=email
		msg['To']=sendto
		msg['subject']=subject
		msg.attach(MIMEText(message,'plain'))


		filename=os.path.basename('sendfile.jpg')
		attachment=open(filename,'rb')
		part=MIMEBase('application','octet.stream')
		part.set_payload(attachment.read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition','attachment;filename="%s"'%filename)
		msg.attach(part)

		server=smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login(email,password)
		txt=msg.as_string()
		server.sendmail(email,sendto,txt)
		server.quit()
		messagebox.showinfo('email send','sent')


	l=Label(wm,text='Welcome to encypted mailing',font='arial',fg='blue').place(x=150,y=50)
	l1=Label(wm,text='Username:').place(x=50,y=100)
	e1=Entry(wm,width=40)
	e1.place(x=150,y=100)
	l2=Label(wm,text='Password:').place(x=50,y=150)
	e2=Entry(wm,width=40)
	e2.place(x=150,y=150)
	l3=Label(wm,text='Send To:').place(x=50,y=200)
	e3=Entry(wm,width=40)
	e3.place(x=150,y=200)
	l4=Label(wm,text='Subject:').place(x=50,y=250)
	e4=Entry(wm,width=40)
	e4.place(x=150,y=250)
	l5=Label(wm,text='Message:').place(x=50,y=300)
	e5=Entry(wm,width=60)
	e5.place(x=150,y=300,height=50)
	l6=Label(wm,text='Enter Key:').place(x=50,y=470)
	e6=Entry(wm,width=60)
	e6.place(x=150,y=470)
	b_open=Button(wm,text="choose file",width=30,command=choosefile).place(x=50,y=420)
	b=Button(wm,text='Send',fg='dark green',bg='light green',command=sendmail)
	b.place(x=250,y=550)
	wm.title("Encrypted Email Terminal")
	wm.geometry('500x600')
	wm.mainloop()


def getmail():
	wm=Tk() # window to get encrypyed attachment and decrypt them
	

	def readmail():
		user=e1.get()
		password=e2.get()
		imap_url = 'imap.gmail.com'
		attachment_dir = 'H:\Programing\Encryptor'
		# sets up the auth
		def auth(user,password,imap_url):
			con = imaplib.IMAP4_SSL(imap_url)
			con.login(user,password)
			return con

		def get_attachments(msg):
		    for part in msg.walk():
		        if part.get_content_maintype()=='multipart':
		            continue
		        if part.get('Content-Disposition') is None:
		            continue
		        fileName = part.get_filename()

		        if bool(fileName):
		            filePath = os.path.join(attachment_dir, fileName)
		            with open(filePath,'wb') as f:
		                f.write(part.get_payload(decode=True))
		    
		    
		    key=int(e3.get())
		    f=open(fileName,'rb')
		    file=f.read()
		    f.close()
		    file=bytearray(file)
		    for index ,value in enumerate(file):
		        file[index]=value^key
		    f1=open(fileName,'wb')
		    f1.write(file)
		    f1.close()


		con = auth(user,password,imap_url)
		con.select('INBOX')

		result, data = con.fetch(b'5','(RFC822)')
		raw = email.message_from_bytes(data[0][1])
		get_attachments(raw)

	


	
	l=Label(wm,text='Welcome to encypted mailing',font='arial',fg='blue').place(x=150,y=50)
	l1=Label(wm,text='Username:').place(x=50,y=100)
	e1=Entry(wm,width=40)
	e1.place(x=150,y=100)
	l2=Label(wm,text='Password:').place(x=50,y=150)
	e2=Entry(wm,width=40)
	e2.place(x=150,y=150)
	l3=Label(wm,text='Enter Key:').place(x=50,y=470)
	e3=Entry(wm,width=60)
	e3.place(x=150,y=470)
	b=Button(wm,text='Get',fg='dark green',bg='light green',command=readmail)
	b.place(x=250,y=550)
	wm.title("Encrypted Email Terminal")
	wm.geometry('500x600')
	wm.mainloop()





root.geometry('500x450')
b_encrypt=Button(root,text="Encrypt file",bg='sky blue',fg='black',command=Encrypt_file).place(x=120,y=120)
b_decrypt=Button(root,text="decrypt file",bg='sky blue',fg='black',command=Decrypt_file).place(x=120,y=160)
b_Sendmail=Button(root,text="Send Mail",bg='light green',fg='black',command=Emailing).place(x=120,y=200)
b_Getmail=Button(root,text="Get Mail",bg='light green',fg='black',command=getmail).place(x=120,y=240)
quite_button=Button(root,text="Quit",bg='red',fg='black',command=root.quit).place(x=400,y=350)

Labe_2=Label(root,text="Choose one option below:",fg="Blue").place(x=50,y=100)
root.mainloop()
