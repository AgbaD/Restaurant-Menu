# =============== Restaurant UI.py ============

from tkinter import *
import sys


class Resturant:

    def __init__(self):
        HEIGHT = 750
        WIDTH = 1503

        root = Tk()
        root.title("Restaurant GUI")

        canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg='#696969')
        canvas.pack()

        frame1 = Frame(root)
        frame1.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        label = Label(frame1, text="Fast Food Restaurant", bg="gray", font=40)
        label.place(relwidth=1, relheight=1)

        frame2 = Frame(root, bg="gray")
        frame2.place(relx=0, rely=0.11, relwidth=0.37, relheight=0.9)

        label2 = Label(frame2, text="Fast Food Meal And Vegetarian", bg="gray", font=40)
        label2.place(relwidth=1, relheight=0.07)

        label21 = Label(frame2, text="Fries(1.20$)", bg="gray", font=30)
        label21.place(relx=0.2, rely=0.09, relwidth=0.6, relheight=0.07, anchor="n")

        self.friesvar = IntVar()
        entry21 = Entry(frame2, textvariable=self.friesvar, bg="#A9A9A9")
        entry21.place(relx=0.75, rely=0.09, relwidth=0.2, relheight=0.07, anchor="n")

        label22 = Label(frame2, text="Salad(1.40$)", bg="gray", font=30)
        label22.place(relx=0.2, rely=0.18, relwidth=0.6, relheight=0.07, anchor="n")

        self.saladvar = IntVar()
        entry22 = Entry(frame2, textvariable=self.saladvar, bg="#A9A9A9")
        entry22.place(relx=0.75, rely=0.18, relwidth=0.2, relheight=0.07, anchor="n")

        label23 = Label(frame2, text="Chicken Salad(1.80$)", bg="gray", font=30)
        label23.place(relx=0.25, rely=0.27, relwidth=0.6, relheight=0.07, anchor="n")

        self.chickensaladvar = IntVar()
        entry23 = Entry(frame2, textvariable=self.chickensaladvar, bg="#A9A9A9")
        entry23.place(relx=0.75, rely=0.27, relwidth=0.2, relheight=0.07, anchor="n")

        label24 = Label(frame2, text="Hamburger(2.20$)", bg="gray", font=30)
        label24.place(relx=0.23, rely=0.36, relwidth=0.6, relheight=0.07, anchor="n")

        self.hamburgervar = IntVar()
        entry24 = Entry(frame2, textvariable=self.hamburgervar, bg="#A9A9A9")
        entry24.place(relx=0.75, rely=0.36, relwidth=0.2, relheight=0.07, anchor="n")

        label25 = Label(frame2, text="Onion Rings(1.50$)", bg="gray", font=30)
        label25.place(relx=0.23, rely=0.45, relwidth=0.6, relheight=0.07, anchor="n")

        self.onionringsvar = IntVar()
        entry25 = Entry(frame2, textvariable=self.onionringsvar, bg="#A9A9A9")
        entry25.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.07, anchor="n")

        label26 = Label(frame2, text="Sandwich", bg="gray", font=40)
        label26.place(relx=0.4, rely=0.54, relwidth=1, relheight=0.07, anchor="n")

        label27 = Label(frame2, text="Fish Sandwich(1.80$)", bg="gray", font=30)
        label27.place(relx=0.25, rely=0.63, relwidth=0.6, relheight=0.07, anchor="n")

        self.fsandwichvar = IntVar()
        entry27 = Entry(frame2, textvariable=self.fsandwichvar, bg="#A9A9A9")
        entry27.place(relx=0.75, rely=0.63, relwidth=0.2, relheight=0.07, anchor="n")

        label28 = Label(frame2, text="Cheese Sandwich(1.80$)", bg="gray", font=40)
        label28.place(relx=0.25, rely=0.72, relwidth=0.6, relheight=0.07, anchor="n")

        self.csandwichvar = IntVar()
        entry28 = Entry(frame2, textvariable=self.csandwichvar, bg="#A9A9A9")
        entry28.place(relx=0.75, rely=0.72, relwidth=0.2, relheight=0.07, anchor="n")

        label29 = Label(frame2, text="Chicken Sandwich(1.80$)", bg="gray", font=40)
        label29.place(relx=0.25, rely=0.81, relwidth=0.6, relheight=0.07, anchor="n")

        self.chsandwichvar = IntVar()
        entry29 = Entry(frame2, textvariable=self.chsandwichvar, bg="#A9A9A9")
        entry29.place(relx=0.75, rely=0.81, relwidth=0.2, relheight=0.07, anchor="n")

        frame3 = Frame(root, bg="gray")
        frame3.place(relx=0.375, rely=0.11, relwidth=0.35, relheight=0.5)

        label3 = Label(frame3, text="Desserts", bg="gray", font=40)
        label3.place(relwidth=1, relheight=0.14)

        label31 = Label(frame3, text="Hash Brown(1.80$)", bg="gray", font=40)
        label31.place(relx=0.25, rely=0.16, relwidth=0.6, relheight=0.14, anchor="n")

        self.hashbrownvar = IntVar()
        entry31 = Entry(frame3, textvariable=self.hashbrownvar, bg="#A9A9A9")
        entry31.place(relx=0.75, rely=0.16, relwidth=0.2, relheight=0.14, anchor="n")

        label32 = Label(frame3, text="Toasted Bagel(1.80$)", bg="gray", font=40)
        label32.place(relx=0.25, rely=0.32, relwidth=0.6, relheight=0.14, anchor="n")

        self.toastedbagelvar = IntVar()
        entry32 = Entry(frame3, textvariable=self.toastedbagelvar, bg="#A9A9A9")
        entry32.place(relx=0.75, rely=0.32, relwidth=0.2, relheight=0.14, anchor="n")

        label33 = Label(frame3, text="Pancakes Syrup(1.80$)", bg="gray", font=40)
        label33.place(relx=0.27, rely=0.48, relwidth=0.6, relheight=0.14, anchor="n")

        self.pancakesvar = IntVar()
        entry33 = Entry(frame3, textvariable=self.pancakesvar, bg="#A9A9A9")
        entry33.place(relx=0.75, rely=0.48, relwidth=0.2, relheight=0.14, anchor="n")

        label34 = Label(frame3, text="Pineapple Stick(1.80$)", bg="gray", font=40)
        label34.place(relx=0.27, rely=0.64, relwidth=0.6, relheight=0.14, anchor="n")

        self.pineapplevar = IntVar()
        entry34 = Entry(frame3, textvariable=self.pineapplevar, bg="#A9A9A9")
        entry34.place(relx=0.75, rely=0.64, relwidth=0.2, relheight=0.14, anchor="n")

        label35 = Label(frame3, text="Chocolate Muffin(1.80$)", bg="gray", font=40)
        label35.place(relx=0.27, rely=0.8, relwidth=0.6, relheight=0.14, anchor="n")

        self.chocolatevar = IntVar()
        entry35 = Entry(frame3, textvariable=self.chocolatevar, bg="#A9A9A9")
        entry35.place(relx=0.75, rely=0.8, relwidth=0.2, relheight=0.14, anchor="n")

        frame4 = Frame(root, bg="gray")
        frame4.place(relx=0.73, rely=0.11, relwidth=0.27, relheight=0.89)

        label4 = Label(frame4, text="Drinks", bg="gray", font=40)
        label4.place(relwidth=1, relheight=0.07)

        label41 = Label(frame4, text="Tea(1.80$)", bg="gray", font=40)
        label41.place(relx=0.2, rely=0.09, relwidth=0.6, relheight=0.07, anchor="n")

        self.teavar = IntVar()
        entry41 = Entry(frame4, textvariable=self.teavar, bg="#A9A9A9")
        entry41.place(relx=0.75, rely=0.09, relwidth=0.2, relheight=0.07, anchor="n")

        label42 = Label(frame4, text="Cola(1.80$)", bg="gray", font=30)
        label42.place(relx=0.21, rely=0.18, relwidth=0.6, relheight=0.07, anchor="n")

        self.colavar = IntVar()
        entry42 = Entry(frame4, textvariable=self.colavar, bg="#A9A9A9")
        entry42.place(relx=0.75, rely=0.18, relwidth=0.2, relheight=0.07, anchor="n")

        label43 = Label(frame4, text="Coffee(1.80$)", bg="gray", font=30)
        label43.place(relx=0.23, rely=0.27, relwidth=0.6, relheight=0.07, anchor="n")

        self.coffeevar = IntVar()
        entry43 = Entry(frame4, textvariable=self.coffeevar, bg="#A9A9A9")
        entry43.place(relx=0.75, rely=0.27, relwidth=0.2, relheight=0.07, anchor="n")

        label44 = Label(frame4, text="Orange(1.80$)", bg="gray", font=30)
        label44.place(relx=0.23, rely=0.36, relwidth=0.6, relheight=0.07, anchor="n")

        self.orangevar = IntVar()
        entry44 = Entry(frame4, textvariable=self.orangevar, bg="#A9A9A9")
        entry44.place(relx=0.75, rely=0.36, relwidth=0.2, relheight=0.07, anchor="n")

        label45 = Label(frame4, text="Bottle Water(1.80$)", bg="gray", font=30)
        label45.place(relx=0.27, rely=0.45, relwidth=0.6, relheight=0.07, anchor="n")

        self.bwatervar = IntVar()
        entry45 = Entry(frame4, textvariable=self.bwatervar, bg="#A9A9A9")
        entry45.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.07, anchor="n")

        label46 = Label(frame4, text="Shakes", bg="gray", font=40)
        label46.place(relx=0.4, rely=0.54, relwidth=1, relheight=0.07, anchor="n")

        label47 = Label(frame4, text="Vanilla Cone(1.80$)", bg="gray", font=30)
        label47.place(relx=0.25, rely=0.63, relwidth=0.6, relheight=0.07, anchor="n")

        self.vanillacvar = IntVar()
        entry47 = Entry(frame4, textvariable=self.vanillacvar, bg="#A9A9A9")
        entry47.place(relx=0.75, rely=0.63, relwidth=0.2, relheight=0.07, anchor="n")

        label48 = Label(frame4, text="Vanilla Shakes(1.80$)", bg="gray", font=40)
        label48.place(relx=0.25, rely=0.72, relwidth=0.6, relheight=0.07, anchor="n")

        self.vanillasvar = IntVar()
        entry48 = Entry(frame4, textvariable=self.vanillasvar, bg="#A9A9A9")
        entry48.place(relx=0.75, rely=0.72, relwidth=0.2, relheight=0.07, anchor="n")

        label49 = Label(frame4, text="Strawberry Shakes(1.80$)", bg="gray", font=40)
        label49.place(relx=0.29, rely=0.81, relwidth=0.6, relheight=0.07, anchor="n")

        self.strawberryvar = IntVar()
        entry49 = Entry(frame4, textvariable=self.strawberryvar, bg="#A9A9A9")
        entry49.place(relx=0.75, rely=0.81, relwidth=0.2, relheight=0.07, anchor="n")

        frame5 = Frame(root, bg="gray")
        frame5.place(relx=0.375, rely=0.62, relwidth=0.35, relheight=0.38)

        label5 = Label(frame5, text="Payment", bg="gray", font=40)
        label5.place(relwidth=1, relheight=0.22)

        label51 = Label(frame5, text="Amount", bg="gray", font=40)
        label51.place(relx=0.1, rely=0.24, relwidth=0.25, relheight=0.22, anchor="n")

        self.amountvar = IntVar()
        entry51 = Entry(frame5, textvariable=self.amountvar, bg='#A9A9A9')
        entry51.place(relx=0.36, rely=0.24, relwidth=0.15, relheight=0.2, anchor="n")

        label52 = Label(frame5, text="Total", bg="gray", font=40)
        label52.place(relx=0.57, rely=0.24, relwidth=0.25, relheight=0.22, anchor="n")

        self.label53 = Label(frame5, bg="#A9A9A9")
        self.label53.place(relx=0.8, rely=0.24, relwidth=0.2, relheight=0.22, anchor="n")

        label54 = Label(frame5, text="Change", bg="gray", font=40)
        label54.place(relx=0.57, rely=0.5, relwidth=0.25, relheight=0.22, anchor="n")

        self.label55 = Label(frame5, bg="#A9A9A9")
        self.label55.place(relx=0.8, rely=0.5, relwidth=0.2, relheight=0.22, anchor="n")

        button51 = Button(frame5, text="Display", command=self.processTotal, bg="gray", font=40)
        button51.place(relx=0.16, rely=0.75, relwidth=0.2, relheight=0.22, anchor="n")

        button52 = Button(frame5, text="Change", command=self.genChange, bg="gray", font=40)
        button52.place(relx=0.39, rely=0.75, relwidth=0.2, relheight=0.22, anchor="n")

        button53 = Button(frame5, text="Reset", command=self.reset, bg="gray", font=40)
        button53.place(relx=0.62, rely=0.75, relwidth=0.2, relheight=0.22, anchor="n")

        button54 = Button(frame5, text="Exit", command=self.exit, bg="gray", font=40)
        button54.place(relx=0.85, rely=0.75, relwidth=0.2, relheight=0.22, anchor="n")

        root.mainloop()

    def processTotal(self):
        total = (1.20 * self.friesvar.get()) + (1.40 * self.saladvar.get()) + (1.80 * self.chickensaladvar.get()) \
                + (2.20 * self.hamburgervar.get()) + (1.50 * self.onionringsvar.get()) + (1.80 * self.fsandwichvar.get()) \
                + (1.80 * self.csandwichvar.get()) + (1.80 * self.chsandwichvar.get()) + (1.80 * self.hashbrownvar.get()) \
                + (1.80 * self.toastedbagelvar.get()) + (1.80 * self.pancakesvar.get()) + (1.80 * self.pineapplevar.get()) \
                + (1.80 * self.chocolatevar.get()) + (1.80 * self.teavar.get()) + (1.80 * self.colavar.get()) \
                + (1.80 * self.coffeevar.get()) + (1.80 * self.orangevar.get()) + (1.80 * self.bwatervar.get()) \
                + (1.80 * self.vanillacvar.get()) + (1.80 * self.vanillasvar.get()) + (1.80 * self.strawberryvar.get())

        self.real_total = round((((8 / 100) * total) + total), 2)
        self.label53['text'] = self.real_total

    def genChange(self):
        amount = self.amountvar.get()
        change = round((amount - self.real_total), 2)

        self.label55['text'] = change

    def reset(self):
        self.friesvar.set(0)
        self.saladvar.set(0)
        self.chickensaladvar.set(0)
        self.hamburgervar.set(0)
        self.onionringsvar.set(0)
        self.fsandwichvar.set(0)
        self.csandwichvar.set(0)
        self.chsandwichvar.set(0)
        self.hashbrownvar.set(0)
        self.toastedbagelvar.set(0)
        self.pancakesvar.set(0)
        self.pineapplevar.set(0)
        self.chocolatevar.set(0)
        self.teavar.set(0)
        self.colavar.set(0)
        self.coffeevar.set(0)
        self.orangevar.set(0)
        self.bwatervar.set(0)
        self.vanillacvar.set(0)
        self.vanillasvar.set(0)
        self.strawberryvar.set(0)
        self.amountvar.set(0)

        self.label53['text'] = ""
        self.label55['text'] = ""

    def exit(self):
        sys.exit()


Resturant()
