# Why Inheritance
# Code Redundancy -> Development Time

class FlightBooking:

    def __init__(self, from_location, to_location, departure_date, travellers, travel_class):
        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date
        self.travellers = travellers
        self.travel_class = travel_class

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(self.from_location, self.to_location)
        print(self.departure_date)
        print(self.travellers, self.travel_class)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

# RoundTripFlightBooking IS-A FlightBooking
# extension
class RoundTripFlightBooking(FlightBooking):

    def __init__(self, from_location, to_location, departure_date, travellers, travel_class, return_date):
        FlightBooking.__init__(self, from_location, to_location, departure_date, travellers, travel_class)
        self.return_date = return_date

    def show(self):
        FlightBooking.show(self)
        print(self.return_date)


def main():

    one_way_booking = FlightBooking(from_location="Delhi", to_location="Bangalore", departure_date="12th Aug 2021", travellers=2, travel_class="economy")
    print(vars(one_way_booking))

    print()

    two_way_booking = RoundTripFlightBooking(from_location="Delhi", to_location="Bangalore", departure_date="12th Aug 2021", travellers=2, travel_class="economy", return_date="20th Aug 2021")
    print(vars(two_way_booking))

    two_way_booking.show()


if __name__ == '__main__':
    main()


# Assignment: Code Inheritance looking into the PayTM App

"""
    Types of Inheritance
    
    1. Single Level
    class CA:
        pass
        
    class CB(CA):
        pass   
        
    2. Multi Level
    class CA:
        pass
        
    class CB(CA):
        pass   
        
    class CC(CB):
        pass 
        
    3. Hierarchy
    class CD(CA):
       pass
       
       
    4. Multiple
    class CE:
        pass
        
    class CF(CE, CA):
        pass       
               
"""