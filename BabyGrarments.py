import tkinter as tk
from tkinter import *
from tkinter import Button
import add_to_db
import updatestock



import point_of_sale
import searchstock
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL

class Dashboard:
    def __init__(self, master):
        self.master = master
 
        master.title("Baby Garments & Shoes Piplan")
        
        # Set background color
        master.configure(bg="skyblue")  # You can use any hexadecimal color code or a color name

        # Set geometry
        # master.geometry("800x100")  # Adjust the size as needed

        # Add a label for the title
        # title_label = tk.Label(master, text="BABY GARMENTS & SHOES", font=("Arial", 40), bg="green", fg="white")
        # title_label.pack(pady=10)

        dashboard_label = tk.Label(master, text="DASHBOARD", font=("arial 40 bold"), bg="green", fg="white")
        dashboard_label.pack(pady=20)

        # Create buttons with colors
        self.add_button = Button(master, text="Add Product",font=("arial 15 bold"), command=self.open_add_to_db,height=2, bg="orange", fg="white",width=14)
        self.add_button.place(x=10,y=150)

        self.update_button = Button(master, text="Update Product",font=("arial 15 bold"), command=self.open_update_database,height=2, bg="purple", fg="white",width=14)
        self.update_button.place(x=200,y=150)

        self.point_of_sale = Button(master, text="Sale Point",font=("arial 25 bold"), command=self.point_of_sale, bg="green", fg="white",height=2, width=18)
        self.point_of_sale.place(x=10,y=240)

        self.viewstock = Button(master, text="View Stock",font=("arial 15 bold"), command=self.search_stock, bg="blue", fg="white", width=18,height=2)
        self.viewstock.place(x=100,y=370)

        # self.check = Button(master, text="View Stock",font=("arial 15 bold"), command=self.checkup1, bg="blue", fg="white", )
        # self.check.place(x=0,y=370)


    def open_add_to_db(self):
        add_to_db.main()
    def open_update_database(self):
        updatestock.main()


    def point_of_sale(self):
        point_of_sale.main()

    def search_stock(self):
        searchstock.main()

    # def checkup1(self):
    #     checkup.main()



def main():
    root = tk.Tk()
    app = Dashboard(root)
    root.geometry("400x450+0+0")
    root.mainloop()

if __name__ == "__main__":
    main()