from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root=Tk()
root.title('Country Flags')
root.geometry('600x400')
root.configure(background='lightblue')

get_input = Entry(root)
show_label = Label(root)

indiaImg = ImageTk.PhotoImage(Image.open('Project159+/India.jpg'))
americaImg = ImageTk.PhotoImage(Image.open('Project159+/America.jpg'))
australiaImg = ImageTk.PhotoImage(Image.open('Project159+/Australia.png'))
philippinesImg = ImageTk.PhotoImage(Image.open('Project159+/Japan.jpg'))
japanImg = ImageTk.PhotoImage(Image.open('Project159+/Philippines.png'))

maps_dictionary = { 'India' : indiaImg , 
                    'America' : americaImg ,
                    'Australia' : australiaImg ,
                    'Philippines' : philippinesImg,
                    'Japan' : japanImg,}

def showMaps():
    map_name = get_input.get()
    try:
        show_label['image'] = maps_dictionary[map_name]
    except (KeyError):
        messagebox.showerror('Sorry!', 'That flag is not in our data!')

btn = Button(root , text='Show Map', bg='green', command=showMaps)
get_input.place(relx=0.5, rely=0.1, anchor=CENTER)
btn.place(relx=0.5, rely=0.2, anchor=CENTER)
show_label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()