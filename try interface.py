from tkinter import *
from tkinter import messagebox
from tkinter import font


entries = Tk()
entries.title("COVID Contact Tracing App")


frame = Frame(entries)
frame.pack()


#FONT
italic_font = font.Font(slant="italic", size=8)
bold_font = font.Font(weight="bold", size=9)

# Function to add new entry
def add_entry():
    # def save_entry():
    #     first_name = firstEntry.get()
    #     last_name = lastEntry.get()
    #     phone = numberEntry.get()
    #     email = emailEntry.get()

    #     if first_name and last_name and phone and email:
    #         with open("contacts.txt", "a") as file:
    #             file.write(f"{name},{phone},{date}\n")
    #         messagebox.showinfo("Success", "Entry added successfully.")
    #         add_window.destroy()
    #     else:
    #         messagebox.showerror("Error", "Please fill in all the fields.")



    #USERINFO
    userInfo = LabelFrame(frame, text="Person's Information")
    userInfo.grid(row=0, column=0, padx=20, pady=20)

    #NAME
    nameLabel = Label(userInfo, text="Name: ", font=bold_font)
    nameLabel.grid(row=1, column=0, padx=10)


    firstLabel = Label(userInfo, text="First Name", font=italic_font)
    firstLabel.grid(row=2, column=1)
    lastLabel = Label(userInfo, text="Last Name", font=italic_font)
    lastLabel.grid(row=2, column=2)

    firstEntry = Entry(userInfo, width=20)
    lastEntry = Entry(userInfo, width=20)
    firstEntry.grid(row=1, column=1, padx=10)
    lastEntry.grid(row=1, column=2, padx=10)

    #PHONE NUMBER AND EMAIL
    phoneNumber = Label(userInfo, text="Phone Number: ", font=bold_font)
    phoneNumber.grid(row=3, column=0, padx=10)
    emailLabel = Label(userInfo, text="Email: ", font=bold_font)
    emailLabel.grid(row=5, column=0, padx=10)

    numberLabel = Label(userInfo, text="+63                                         ", font=italic_font)
    numberLabel.grid(row=4, column=1)
    emailSample = Label(userInfo, text="example@example.com     ", font=italic_font)
    emailSample.grid(row=6, column=1)
    

    numberEntry = Entry(userInfo, width=50)
    numberEntry.grid(row=3, column=1, columnspan=2, padx=10)
    emailEntry = Entry(userInfo, width=50)
    emailEntry.grid(row=5, column=1, columnspan= 2, padx=10)




# # Function to search for entry
# def search_entry():
#     def search():
#         search_term = entry_search.get()
#         results.delete(1.0, tk.END)

#         with open("contacts.txt", "r") as file:
#             for line in file:
#                 name, phone, date = line.strip().split(",")
#                 if search_term.lower() in name.lower():
#                     results.insert(tk.END, f"Name: {name}\tPhone: {phone}\tDate: {date}\n")

#     search_window = tk.Toplevel(root)
#     search_window.title("Search Entry")

#     label_search = tk.Label(search_window, text="Search:")
#     label_search.grid(row=0, column=0)
#     entry_search = tk.Entry(search_window)
#     entry_search.grid(row=0, column=1)

#     search_button = tk.Button(search_window, text="Search", command=search)
#     search_button.grid(row=0, column=2)

#     results = tk.Text(search_window, width=50, height=10)
#     results.grid(row=1, column=0, columnspan=3)


addButton = Button(entries, text = "Add Entry", command=add_entry)
addButton.pack()
searchButton = Button(entries, text="Search Entry")
searchButton.pack()

entries.geometry("500x500")
entries.mainloop()
