# --------------------------------- User ---------------------------------- #
class Food_Ordering_App:
    def __init__ (self):
        self.order={}
        self.order_id=len(self.order)+1
        self.personal_detail={}
    

    def register_user(self):
        print("\n__________Welcome to B.B.C good food!!!__________")
        print('\n****** Regiteration ******')
        self.Name      = input("Enter your Full Name: ")
        self.Mobile_no = int(input("Enter your Mobile no : "))
        self.Email     =  input("Enter your Email : ")
        self.Address   = input("Enter your Address : ")
        self.Password  = input("Enter any strong Password : ")
        self.items1    = {"full_name" : self.Name ,"mobile no." : self.Mobile_no ,"Email ID" : self.Email ,"Address" : self.Address ,"Password" : self.Password}
        self.customer_id= len(self.personal_detail)+1
        self.personal_detail[self.customer_id]=self.items1
        print()
        print("The Regiteration details is filled by the customer ",self.personal_detail)
        print("*** details are completed *** thank you!")

    def login_user(self):
        print('\n****** Login ******')
        name = input("Enter Your Username : ")
        password = input("Enter Your Password : ")
        if (self.Name == name and self.Password == password):
            print("*** Varified ***")
            print("Successful login!\nGo ahead for order!!!")
            order_count=0
            obj.my_order(order_count)
        else:
            print("\nUsername or Password is incorrect")
            obj.login_user()

    def my_order(self,order_count):
        print("\nPlace New Order")
        print("1 - Tandoori Chicken (4 pieces) [INR 240] ,2 - Vegan Burger (1 Piece) [INR 320] ,3 - Truffle Cake (500gm) [INR 900]")
        self.food1 = {
            1:"Tandoori Chicken (4 pieces) [INR 240]",
            2:"Vegan Burger (1 Piece) [INR 320]",
            3:"Truffle Cake (500gm) [INR 900]"
        }
        order = False
        entry = int(input("Enter order no --  \n"))
        if(entry in self.food1.keys()):
            order=True
        
        if order:
            print("your order : ",self.food1.get(entry))
            print("\nYour order is placed!\nThank you visit again")
            quit()
        else:
            order_count+=1
            print("Invalid option. Please try agian!")
            if order_count<3:
                self.my_order(order_count)
            else:
                quit()

obj = Food_Ordering_App()
obj.register_user()
obj.login_user()
obj.my_order()
        
