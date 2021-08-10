class MovieTicket:

    # Property of Class
    cinema_hall = {
        "A": 10,
        "B": 12,
        "C": 8,
        "D": 15,
        "E": 10,
        "F": 10,
    }

    total_seats = sum(cinema_hall.values())

    ticket_number = 1

    def __init__(self, movie, date, time):

        if MovieTicket.total_seats == 0:
            print("Movie is all Booked :)")
            return

        self.ticket_number = MovieTicket.ticket_number
        self.movie = movie
        self.seat = MovieTicket.cinema_hall["A"]
        self.date = date
        self.time = time

        # MovieTicket.cinema_hall["A"] -= 1
        # MovieTicket.total_seats -= 1
        # MovieTicket.ticket_number += 1

    # for any function if we create inside the class
    # 1st input is self -> which is reference to the current object
    def show(self):
        pass

    # it takes reference of class as input
    @classmethod
    def create_tickets_from_file(cls, file_name):
        print("cls is:", cls)
        print("vars(cls) is:", vars(cls))
        # why to use @classmethod
        # we need to process data of class :)
        print(cls.cinema_hall)

        file = open(file_name, "r")
        lines = file.readlines()

        tickets = []

        for line in lines:
            data = line.split(",")
            print("data:", data)

            ref = cls(movie=data[0], date=data[1].strip(), time=data[1].strip())
            ref.ticket_number = cls.ticket_number
            ref.seat = cls.cinema_hall["A"]

            cls.cinema_hall["A"] -= 1
            cls.total_seats -= 1
            cls.ticket_number += 1

            tickets.append(ref)

        return tickets

    # We may have a function inside a class which needs no data processing
    @staticmethod
    def show_header():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Welcome to my Movie Ticket App")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def main():

    """
    ticket1 = MovieTicket(movie="Any Movie Name", date="15th Aug, 2021", time="16:00")
    print(vars(ticket1))
    print(vars(MovieTicket))

    # ticket1.create_tickets_from_file()
    MovieTicket.create_tickets_from_file()
    """

    MovieTicket.show_header()

    tickets = MovieTicket.create_tickets_from_file(file_name="tickets.csv")

    print("TICKET OBJECTS FROM FILE")
    for ticket in tickets:
        print(vars(ticket))

if __name__ == '__main__':
    main()