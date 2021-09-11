from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk,Image
from pytube import YouTube

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#donwload video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!",fg="red")


    #download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")



root = Tk()
root.title("YTD Downloader")
root.geometry("450x400") #set window
root.resizable(0,0)
root.columnconfigure(0,weight=1)#set all content in center.
# img = ImageTk.PhotoImage(Image.open(r"D:\crome downloads\music\732269.jpg"))
c1 = Canvas(root, width=400,height=400)
c1.pack(fill="both", expand=True)
# c1.create_image(0, 0, image=img,anchor="nw")

#Ytd Link Label
c1.create_text( 240, 60, text = "Enter the URL of the Video",font=('Arial',15))
#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar,bg='#CFE2F1')
ytdEntry.place(x=100,y=80)

#path-----------------
ytdError = Label(root,text="Downloading!!!",fg="red",font=('Palatino',10),bg="#CFE2F1")
ytdError.place(x=190,y=330)

#Asking save file label
c1.create_text( 240, 130, text = "Save the Video File",font=('Arial',15))


#btn of save file
saveEntry = Button(root,width=10,bg="Grey",fg="white",text="Choose Path",command=openLocation)
saveEntry.place(x=200,y=160)

#Error Msg location
locationError = Label(root,text="Path",fg="red",font=('Palatino',8),bg="#CFE2F1")
locationError.place(x=230,y=205)

#Download Quality
# ytdQuality = Label(root,text="Select Quality",font=('Palatino',15),bg="#CFE2F1")
# ytdQuality.place(x=200,y=230)
c1.create_text( 240, 240, text = "Select Quality",font=('Arial',15))

#combobox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.place(x=165,y=260)

#donwload btn
downloadbtn = Button(root,text="Donwload",width=10,bg="green",fg="white",command=DownloadVideo)
downloadbtn.place(x=195,y=290)

#Project label
developerlabel = Label(root,text="Python Project",font=('Palatino',15),bg="#CFE2F1")
# developerlabel.grid()
root.mainloop()