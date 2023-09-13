class CoffeeMaker():

    def __init__(self):

           self.milk=0
           self.coffee=0
           self.sugar=0
           self.tea=0
           self.repeat=True
           while self.repeat is True:
                self.menu()

    def menu(self):

        a= int(input('''
                What would you like to have?
                1. Coffee 
                2. Tea
                3. Refill the resources    
                4. Power off the machine
        '''))
        if a==1:
            self.make_coffee()
        elif a==2:
            self.make_tea()
        elif a==3:
            self.refil()
        elif a==4:
            self.repeat= False
        else:
            print('Invalid Input')
    def make_coffee(self):

        size=int(input('''
                How much coffee do you want?
                1. 25ml
                2. 50ml
         '''))
        if size==1:
            if self.milk>=25 and self.coffee>=10:
                self.milk=self.milk - 25
                self.coffee=self.coffee - 10
                sugar1=int(input('''
                                Do you want to add sugar?
                                1. yes
                                2. No
                                '''))
                if sugar1==1:
                    if self.sugar>=10:
                        self.sugar=self.sugar-10
                    else:
                        print("Sorry, insufficient sugar.")
                print("Here is your coffee !!")
            else:
                print("Sorry, insufficient resources.")

        elif size == 2:
            if self.milk >= 50 and self.coffee >= 20:
                self.milk = self.milk - 50
                self.coffee = self.coffee - 20
                sugar1 = int(input('''
                                Do you want to add sugar?
                                1. yes
                                2. No
                                '''))
                if sugar1 == 1:
                    if self.sugar >= 20:
                        self.sugar = self.sugar - 20
                    else:
                        print("Sorry, insufficient sugar.")
                print("Here is your coffee !!")
            else:
                print("Sorry, insufficient resources.")
        else:
            print("invalid input")
    def make_tea(self):

        size=int(input('''
                How much tea do you want?
                1. 25ml
                2. 50ml
         '''))
        if size==1:
            if self.milk>=25 and self.tea>=10:
                self.milk=self.milk - 25
                self.tea=self.tea - 10
                sugar1=int(input('''Do you want to add sugar?
                                1. yes
                                2. No
                                '''))
                if sugar1==1:
                    if self.sugar>=10:
                        self.sugar=self.sugar-10
                    else:
                        print("Sorry, insufficient sugar.")
                print("Here is your tea !!")
            else:
                print("Sorry, insufficient resources.")

        elif size == 2:
            if self.milk >= 50 and self.tea >= 20:
                self.milk = self.milk - 50
                self.tea = self.tea - 20
                sugar1 = int(input('''Do you want to add sugar?
                                1. yes
                                2. No
                                '''))
                if sugar1 == 1:
                    if self.sugar >= 20:
                        self.sugar = self.sugar - 20
                    else:
                        print("Sorry, insufficient sugar.")
                print("Here is your coffee !!")
            else:
                print("Sorry, insufficient resources.")
        else:
            print("invalid input")
    def refil(self):
        print(f'''  The resources 
                    Milk: {self.milk} ml
                    Sugar:{self.sugar} gm
                    Tea:{self.tea} gm
                    Coffee: {self.coffee} gm
                ''')
        refil1= int(input('''
                    Do you want to refil the resources?
                    1. Yes
                    2. No
                             '''))
        if refil1==1:
            sugar_add=int(input("Amount of sugar to be added:"))
            self.sugar+=sugar_add
            tea_add = int(input("Amount of tea to be added:"))
            self.tea += tea_add
            milk_add = int(input("Amount of milk to be added:"))
            self.milk += milk_add
            coffee_add = int(input("Amount of coffee to be added:"))
            self.coffee += coffee_add
            print(f'''         Updated resources 
                               Milk: {self.milk} ml
                               Sugar:{self.sugar} gm
                               Tea:{self.tea} gm
                               Coffee: {self.coffee} gm
                           ''')
        elif refil1==2:
            print("OK! Thank You!!")
        else:
            print("Invalid input!!")

nesscaffe=CoffeeMaker()
