from database import *

class Inventory:

    @staticmethod
    def add_blood(blood_type, quantity=1):
        query = f""" SELECT quantity from inventory 
                WHERE blood_type = "{blood_type}"; """
        result = db_query(query)[0][0]
        result = result + quantity
        query = f"""UPDATE inventory SET quantity = {result} 
                WHERE blood_type = "{blood_type}"; """
        db_query(query)
        mydb.commit()
        # print(result)

    @staticmethod
    def deduct_blood(blood_type, quantity=1):
        query = f"""SELECT quantity from inventory WHERE 
                blood_type = "{blood_type}";"""
        result = db_query(query)[0][0]

        if result < quantity:
            print(f"Sorry Not Sufficient Blood Available {blood_type}")
        else:
            result = result - quantity
            query = f"""UPDATE inventory SET quantity = {result} 
                    WHERE blood_type = "{blood_type}"; """

            db_query(query)
            mydb.commit()


# Inventory.add_blood("A+")
# Inventory.deduct_blood(blood_type="A+", quantity=10)
