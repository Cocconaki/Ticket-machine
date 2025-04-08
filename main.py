from distances import *
import os
from prices import discounts
from ticket import determine_price, create_instance

while True:
    os.system("cls")
    print("Üdvözöljük! Válasszon az alábbi opciók közül:")
    print("Vonatjegy vásárlás (1)")
    print("Vonaljegy vásárlás autóbuszra (2)")

    choice = int(input("Enter: "))

    match choice:

        case 1:
            os.system("cls")
            print("Válasszon úticélt:")
            for loc in locations:
                print(f"{loc['id']}. {loc['name']}: {loc['distance']} km")

            destination_number = input("Adja meg az úticél számát: ")
            for loc in locations:
                if {loc['id']} == destination_number:
                    chosen_destination = {loc['name']}
                    distance_to_travel = {loc['distance']}

            print("Válasszon kedvezményt: ")
            for dis in discounts:
                print(f"{dis['id']}. {dis['name']}")
            discount_number = input(": ")
            for dis in discounts:
                if {dis['name']} == discount_number:
                    discount_value = {dis['discount']}
                    discount_name = {dis['name']}
            
            final_price = determine_price("train", distance_to_travel, discount_value)
            ticket_ready = create_instance(chosen_destination, "train", "30days", distance_to_travel, discount_name, final_price  )

            print("Vegye el a jegyet")
            input()
            print(f"Fizetendő összeg: {ticket_ready.price}")
            
            

            
            

        case 2:
            print("Válasszon kedvezményt: ")
            for dis in discounts:
                print(f"{dis['id']}. {dis['name']}")
            discount_number = input(": ")
            for dis in discounts:
               if {dis['name']} == discount_number:
                    discount_value = {dis['discount']}

            determine_price("bus", None, discount_value)


###testing git###