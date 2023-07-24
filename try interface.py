from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import ttk

entries = Tk()
entries.title("COVID Contact Tracing App")





#FONT
italic_font = font.Font(slant="italic", size=8)
bold_font = font.Font(weight="bold", size=9)
size_entry = font.Font(size=10)
bold_font1 = font.Font(weight="bold", size=9)

#RADIOBUTTON
butt1 = IntVar()
butt2 = IntVar()
butt3 = IntVar()
butt4 = IntVar()
butt5 = IntVar()




# Function to add new entry
def add_entry():
    # def save_entry():
    #     first_name = firstEntry.get()
    #     last_name = lastEntry.get()
    #     phone = numberEntry.get()
    #     email = emailEntry.get()
    #     address = addressEntry.get()
        

    #     if first_name and last_name and phone and email and address:
    #         with open("contacts.txt", "a") as file:
    #             file.write(f"{first_name, last_name},{phone},{date}\n")
    #         messagebox.showinfo("Success", "Entry added successfully.")
    #         entries.destroy()
    #     else:
    #         messagebox.showerror("Error", "Please fill in all the fields.")

    addButton.destroy()
    searchButton.destroy()


    #USERINFO
    userInfo = LabelFrame(entries, text="Person's Information", font=bold_font)
    userInfo.pack()
    # userInfo.place(x="10", y="100", anchor="w")
    
    

    #NAME
    nameLabel = Label(userInfo, text="Name: ", font=bold_font)
    nameLabel.grid(row=1, column=0, padx=20)


    firstLabel = Label(userInfo, text="First Name", font=italic_font)
    firstLabel.grid(row=2, column=1, padx=20)
    lastLabel = Label(userInfo, text="Last Name", font=italic_font)
    lastLabel.grid(row=2, column=2, padx=20)

    firstEntry = Entry(userInfo, width=30, font=size_entry)
    lastEntry = Entry(userInfo, width=30, font=size_entry)
    firstEntry.grid(row=1, column=1, padx=20)
    lastEntry.grid(row=1, column=2, padx=20)

    #PHONE NUMBER AND EMAIL
    phoneNumber = Label(userInfo, text="Phone Number: ", font=bold_font)
    phoneNumber.grid(row=3, column=0, padx=20)
    emailLabel = Label(userInfo, text="Email: ", font=bold_font)
    emailLabel.grid(row=5, column=0, padx=20)

    numberLabel = Label(userInfo, text="                         +63                                                       ", font=italic_font)
    numberLabel.grid(row=4, column=1, padx=20)
    emailSample = Label(userInfo, text="      example@example.com ", font=italic_font)
    emailSample.grid(row=6, column=1, padx=50)
    

    numberEntry = Entry(userInfo, width=60, font=size_entry)
    numberEntry.grid(row=3, column=1, columnspan=2, padx=20)
    emailEntry = Entry(userInfo, width=60, font=size_entry)
    emailEntry.grid(row=5, column=1, columnspan= 2, padx=20)


    #ADDRESS
    addressLabel = Label(userInfo, text="Address: ", font=bold_font)
    addressLabel.grid(row=7, column=0, padx=20)

    addressEntry = Entry(userInfo, width=60, font=size_entry)
    addressEntry.grid(row=7, column=1, columnspan= 2, padx=20)


    #SEX
    sexLabel = Label(userInfo, text="Sex: ", font=bold_font)
    sexLabel.grid(row=10, column=0, padx=20)

    femaleButton = Radiobutton(userInfo, text="Female", variable=butt1, value="1")
    femaleButton.grid(row=10, column=1, padx=20)

    maleButton = Radiobutton(userInfo, text="Male", variable=butt1, value="2")
    maleButton.grid(row=10, column=2, padx=20)

    for widget in userInfo.winfo_children():
            widget.grid_configure(padx=66, pady=2)
    










    ########SURVEY INFO############
    healthInfo = LabelFrame(entries, text="Health Status", font=bold_font)
    healthInfo.pack()

    #COVID VAXX STATS
    ques1Label = Label(healthInfo, text="Have you been vaccinated for COVID-19? ", font=bold_font1)
    ques1Label.grid(row=1, column=0, pady=10)

    yesButton = Radiobutton(healthInfo, text="Yes", variable=butt2, value="1")
    yesButton.grid(row=1, column=1, pady=10)

    noButton = Radiobutton(healthInfo, text="No", variable=butt2, value="2")
    noButton.grid(row=1, column=2, pady=10)

    uncertainButton = Radiobutton(healthInfo, text="Uncertain", variable=butt2, value="3")
    uncertainButton.grid(row=1, column=3, pady=10)

    #SYPMTOMS
    ques2Label = Label(healthInfo, text="Are you experiencing any symptoms in the past 7 days? ", font=bold_font1)
    ques2Label.grid(row=2, column=0, pady=10)

    def symp_indicate():
        sympLabel = Label(healthInfo, text="Indicate symptoms")
        sympLabel.grid(row=3, column=0, pady=10)
        sympEntry = Entry(healthInfo, width=20)
        sympEntry.grid(row=3, column=1, columnspan=2, pady=10)
        return symp_indicate

    yesButton = Radiobutton(healthInfo, text="Yes", variable=butt3, value="1", command=symp_indicate)
    yesButton.grid(row=2, column=1, pady=10)

    noButton = Radiobutton(healthInfo, text="No", variable=butt3, value="2")
    noButton.grid(row=2, column=2, pady=10)

    #CONTACT WITH SAME CASE
    ques3Label = Label(healthInfo, text="Have you had in contact with somebody with body pains, headache, sore throat, fever,", font=bold_font1)
    ques3Label.grid(row=4, column=0)
    ques33Label = Label(healthInfo, text=" diarrhea, cough, colds, shortness of breath, loss of taste, or loss of smell in the past 7 days?", font=bold_font1)
    ques33Label.grid(row=5, column=0, pady=10)

    yesButton = Radiobutton(healthInfo, text="Yes", variable=butt4, value="1")
    yesButton.grid(row=5, column=1, pady=10)

    noButton = Radiobutton(healthInfo, text="No", variable=butt4, value="2")
    noButton.grid(row=5, column=2, pady=10)
    
    #TEST
    ques4Label = Label(healthInfo, text="Have you been tested for Covid-19 in the last 14 days? ", font=bold_font1)
    ques4Label.grid(row=6, column=0, pady=10)

    noButton = Radiobutton(healthInfo, text="No", variable=butt5, value="1")
    noButton.grid(row=6, column=1, pady=10)

    yespButton = Radiobutton(healthInfo, text="Yes-Positive", variable=butt5, value="2")
    yespButton.grid(row=6, column=2, pady=10)

    yesnButton = Radiobutton(healthInfo, text="Yes-Negative", variable=butt5, value="3")
    yesnButton.grid(row=6, column=3, pady=10)

    yeswButton = Radiobutton(healthInfo, text="Yes-Pending", variable=butt5, value="4")
    yeswButton.grid(row=6, column=4, pady=10)


    for widget in healthInfo.winfo_children():
            widget.grid_configure(padx=11)









    ########EMERGENCY CONTACT INFO############
    contactInfo = LabelFrame(entries, text="Emergency Contact Information", font=bold_font)
    contactInfo.pack()

    #NAME
    nameLabel = Label(contactInfo, text="Name: ", font=bold_font)
    nameLabel.grid(row=1, column=0, padx=20)

    firstEntry = Entry(contactInfo, width=60, font=size_entry)
    firstEntry.grid(row=1, column=1, columnspan=2, padx=20)

    #PHONE NUMBER AND EMAIL
    phoneNumber = Label(contactInfo, text="Phone Number: ", font=bold_font)
    phoneNumber.grid(row=3, column=0, padx=20)
    emailLabel = Label(contactInfo, text="Email: ", font=bold_font)
    emailLabel.grid(row=5, column=0, padx=20)


    numberEntry = Entry(contactInfo, width=60, font=size_entry)
    numberEntry.grid(row=3, column=1, columnspan=2, padx=20)
    emailEntry = Entry(contactInfo, width=60, font=size_entry)
    emailEntry.grid(row=5, column=1, columnspan= 2, padx=20)


    #ADDRESS
    addressLabel = Label(contactInfo, text="Address: ", font=bold_font)
    addressLabel.grid(row=7, column=0, padx=20)

    addressEntry = Entry(contactInfo, width=60, font=size_entry)
    addressEntry.grid(row=7, column=1, columnspan= 2, padx=20)

    #RELATIONSHIP
    rsLabel = Label(contactInfo, text="Relationship: ", font=bold_font)
    rsLabel.grid(row=8, column=0, padx=20)

    addressEntry = Entry(contactInfo, width=60, font=size_entry)
    addressEntry.grid(row=8, column=1, columnspan= 2, padx=20)


    for widget in contactInfo.winfo_children():
            widget.grid_configure(padx=113, pady=10)



    ########DATE AND SIG############
    lastInfo = LabelFrame(entries, font=bold_font)
    lastInfo.pack()

    dateLabel = Label(lastInfo, text="Date: ", font=bold_font)
    dateLabel.grid(row=9, column=0, padx=20, pady=5)

    monthCombobox = ttk.Combobox(lastInfo,  values=["January", "February", "March", "April", "May", "June","July","August", "September", "October", "November", "December"])
    monthCombobox.grid(row=9, column=1, padx=20, pady=5)

    dayCombobox = ttk.Combobox(lastInfo,  values=["1", "2", "3", "4", "5", "6","7","8", "9", "10", "11", "12", "13", "14", "15","16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
    dayCombobox.grid(row=9, column=2, padx=20, pady=5)

    yearCombobox = ttk.Combobox(lastInfo,  values=["1980", "1981", "1982","1983", "1984", "1985", "1986","1987","1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995","1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006"])
    yearCombobox.grid(row=9, column=3, padx=20, pady=5)

    monthLabel = Label(lastInfo, text="Month", font=italic_font)
    monthLabel.grid(row=10, column=1, padx=20, pady=5)

    dayLabel = Label(lastInfo, text="Day", font=italic_font)
    dayLabel.grid(row=10, column=2, padx=20, pady=5)

    yearLabel = Label(lastInfo, text="Year", font=italic_font)
    yearLabel.grid(row=10, column=3, padx=20, pady=5)

    sigLine = Label(lastInfo, text="__________________________", font=bold_font)
    sigLine.grid(row=9, column=4, padx=20, pady=5)

    sigLabel = Label(lastInfo, text="Signature", font=italic_font)
    sigLabel.grid(row=10, column=4, padx=20, pady=10)
    
    for widget in lastInfo.winfo_children():
            widget.grid_configure(padx=32, pady=10)


    saveButton = Button(entries, text = "Save", command=add_entry)
    saveButton.pack()



# # Function to search for entry
# def search_entry():
#     def search():
#         search_term = add_entry.get()
#         results.delete(1.0, END)

#         with open("contacts.txt", "r") as file:
#             for line in file:
#                 name, phone, date = line.strip().split(",")
#                 if search_term.lower() in name.lower():
#                     results.insert(END, f"Name: {name}\tPhone: {phone}\tDate: {date}\n")

#     search_window = Toplevel(root)
#     search_window.title("Search Entry")

#     label_search = Label(search_window, text="Search:")
#     label_search.grid(row=0, column=0)
#     entry_search = Entry(search_window)
#     entry_search.grid(row=0, column=1)

#     search_button = Button(search_window, text="Search", command=search)
#     search_button.grid(row=0, column=2)

#     results = Text(search_window, width=50, height=10)
#     results.grid(row=1, column=0, columnspan=3)







addButton = Button(entries, text = "Add Entry", command=add_entry)
addButton.pack()
searchButton = Button(entries, text="Search Entry")
searchButton.pack()


entries.geometry("1000x1000")
entries.mainloop()
