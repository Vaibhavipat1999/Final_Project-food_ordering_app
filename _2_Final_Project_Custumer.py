# --------------------------------- User ---------------------------------- #

class Food_Ordering_App:
    def __init__ (self):
        self.order    = {}
        self.order_id = len(self.order)+1
        self.personal_detail = {}

    def user_details(self):
        print('\n****** User details ******')
        self.Name      = input("Enter your Full Name: ")
        self.Mobile_no = int(input("Enter your Mobile no : "))
        self.Email     =  input("Enter your Email : ")
        self.Address   = input("Enter your Address : ")
        self.Password  = input("Enter any strong Password : ")
        self.items1    = {"full_name" : self.Name ,"mobile no." : self.Mobile_no ,"Email ID" : self.Email ,"Address" : self.Address ,"Password" : self.Password}
        self.customer_id= len(self.personal_detail)+1
        self.personal_detail[self.customer_id]=self.items1
        print("------- user details are completed -------")

    def login_info(self):
        user = input('''\nIf you are already a User then enter "Yes" to login. If you are new user enter "No" for Regiteration : ''') 
        if user.upper() == "YES": 
            obj.login_user() 
        else:
            obj.register_user()
            return user 

    def register_user(self):    
        print('\n****** Regiteration ******')
        new_user = input("Enter a New Username : ")
        if new_user == self.Name:
            print("This username already exists!!!! ")
            return new_user
        else:
            new_Password  = input("Enter a Strong Password: ")
            re_Password   = input("Please Re-enter your Password: ") 
            if self.Password == new_Password and new_Password  == re_Password:
                print("Successful registration!")
                order_count=0
                obj.my_order(order_count)
            else:
                print("Invalid username/passord. Register again!")
                return new_user

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
            return obj.login_user

    def my_order(self,order_count):
        print("\nPlace New Order")
        print("1 - Tandoori Chicken (4 pieces) [INR 240] ,2 - Vegan Burger (1 Piece) [INR 320] ,3 - Truffle Cake (500gm) [INR 900]")
        self.food1 = {
            1:"Tandoori Chicken (4 pieces) [INR 240]",
            2:"Vegan Burger (1 Piece) [INR 320]",
            3:"Truffle Cake (500gm) [INR 900]"
        }
        order=False
        entry=int(input("enter order no -"))
        if(entry in self.food1.keys()):
            order=True
        
        if order:
            print(self.food1.get(entry))
            print("thank you visit again")
            quit()
        else:
            order_count+=1
            print("Invalid option. Please try agian!")
            if order_count<3:
                self.my_order(order_count)
            else:
                quit()
          
        
obj = Food_Ordering_App()
obj.user_details()
obj.login_info()
obj.register_user()
obj.login_user()
obj.my_order()

