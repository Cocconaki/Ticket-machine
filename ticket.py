from dataclasses import dataclass
from prices import *

@dataclass
class Ticket:

    price: int
    destination: str
    ticket_type: str #train, bus, etc...
    starting_point: str
    valid_until: str
    distance: int
    discount_type: str


def determine_price(ticket_type, distance, discount_type):
    
    if ticket_type == "bus":
        final_price == BUS_TICKET_PRC - (BUS_TICKET_PRC / 100) * discount_type
        return final_price
    elif ticket_type == "train":
        base_price = distance * PPK_train
        final_price = base_price - (base_price / 100) * discount_type
        return final_price

def create_instance(destination, ticket_type, valid_until, distance, discount_type, price, starting_point="Budapest"):

    ticket = Ticket(
                    price=price, 
                    destination=destination, 
                    ticket_type=ticket_type, 
                    starting_point=starting_point, 
                    valid_until=valid_until, 
                    distance=distance, 
                    discount_ticket_type=discount_type)
    return ticket