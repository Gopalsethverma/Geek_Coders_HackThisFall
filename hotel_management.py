import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

users = {"amit":125,"vipul": 2541,"anish": 1241}
print("******************WELCOME TO TAJ HOTEL*********************")
guests = pd.DataFrame({"Name": ["Amitabh","Naman","King","Darshan","Narendra"],"Check In Time": [5,0.00,2.0,3.50,5.25],
                        "Room Type": ["Non A/C Room","A/C Room","Deluxe Suite","A/C Room","Non A/C Room"],
                        "Food Type": ["Breakfast Combo","Lunch Combo","Dinner Combo","Tea","Water"],
                        "Nights": [2,1,2,2,2],
                        "Cost": [25000,3000,10000,50000,45000],
                        "Laundry Cost": [550,0,50,160,0],
                        "Review":[5,4,4,5,5]})

room_types = {"Non A/C Room":3000,"A/C Room":5000,"Deluxe Suite":10000}
food_types = {"Water":50,"Tea":100,"Breakfast Combo":9000,"Lunch Combo":15000,"Dinner Combo":25000}
laundry_types = {"Shorts":10,"Trouser":15,"Shirt":20,"Jeans":30,"GirlsSuit":70}

def main_menu():
    print("1. Guest Details")
    print("2. Add new Guest")
    print("3. Cancel Booking of a Guest")
    print("4. Hotel Bill (Room Rent & Food Cost)")
    print("5. Laundry Bill")
    print("6. Ask the guest for review")
    print("7. Distribution of room types")
    print("8. Distribution of total costs")
    print("9. Histogram for cost of rooms")
    print("10. Scatter Plot of cost of room and number of nights")
    

def guest_details():
    print("Guest Details:")
    print(guests)

def add_guest():
    name = input("Enter the name of Guest : ")
    time = float(input("Enter the time of Check-in in 24 hour format : "))
    room_type = input("Enter the room type :")
    nights = int(input("Enter the number of nights he want to stay : "))
    food_type = input("Enter the type of food services opted :")
    laundry_type=input("Enter the type of cloth you want to be washed : ")

    if room_type not in room_types or food_type not in food_types:
        print("Input the correct option.")

    else:
        cost = room_types[room_type] * nights + food_types[food_type]
        laundry_cost=laundry_types[laundry_type]
        guests = guests.append({"Name": name, "Check In Time": time, "Room Type": room_type, "Food Type": food_type, "Nights": nights, "Cost": cost, "Laundry Cost":laundry_cost }, ignore_index=True)
        print("The new data of Guest and their payments :")
        print(guests)

def cancel_room():
    name = input("Enter the name of guest you want to cancel booking : ")
    guests = guests[guests.Name != name]
    print("The updated details of guests: ")
    print(guests)

def print_hotel_bill(guests, name):
    mask = guests['Name'] == name
    person = guests[mask]
    if person.empty:
        print(f"No records found for {name}")
        return
    bill = person['cost'].values[0]
    print("Hotel Bill")
    print("==========")
    print(f"Name: {person['Name']}")
    print(f"Room Type: {person['Room Type']}")
    print(f"Nights Stayed: {person['Nights']}")
    print("--------")
    print(f"Total Bill: {bill}")


def laundry_bill(guests):
    print("Laundry Bill:")
    print("Name\t\tLaundry Cost")
    print(guests[["Name","Laundry Cost"]])

def ask_for_feedback(guests):
    review = int(input("Enter your review on a scale of 1-5: "))
    guests = guests.append({"Name": guests.iloc[-1]["Name"], "Check In Time": guests.iloc[-1]["Check In Time"], "Room Type": guests.iloc[-1]["Room Type"], "Food Type": guests.iloc[-1]["Food Type"], "Nights": guests.iloc[-1]["Nights"], "Cost": guests.iloc[-1]["Cost"], "Laundry Cost": guests.iloc[-1]["Laundry Cost"], "Review": review }, ignore_index=True)
    print("Thank you for your feedback!")
    return guests

def plot_room_type_distribution(data):
    room_types = data['room_type'].value_counts()
    room_types.plot(kind='bar')
    plt.xlabel('Room Type')
    plt.ylabel('Count')
    plt.title('Distribution of Room Types')
    plt.show()

def plot_cost_distribution():
    guests["Total Cost"] = guests["Cost"] + guests["Laundry Cost"]
    guests.plot(x="Name", y="Total Cost", kind="line", linestyle=":")
    plt.title("Total Cost per Guest")
    plt.xlabel("Guest Name")
    plt.ylabel("Total Cost")
    plt.show()

def plot_room_cost_histogram():
    plt.figure()
    sns.histplot(data=guests, x="Cost", bins=20)
    plt.xlabel("Cost (in Rupees)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Room Costs")
    plt.show()

def scatter_plot(data):
    cost = data['Cost of Room']
    nights = data['Number of Nights']
    plt.scatter(nights, cost)
    plt.xlabel('Number of Nights')
    plt.ylabel('Cost of Room')
    plt.title('Cost of Room vs Number of Nights')
    plt.show()

print("1. Register yourself to portal")
print("2. Login here")
option=int(input("Enter your choose : "))
if option==1:
    username = input("Enter your username: ")
    password = int(input("Enter your password: "))
    users[username]=password
    print("You are successfully registered.")
    main_menu()
    op=int(input("Choose any option : "))
    if op==1:
        guest_details()
    elif op==2:
        add_guest()
    elif op==3:
        cancel_room()
    elif op==4:
        name=input("Enter the name of Guest : ")
        print_hotel_bill(guests,name)
    elif op==5:
        laundry_bill(guests)
    elif op==6:
        ask_for_feedback(guests)
    elif op==7:
        plot_room_type_distribution(guests)
    elif op==8:
        plot_cost_distribution()
    elif op==9:
        plot_room_cost_histogram()
    elif op==10:
        scatter_plot(guests)
    else:
        print("Enter the correct input.")
elif option==2:
    username = input("Enter your username: ")
    password = int(input("Enter your password: "))
    if username in users and users[username] == password:
        print("Login successful!")
        main_menu()
        op=int(input("Enter your option :"))
        if op==1:
            guest_details()
        elif op==2:
            add_guest()
        elif op==3:
            cancel_room()
        elif op==4:
            name=input("Enter the name of Guest : ")
            print_hotel_bill(guests,name)
        elif op==5:
            laundry_bill(guests)
        elif op==6:
            ask_for_feedback(guests)
        elif op==7:
            plot_room_type_distribution(guests)
        elif op==8:
            plot_cost_distribution()
        elif op==9:
            plot_room_cost_histogram()
        elif op==10:
            scatter_plot(guests)
        else:
            print("Enter the correct input.")
    else:
        print("Wrong username or password, try again.")
else:
    print("Enter correct option.")
    











   
    


