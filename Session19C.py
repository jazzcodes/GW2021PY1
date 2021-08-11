# Duck Typing

class CA:
    pass

# RTP
# Dynamic Typing
a = 10
a = 2.2
a = "Hello"
a = CA()

class Cab:

    def book_cab(self, source, destination):
        print("Cab Booked from {} to {}".format(source, destination))


class OLAMini(Cab):

    def book_cab(self, source, destination):
        print("OLA MINI Booked from {} to {}".format(source, destination))


class OLASedan(Cab):

    def book_cab(self, source, destination):
        print("OLA Sedan Booked from {} to {}".format(source, destination))

class Truck:

    def book_truck(self, source, destination, load=100):
        print("Truck Booked from {} to {} with load of {} kgs".format(source, destination, load))


def duck_testing(ref):
    ref.book_cab("Home", "Work")

cab = Cab()
duck_testing(cab)

cab = OLAMini()
duck_testing(cab)

cab = OLASedan()
duck_testing(cab)

cab = Truck()
duck_testing(cab)

