while True: 
    import mysql.connector
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="car_dealership"
    )
    cursor = con.cursor()

    print("\U0001F600   WELCOME TO FIRST MOTORS   \U0001F600")

    purpose = int(input("1. View Collection\n2. Sell Car\n3. Raise Service Request\nEnter your choice : "))
    if purpose==1:
        view_layout = int(input("Enter 0 to view full collection, and 1 to filter your search : "))
        if view_layout==0:
            cursor.execute(
            "select*from collection;"
            )
            results = cursor.fetchall()
            for row in results:
                print(f"Sr. No.: {row[0]}, Registration Number: {row[1]} \nMake: {row[2]}, Model: {row[3]} \nPrice: {row[4]}, Driven KMs: {row[5]}")
        else:
            filter_area = int(input('1. Make\n2. Model\n3. Price\n4. Driven KMs\n Enter your filter branch : '))
            if filter_area==1:
                make_input = str(input("Enter the make : "))
                make_filter_query = f"select*from collection where make='{make_input}'"
                cursor.execute(make_filter_query
                )
                results = cursor.fetchall()
                for row in results:
                    print(f"Sr. No.: {row[0]}, Registration Number: {row[1]} \nMake: {row[2]}, Model: {row[3]} \nPrice: {row[4]}, Driven KMs: {row[5]}")

            elif filter_area==2:
                model_input = str(input("Enter the model : "))
                model_filter_query = f"select*from collection where model='{model_input}'"
                cursor.execute(model_filter_query
                )
                results = cursor.fetchall()
                for row in results:
                    print(f"Sr. No.: {row[0]}, Registration Number: {row[1]} \nMake: {row[2]}, Model: {row[3]} \nPrice: {row[4]}, Driven KMs: {row[5]}")
            elif filter_area==3:
                min_price_range = int(input("Enter the minimum price : "))
                max_price_range = int(input("Enter the maximum price : "))
                price_filter_query = f"select*from collection where price between {min_price_range} and {max_price_range}"
                cursor.execute(price_filter_query
                )
                results = cursor.fetchall()
                for row in results:
                    print(f"Sr. No.: {row[0]}, Registration Number: {row[1]} \nMake: {row[2]}, Model: {row[3]} \nPrice: {row[4]}, Driven KMs: {row[5]}")
            else:
                min_drivenkm_range = int(input("Enter the minimum driven kms : "))
                max_drivenkm_range = int(input("Enter the maximum driven kms : "))
                drivenkm_filter_query = f"select*from collection where driven_kms between {min_drivenkm_range} and {max_drivenkm_range}"
                cursor.execute(drivenkm_filter_query
                )
                results = cursor.fetchall()
                for row in results:
                    print(f"Sr. No.: {row[0]}, Registration Number: {row[1]} \nMake: {row[2]}, Model: {row[3]} \nPrice: {row[4]}, Driven KMs: {row[5]}")
        buy_car = int(input("Enter 0 to exit and 1 to buy a car : "))
        if buy_car == 0:
            break
        else:
            while True:
                registration_no = str(input("Enter the registration number of the car you want to buy : "))
                regno_filter_query = f"select*from collection where reg_no='{registration_no}'"
                cursor.execute(regno_filter_query
                )
                results = cursor.fetchall()
                for row in results:
                    print(f"Sr. No.: {row[0]}, Registration Number: {row[1]} \nMake: {row[2]}, Model: {row[3]} \nPrice: {row[4]}, Driven KMs: {row[5]}")
                
                confirm_purchase = int(input("\nEnter 0 to change selection, 1 to PROCEED : "))
                if confirm_purchase==0:
                    continue                  
                else:
                    price = 0
                    make = ''
                    model = ''
                    reg_no = ''
                    for row in results:
                        price = row[4]
                        make = row[2]
                        model = row[3]
                        reg_no = row[1]
                    
                    last_confirmation = int(input("Press 0 to confirm purchase : "))
                    if last_confirmation==0:
                        delete_query = f"DELETE FROM collection WHERE reg_no = '{registration_no}';"
                        cursor.execute(delete_query)
                        query = f"{make}" + f" {model}"
                        accounts_query = f"insert into accounts(reg_no,make,model,reason_of_transaction,amount) values('{reg_no}','{make}','{model}','Customer bought {query}',{price})"
                        cursor.execute(accounts_query)
                        con.commit()
                        cursor.close()
                        con.close()
                        new_balance = 0
                        with open('current_balance.txt','r') as f:
                            current_balance = f.read()
                            number = int(current_balance)
                            new_balance = number + price
                            new_balance = str(new_balance)
                        balance = str(new_balance)
                        with open("current_balance.txt","w") as f:
                            f.write(balance)
                        print("\U0001F389\U0001F389Congratulations !!! on your new purchase of",make + '',model,'\U0001F389\U0001F389')
                        print("Thank you for letting us be a part of your happiness.\U0001F600")
                        break
                    else:
                        break
            break
                    
    elif purpose==2:
        reg_no = str(input("Enter the Registration Number for the vehicle : "))
        make = str(input("Enter the Make for the vehicle : "))
        model = str(input("Enter the Model for the vehicle : "))
        driven_kms = int(input("Enter the Driven KMs for the vehicle : "))
        type = str(input("Enter the Type of the vehicle : "))
        price = int(input("Enter the Price for the vehicle : "))
        increased_price = int(price * 1.2)
        new_balance = 0
        with open('current_balance.txt','r') as f:
            current_balance = f.read()
            number = int(current_balance)
            new_balance = number - price
            new_balance = str(new_balance)
        balance = str(new_balance)
        with open("current_balance.txt","w") as f:
            f.write(balance)
        query = f"{make}" + f" {model}"
        accounts_query = f"insert into accounts(reg_no,make,model,reason_of_transaction,amount) values('{reg_no}','{make}','{model}','Customer sold {query}',{price})"
        insert_query = f"insert into collection(reg_no,make,model,driven_kms,type,price) values('{reg_no}','{make}','{model}',{driven_kms},'{type}',{increased_price});"
        cursor.execute(insert_query)
        cursor.execute(accounts_query)
        con.commit()
        cursor.close()
        con.close()
        print("\U0001F389\U0001F389Congratulations !!! Your car",make + '',model,'is put up for sale\U0001F389\U0001F389')
        break
    elif purpose==3:
        reg_no = str(input("Enter the Registration Number for the vehicle : "))
        make = str(input("Enter the Make for the vehicle : "))
        model = str(input("Enter the Model for the vehicle : "))
        issue = str(input("Expain your problem : "))
        insert_query = f"insert into service(reg_no,make,model,issue) values('{reg_no}','{make}','{model}','{issue}');"
        cursor.execute(insert_query)
        con.commit()
        cursor.close()
        con.close()
        print("Thank you for trusting us on your problem. \nWe will reach out to you with a solution shortly.\U0001F600")
        break
    else:
        print("Wrong input !! Please choose carefully. \U0001F600")
        break
