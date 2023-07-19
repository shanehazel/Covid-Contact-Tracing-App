from tkinter import *




window = Tk()
window.title("COVID Contact Tracing App")


frame = Frame(window)
frame.pack()

userInfo = LabelFrame(frame, text="Person's Information")
userInfo.grid(row=0, column=0, padx=20, pady=20)

nameLabel = Label(userInfo, text="Enter Name: ")
nameLabel.grid(row=2, column=0, padx=10,pady=10)

firstName = Label(userInfo, text="First Name")
firstName.grid(row=1, column=1, padx=10, pady=10)
lastName = Label(userInfo, text="Last Name")
lastName.grid(row=1, column=2, padx=10, pady=10)

firstEntry = Entry(userInfo)
lastEntry = Entry(userInfo)
firstEntry.grid(row=2, column=1, padx=10, pady=10)
lastEntry.grid(row=2, column=2, padx=10, pady=10)


window.geometry("500x500")
window.mainloop()

