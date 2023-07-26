from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import ttk
  

entries = Tk()
entries.title("COVID Contact Tracing App")


#FONT
italic_font = ("Century Gothic", 8, "italic")
bold_font = ("Century Gothic", 8, "bold")
size_entry = ("Century Gothic", 9)
bold_font1 = ("Century Gothic", 8, "bold")
title_font = ("Century Gothic", 20, "bold")
title_font1 = ("Century Gothic", 15, "bold")
message_font = ("Century Gothic", 10)


#RADIOBUTTONS
butt1 = IntVar()
butt2 = IntVar()
butt3 = IntVar()
butt4 = IntVar()
butt5 = IntVar()
butt6 = IntVar()




# FUNCTION TO ADD ENTRY
def add_entry():
    def save_entry():
        first_name = firstEntry.get()
        last_name = lastEntry.get()
        phone = numberEntry.get()
        email = emailEntry.get()
        address = addressEntry.get()
        

        if first_name and last_name and phone and email and address:
            with open("saved infos.csv", "a") as file:
                file.write(f"{first_name}:{last_name}:{phone}:{email}:{address}\n")
            messagebox.showinfo("Success", "Entry added successfully.")
            return entries.mainloop()
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")

    add_window = Toplevel(entries)
    add_window.title("Add New Entry")
    add_window.geometry("1000x1000")
    add_window['background']='#c8c9c9'





    #USERINFO
    userInfo = LabelFrame(add_window, text="Person's Information", font=bold_font)
    userInfo.pack()
    userInfo['background']='#c8c9c9'


    #NAME
    nameLabel = Label(userInfo, text="Name: ", font=bold_font)
    nameLabel.grid(row=1, column=0, padx=20)
    nameLabel['background']='#c8c9c9'


    firstLabel = Label(userInfo, text="First Name", font=italic_font)
    firstLabel.grid(row=2, column=1, padx=20)
    firstLabel['background']='#c8c9c9'
    lastLabel = Label(userInfo, text="Last Name", font=italic_font)
    lastLabel.grid(row=2, column=2, padx=20)
    lastLabel['background']='#c8c9c9'


    firstEntry = Entry(userInfo, width=30, font=size_entry)
    lastEntry = Entry(userInfo, width=30, font=size_entry)
    firstEntry.grid(row=1, column=1, padx=20)
    lastEntry.grid(row=1, column=2, padx=20)

    #PHONE NUMBER AND EMAIL
    phoneNumber = Label(userInfo, text="Phone Number: ", font=bold_font)
    phoneNumber.grid(row=3, column=0, padx=20)
    phoneNumber['background']='#c8c9c9'
    emailLabel = Label(userInfo, text="Email: ", font=bold_font)
    emailLabel.grid(row=5, column=0, padx=20)
    emailLabel['background']='#c8c9c9'

    numberLabel = Label(userInfo, text="                         +63                                                       ", font=italic_font)
    numberLabel.grid(row=4, column=1, padx=20)
    numberLabel['background']='#c8c9c9'
    emailSample = Label(userInfo, text="      example@example.com ", font=italic_font)
    emailSample.grid(row=6, column=1, padx=50)
    emailSample['background']='#c8c9c9'
    

    numberEntry = Entry(userInfo, width=60, font=size_entry)
    numberEntry.grid(row=3, column=1, columnspan=2, padx=20)
    emailEntry = Entry(userInfo, width=60, font=size_entry)
    emailEntry.grid(row=5, column=1, columnspan= 2, padx=20)


    #ADDRESS
    addressLabel = Label(userInfo, text="Address: ", font=bold_font)
    addressLabel.grid(row=7, column=0, padx=20)
    addressLabel['background']='#c8c9c9'

    addressEntry = Entry(userInfo, width=60, font=size_entry)
    addressEntry.grid(row=7, column=1, columnspan= 2, padx=20)


    #SEX
    sexLabel = Label(userInfo, text="Sex: ", font=bold_font)
    sexLabel.grid(row=10, column=0, padx=20)
    sexLabel['background']='#c8c9c9'

    femaleButton = Radiobutton(userInfo, text="Female", variable=butt1, value="1")
    femaleButton.grid(row=10, column=1, padx=20)
    femaleButton['background']='#c8c9c9'

    maleButton = Radiobutton(userInfo, text="Male", variable=butt1, value="2")
    maleButton.grid(row=10, column=2, padx=20)
    maleButton['background']='#c8c9c9'

    for widget in userInfo.winfo_children():
            widget.grid_configure(padx=66, pady=2)





    ########SURVEY INFO############
    healthInfo = LabelFrame(add_window, text="Health Status", font=bold_font)
    healthInfo.pack()
    healthInfo['background']='#c8c9c9'

    #COVID VAXX STATS
    ques1Label = Label(healthInfo, text="-  Have you been vaccinated for COVID-19? ", font=bold_font1)
    ques1Label.grid(row=1, column=0, pady=10)
    ques1Label['background']='#c8c9c9'

    yesButton = Radiobutton(healthInfo, text="Yes", variable=butt2, value="1")
    yesButton.grid(row=1, column=1, pady=10)
    yesButton['background']='#c8c9c9'

    noButton = Radiobutton(healthInfo, text="No", variable=butt2, value="2")
    noButton.grid(row=1, column=2, pady=10)
    noButton['background']='#c8c9c9'

    uncertainButton = Radiobutton(healthInfo, text="Uncertain", variable=butt2, value="3")
    uncertainButton.grid(row=1, column=3, pady=10)
    uncertainButton['background']='#c8c9c9'

    #SYPMTOMS
    ques2Label = Label(healthInfo, text="-  Are you experiencing any symptoms in the past 7 days? ", font=bold_font1)
    ques2Label.grid(row=2, column=0, pady=10)
    ques2Label['background']='#c8c9c9'

    def symp_indicate():
        sympLabel = Label(healthInfo, text="Indicate symptoms")
        sympLabel.grid(row=3, column=0, pady=10)
        sympLabel['background']='#c8c9c9'
        sympEntry = Entry(healthInfo, width=20)
        sympEntry.grid(row=3, column=1, columnspan=2, pady=10)
        return symp_indicate

    yesButton = Radiobutton(healthInfo, text="Yes", variable=butt3, value="1", command=symp_indicate)
    yesButton.grid(row=2, column=1, pady=10)
    yesButton['background']='#c8c9c9'

    noButton = Radiobutton(healthInfo, text="No", variable=butt3, value="2")
    noButton.grid(row=2, column=2, pady=10)
    noButton['background']='#c8c9c9'

    #CONTACT WITH SAME CASE
    ques3Label = Label(healthInfo, text="-  Have you had in contact with somebody with body pains, headache, sore throat, fever,", font=bold_font1)
    ques3Label.grid(row=4, column=0)
    ques3Label['background']='#c8c9c9'
    ques33Label = Label(healthInfo, text=" diarrhea, cough, colds, shortness of breath, loss of taste, or loss of smell in the past 7 days?", font=bold_font1)
    ques33Label.grid(row=5, column=0, pady=10)
    ques33Label['background']='#c8c9c9'

    yesButton = Radiobutton(healthInfo, text="Yes", variable=butt4, value="1")
    yesButton.grid(row=5, column=1, pady=10)
    yesButton['background']='#c8c9c9'

    noButton = Radiobutton(healthInfo, text="No", variable=butt4, value="2")
    noButton.grid(row=5, column=2, pady=10)
    noButton['background']='#c8c9c9'
    
    #TEST
    ques4Label = Label(healthInfo, text="-  Have you been tested for Covid-19 in the last 14 days? ", font=bold_font1)
    ques4Label.grid(row=6, column=0, pady=10)
    ques4Label['background']='#c8c9c9'

    noButton = Radiobutton(healthInfo, text="No", variable=butt5, value="1")
    noButton.grid(row=6, column=1, pady=10)
    noButton['background']='#c8c9c9'

    yespButton = Radiobutton(healthInfo, text="Yes-Positive", variable=butt5, value="2")
    yespButton.grid(row=6, column=2, pady=10)
    yespButton['background']='#c8c9c9'

    yesnButton = Radiobutton(healthInfo, text="Yes-Negative", variable=butt5, value="3")
    yesnButton.grid(row=6, column=3, pady=10)
    yesnButton['background']='#c8c9c9'

    yeswButton = Radiobutton(healthInfo, text="Yes-Pending", variable=butt5, value="4")
    yeswButton.grid(row=6, column=4, pady=10)
    yeswButton['background']='#c8c9c9'


    for widget in healthInfo.winfo_children():
            widget.grid_configure(padx=11)





    ########EMERGENCY CONTACT INFO############
    contactInfo = LabelFrame(add_window, text="Emergency Contact Information", font=bold_font)
    contactInfo.pack()
    contactInfo['background']='#c8c9c9'

    #NAME
    contactnameLabel = Label(contactInfo, text="Name: ", font=bold_font)
    contactnameLabel.grid(row=1, column=0, padx=20)
    contactnameLabel['background']='#c8c9c9'

    contactfirstEntry = Entry(contactInfo, width=60, font=size_entry)
    contactfirstEntry.grid(row=1, column=1, columnspan=2, padx=20)

    #PHONE NUMBER AND EMAIL
    contactphoneNumber = Label(contactInfo, text="Phone Number: ", font=bold_font)
    contactphoneNumber.grid(row=3, column=0, padx=20)
    contactphoneNumber['background']='#c8c9c9'
    contactemailLabel = Label(contactInfo, text="Email: ", font=bold_font)
    contactemailLabel.grid(row=5, column=0, padx=20)
    contactemailLabel['background']='#c8c9c9'


    contactnumberEntry = Entry(contactInfo, width=60, font=size_entry)
    contactnumberEntry.grid(row=3, column=1, columnspan=2, padx=20)
    contactemailEntry = Entry(contactInfo, width=60, font=size_entry)
    contactemailEntry.grid(row=5, column=1, columnspan= 2, padx=20)


    #ADDRESS
    contactaddressLabel = Label(contactInfo, text="Address: ", font=bold_font)
    contactaddressLabel.grid(row=7, column=0, padx=20)
    contactaddressLabel['background']='#c8c9c9'

    contactaddressEntry = Entry(contactInfo, width=60, font=size_entry)
    contactaddressEntry.grid(row=7, column=1, columnspan= 2, padx=20)

    #RELATIONSHIP
    contactrsLabel = Label(contactInfo, text="Relationship: ", font=bold_font)
    contactrsLabel.grid(row=8, column=0, padx=20)
    contactrsLabel['background']='#c8c9c9'

    contactaddressEntry = Entry(contactInfo, width=60, font=size_entry)
    contactaddressEntry.grid(row=8, column=1, columnspan= 2, padx=20)


    for widget in contactInfo.winfo_children():
            widget.grid_configure(padx=113, pady=10)





    ########DATE AND SIG############
    lastInfo = LabelFrame(add_window, font=bold_font)
    lastInfo.pack()
    lastInfo['background']='#c8c9c9'

    dateLabel = Label(lastInfo, text="Date: ", font=bold_font)
    dateLabel.grid(row=9, column=0, padx=20)
    dateLabel['background']='#c8c9c9'

    monthCombobox = ttk.Combobox(lastInfo,  values=["January", "February", "March", "April", "May", "June","July","August", "September", "October", "November", "December"])
    monthCombobox.grid(row=9, column=1, padx=20)

    dayCombobox = ttk.Combobox(lastInfo,  values=["1", "2", "3", "4", "5", "6","7","8", "9", "10", "11", "12", "13", "14", "15","16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
    dayCombobox.grid(row=9, column=2, padx=20)

    yearCombobox = ttk.Combobox(lastInfo,  values=["2021", "2022", "2023", "2024", "2025", "2026"])
    yearCombobox.grid(row=9, column=3, padx=20)

    monthLabel = Label(lastInfo, text="Month", font=italic_font)
    monthLabel.grid(row=10, column=1, padx=20)
    monthLabel['background']='#c8c9c9'

    dayLabel = Label(lastInfo, text="Day", font=italic_font)
    dayLabel.grid(row=10, column=2, padx=20)
    dayLabel['background']='#c8c9c9'

    yearLabel = Label(lastInfo, text="Year", font=italic_font)
    yearLabel.grid(row=10, column=3, padx=20)
    yearLabel['background']='#c8c9c9'

    agreeButton = Checkbutton(lastInfo, text="")
    agreeButton.grid(row=9, column=4, padx=20)
    agreeButton['background']='#c8c9c9'

    sigLabel = Label(lastInfo, text="I agree that the informations are all true.", font=italic_font)
    sigLabel.grid(row=10, column=4, padx=20)
    sigLabel['background']='#c8c9c9'
    
    for widget in lastInfo.winfo_children():
            widget.grid_configure(padx=30.4)





    ########SAVE AND BACK############
    buttonInfo = LabelFrame(add_window, font=bold_font)
    buttonInfo.pack()

    saveButton = Button(buttonInfo, text = "Save", fg="white", bg="blue", font="time 10 bold", command=save_entry)
    saveButton.grid(row=11, column=1)

    backButton = Button(buttonInfo, text = "Back", fg="white", bg="red", font="time 10 bold", command=add_window.destroy)
    backButton.grid(row=11, column=2)











# FUNCTION TO SEARCH ENTRY
def search_entry():
    def search():
        search_term = searchEntry.get()
        results.delete(1.0, END)

        with open("saved infos.csv", "r") as file:
            for line in file:
                first_name, last_name, phone, email, address = line.strip().split(":")
                if search_term.lower() in first_name.lower():
                    results.insert(END, f" Name: {first_name} {last_name}\n Phone Number: {phone}\n Email: {email}\n Address: {address}\n")


    search_window = Toplevel(entries)
    search_window.title("Search Entry")
    search_window.geometry("1000x1000")
    search_window['background']='#c8c9c9'


    searchInfo = LabelFrame(search_window, font=bold_font)
    searchInfo.pack()
    searchInfo['background']='#c8c9c9'

    searchLabel = Label(searchInfo, text="Search Name:", font=bold_font)
    searchLabel.grid(row=0, column=0, padx=20, pady=20)
    searchLabel['background']='#c8c9c9'
    searchEntry = Entry(searchInfo, width=50, font=size_entry)
    searchEntry.grid(row=0, column=1, padx=20, pady=20)

    searchButt = Button(searchInfo, text="Search", fg="white", bg="green", font="time 10 bold", command=search)
    searchButt.grid(row=0, column=2, padx=20, pady=20)

    results = Text(searchInfo, width=70, height=10, font=size_entry)
    results.grid(row=1, column=0, columnspan=3, padx=20, pady=20)

    backButton = Button(searchInfo, text = "Back", fg="white", bg="red", font="time 10 bold", command=search_window.destroy)
    backButton.grid(row=3, column=1)

#FIRST WIDGETS IN OPENING THE APP
titleLabel = Label(entries, text="Contact Tracing", font=title_font)
titleLabel.grid(padx=50, pady=20)
titleLabel['background']='#c8c9c9'

message = Label(entries, text="If you are either diagnosed with Coronavirus or experiencing Coronavirus symptoms, please provide us with your contact information", font=message_font) 
message1 = Label(entries, text="and select your neighbourhood and work address from the map. ", font=message_font)    
message2 = Label(entries, text="Please list out the people who you regularly contact or have been contacted during the last 14-days period for each. ", font=message_font)    
message3 = Label(entries, text="If you have been in other public or crowded locations during this period, please specify and also list out people that you have contacted.", font=message_font)
message.grid(padx=50)
message['background']='#c8c9c9'   
message1.grid(padx=50)
message1['background']='#c8c9c9'  
message2.grid(padx=50)
message2['background']='#c8c9c9'           
message3.grid(padx=50)
message3['background']='#c8c9c9'   

title2Label = Label(entries, text="Please fill out your infos here:", font=title_font1)
title2Label.grid(padx=50)
title2Label['background']='#c8c9c9'

addButton = Button(entries, text = "Add Entry", fg="white", bg="blue", font="time 10 bold", width=10, height=2, command=add_entry)
addButton.grid(padx=50, pady=20)

title3Label = Label(entries, text="Search entries here:", font=title_font1)
title3Label.grid(padx=50)
title3Label['background']='#c8c9c9'

searchButton = Button(entries, text="Search Entry", fg="white", bg="green", font="time 10 bold", width=10, height=2, command=search_entry)
searchButton.grid(padx=50, pady=20)





entries['background']='#c8c9c9'
entries.geometry("1000x1000")
entries.mainloop()
