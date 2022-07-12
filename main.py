from tkinter import *

import sqlite3

root = Tk()
root.title("Програма за задължения")

root.geometry("1220x800")

# Database

# Create a database or connect to one
conn = sqlite3.connect('Zadalzhenia.db')

# Create cursor
c = conn.cursor()

# Create table


c.execute("""CREATE TABLE IF NOT EXISTS zadalzhenia(
        name_of_firm text,
        number_of_facture text,
        date text,
        sum text,
        what_buy text,
        what_buy_count text,
        date_of_zapis text
        )""")


# Create a Function for delete a record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('Zadalzhenia.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from zadalzhenia WHERE oid= " + delete_box.get())

    # Commit-Changes
    conn.commit()

    # Close-Connectio-
    conn.close()


# Create Submit Function For database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('Zadalzhenia.db')
    # Create cursor
    c = conn.cursor()

    # Insert Into Table
    c.execute("INSERT INTO  zadalzhenia VALUES (:n_o_f, :num_o_f, :date, :sum, :w_b, :w_b_c, :d_o_z)",
              {
                  'n_o_f': name_of_firm.get(),
                  'num_o_f': number_of_facture.get(),
                  'date': date.get(),
                  'sum': sum.get(),
                  'w_b': what_buy.get(),
                  'w_b_c': what_buy_count.get(),
                  'd_o_z': date_of_zapis.get()
              })

    # Commit-Changes
    conn.commit()

    # Close-Connectio-
    conn.close()

    # Clear The Text Boxes
    name_of_firm.delete(0, END)
    number_of_facture.delete(0, END)
    date.delete(0, END)
    sum.delete(0, END)
    what_buy.delete(0, END)
    what_buy_count.delete(0, END)
    date_of_zapis.delete(0, END)



# Create text boxes
name_of_firm = Entry(root, width=30)
name_of_firm .grid(row=0, column=1, padx=20, pady=(10, 0))
number_of_facture = Entry(root, width=30)
number_of_facture .grid(row=1, column=1, padx=20, pady=(10, 0))
date = Entry(root, width=30)
date.grid(row=2, column=1, padx=20, pady=(10, 0))
sum = Entry(root, width=30)
sum.grid(row=3, column=1, padx=20, pady=(10, 0))
what_buy = Entry(root, width=30)
what_buy.grid(row=4, column=1, padx=20, pady=(10, 0))
what_buy_count = Entry(root, width=30)
what_buy_count.grid(row=5, column=1, pady=(10, 0))
date_of_zapis = Entry(root, width=30)
date_of_zapis.grid(row=6, column=1, pady=(10, 0))
delete_box = Entry(root, width=30)
delete_box.grid(row=11, column=1, pady=5)

# Create text box Labels
name_of_firm_label = Label(root, text="Въведете името на фирмата от, когото е издадена фактурата")
name_of_firm_label.grid(row=0, column=0)
number_of_facture_label = Label(root, text="Въведете номера на фактурата")
number_of_facture_label.grid(row=1, column=0)
date_label = Label(root, text="Въведете датата от фактурата")
date_label.grid(row=2, column=0)
sum_label = Label(root, text="Въведете сумата с ДДС от фактурата")
sum_label.grid(row=3, column=0)
what_buy_label = Label(root, text="Въведете какво сте закупили")
what_buy_label.grid(row=4, column=0)
what_buy_count_label = Label(root, text="Въведете броя на нещата, които сте закупили")
what_buy_count_label.grid(row=5, column=0)
date_of_zapis_label = Label(root, text="Въведете днешната дата")
date_of_zapis_label.grid(row=6, column=0)
delete_box_label = Label(root, text="Изтрий задължение по номер")
delete_box_label.grid(row=11, column=0)



# Create Submit Button
submit_btn = Button(root, text="Натиснете за да запишете задължението", command=submit)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


root.mainloop()
