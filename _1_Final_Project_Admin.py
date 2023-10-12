# -------------------------------- Admin ---------------------------------- #

class restaurent:
    def __init__(self):
        self.food={}
        self.food_id = len(self.food)+1
        self.personal_detail={}
        self.customer_id = len(self.personal_detail)+1
    
    def menu_card(self):
        self.food_name = input("Enter food name : ")
        self.quantity  = float(input("Enter food quantity : "))
        self.price     = float(input("Enter food price: INR "))
        self.discount  = float(input("Enter food discount : INR "))
        self.stock     = float(input("Enter your stock : pieces "))
        self.item      = {"Nmae"    :self.food_name,
                          "Quantity":self.quantity,
                          "Price"   :self.price,
                          "Discount":self.discount,
                          "Stock"   :self.stock
                          }
        self.food_id   = len(self.food)+1
        self.food[self.food_id] = self.item
        print(self.food)
        print("**********Item added successfully**********\n")

    def delete_menu_card(self):
        del self.food[float(input("Enter the food ID which you want to delete : "))]
        print("Remaing menu are",self.food)

    def update_menu_card(self):
        f_id=float(input("Enter the food ID which you want to update : "))
        for i in self.food[f_id]:
            self.food[f_id][i]=input(f"Enter {i} you want to update :" )
        print(self.food)

obj = restaurent()
obj.menu_card()
obj.menu_card()
obj.update_menu_card()
obj.delete_menu_card()

     