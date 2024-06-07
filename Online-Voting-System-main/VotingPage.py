import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image

def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode()) #4

    message = client_socket.recv(1024) #Success message
    print(message.decode()) #5
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)

    client_socket.close()



def votingPg(root,frame1,client_socket):

    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Vote", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "BJP\n\nNarendra Modi", variable = vote, value = "bjp", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"bjp",client_socket)).grid(row = 2,column = 1)
    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((45,45),Image.BILINEAR))
    bjpImg = Label(frame1, image=bjpLogo).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "Congress\n\nRahul Gandhi", variable = vote, value = "cong", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"cong",client_socket)).grid(row = 3,column = 1)
    congLogo = ImageTk.PhotoImage((Image.open("img/cong.jpg")).resize((35,48),Image.BILINEAR))
    congImg = Label(frame1, image=congLogo).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "Jana sena party\n\npawan kalyan", variable = vote, value = "jsp", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"jsp",client_socket) ).grid(row = 4,column = 1)
    jspLogo = ImageTk.PhotoImage((Image.open("img/jsp.png")).resize((55,40),Image.BILINEAR))
    jspImg = Label(frame1, image=jspLogo).grid(row = 4,column = 0)

    Radiobutton(frame1, text = "YCP\n\njagan", variable = vote, value = "ycp", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"ycp",client_socket)).grid(row = 5,column = 1)
    ycpLogo = ImageTk.PhotoImage((Image.open("img/ycp.png")).resize((50,45),Image.BILINEAR))
    ycpImg = Label(frame1, image=ycpLogo).grid(row = 5,column = 0)

    Radiobutton(frame1, text = "\nNOTA    \n  ", variable = vote, value = "nota", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"nota",client_socket)).grid(row = 6,column = 1)
    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.jpg")).resize((45,35),Image.BILINEAR))
    notaImg = Label(frame1, image=notaLogo).grid(row = 6,column = 0)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         client_socket='Fail'
#         votingPg(root,frame1,client_socket)
