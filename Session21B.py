import threading
import time

lock = threading.Lock()

class MovieTicket:

    def __init__(self, name, time, row, seat):
        self.name = name
        self.time = time
        self.row = row
        self.seat = seat
        self.is_booked = False

    def book_ticket(self):
        if self.is_booked:
            print("[BOOKTICKET] Sorry {} Ticket is Already Booked".format(self.email))
        else:
            self.is_booked = True
            print("~"*20)
            print("[BOOKTICKET] Ticket Booked for {}:".format(self.email))
            print("[BOOKTICKET] Ticket: {name}, {time}, {row}, {seat}".format_map(vars(self)))
            print("~" * 20)

    def pay(self, email):
        self.email = email
        if self.is_booked:
            # print("[PAYMENT] Sorry {} Ticket is Already Booked".format(self.email))
            return
        else:
            print("[PAYMENT] Dear,{} Please Pay: \u20b9 150".format(self.email))
            time.sleep(3)
            print("[PAYMENT] Thank You {} !! Transaction Finished".format(self.email))

class BookMovieTicket(threading.Thread):

    def select_seat(self, ticket, email):
        self.ticket = ticket
        self.email = email

    def run(self):
        lock.acquire()
        self.ticket.pay(email=self.email)
        self.ticket.book_ticket()
        lock.release()


def main():
    print("BookMoveTicketApp Started")

    row_a_tickets = [
        MovieTicket(name="Avengers", time="16:30", row="A", seat=1),
        MovieTicket(name="Avengers", time="16:30", row="A", seat=2),
        MovieTicket(name="Avengers", time="16:30", row="A", seat=3),
        MovieTicket(name="Avengers", time="16:30", row="A", seat=4),
        MovieTicket(name="Avengers", time="16:30", row="A", seat=5),
        MovieTicket(name="Avengers", time="16:30", row="A", seat=6),
        MovieTicket(name="Avengers", time="16:30", row="A", seat=7),
        MovieTicket(name="Avengers", time="16:30", row="A", seat=8),
        MovieTicket(name="Avengers", time="16:30", row="A", seat=9),
        MovieTicket(name="Avengers", time="16:30", row="A", seat=10),
    ]

    booking1 = BookMovieTicket()
    booking2 = BookMovieTicket()

    booking1.select_seat(ticket=row_a_tickets[1], email="john@example.com")
    booking2.select_seat(ticket=row_a_tickets[1], email="fionna@example.com")

    booking1.start()
    booking2.start()


    # time.sleep(5)
    # print(time.time())

    print("BookMoveTicketApp Finished")

if __name__ == '__main__':
    main()