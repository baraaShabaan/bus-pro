from bus import Bus
import random


class Main(object):

    def __init__(self):
        self.buses = []
        self.init_buses(no_buses=no_buses)
        print("\n Welcome to Shuttle Buses Application.\n")
        self.Start()

    def Start(self):
        while True:
            option = self.get_option()
            if option == 1:
                self.list_buses()

            elif option == 2:
                self.book_ticket()

            elif option == 3:
                print('\nThanks for using Shuttle Buses, Goodbye.')
                break

    def get_option(self):
        while True:
            try:
                print("[1] List All Buses. \n[2] Book New Ticket. \n[3] Quit.")
                option = int(input("\nYour Choice > "))
                if option in [1, 2, 3]:
                    return option
                else:
                    raise

            except Exception as e:
                print("\n[!] Please insert a valid option.")
                self.get_option()
                break

    def list_buses(self):
        for bus_no, bus in enumerate(self.buses):
            free_seats = ', '.join([str(seat['Number']) for seat in bus.listFreeSeats()])
            print(f"Bus {bus_no + 1}:")
            print(f"\t\tStart Destination : {bus.getStartDestination()}")
            print(f"\t\tEnd Destination : {bus.getEndDestination()}")
            print(f"\t\tAvailable Seats : {free_seats}\n")

    def book_ticket(self):
        try:
            bus_number = int(input("Inter Bus Number : ")) - 1
            seat_number = int(input("Choose Seat Number : "))

            free_seats = [seat['Number'] for seat in self.buses[bus_number].listFreeSeats()]
            if seat_number in free_seats:

                self.buses[bus_number].setSeatAs(seat_number, 'Deserved')

                print("\nYour Ticket is now booked.")
                print("Bus Information : ")
                print(f"\t\tStart Destination : {self.buses[bus_number].getStartDestination()}")
                print(f"\t\tEnd Destination : {self.buses[bus_number].getEndDestination()}\n")

            else:
                print("\n[!] This Seat is Deserved try again.\n")
                self.Start()

        except Exception:
            print('\n[!] Invalid Option.\n')
            self.Start()

    def init_buses(self, no_buses: int):
        # Cities List.
        cities = ['Gaza', 'Jericho', 'Metsoke Dragot', 'Tkoa', 'Nablus']

        for i in range(no_buses):
            # Get random city from cities list
            _from = random.choice(cities)

            # a loop to get end_destination different from start_destination.
            while True:
                _to = random.choice(cities)
                # if the chosen city is the start city choose another one.
                if _to == _from:
                    continue
                # if the chosen city is not the start city break the loop.
                else:
                    break

            # create bus object.
            bus = Bus(no_seats=12, start_destination=_from, end_destination=_to)

            # choose sex random seats and set there status as reserved.
            for seat in range(6):
                # choose random seat from available seats.
                bus.setSeatAs(random.randint(1, bus.getNoSeats()), 'Deserved')

            # append created bus object to the main buses variable to use it later.
            self.buses.append(bus)


if __name__ == '__main__':
    no_buses = 3
    main = Main()
