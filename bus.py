class Bus(object):
    __start_destination: str
    __end_destination: str
    __no_seats: int
    __seats: list

    def __init__(self, no_seats=12, start_destination='Gaza', end_destination='Nablus'):
        self.__start_destination = start_destination
        self.__end_destination = end_destination
        self.__no_seats = no_seats
        self.__seats = []
        self.initSeats()

    def setStartDestination(self, destination: str):
        self.__start_destination = destination

    def getStartDestination(self):
        return self.__start_destination

    def setEndDestination(self, destination: str):
        self.__end_destination = destination

    def getEndDestination(self):
        return self.__end_destination

    def setNoSeats(self, no_seats: int):
        self.__no_seats = no_seats
        self.initSeats()

    def getNoSeats(self):
        return self.__no_seats

    def setSeatAs(self, seat_no: int, status: str):
        """Set Seat status Free or Deserved"""
        self.__seats[seat_no - 1]['Status'] = status

    def initSeats(self):
        """Create a list of seats dict and set there all status as Free"""
        for seat_no in range(self.__no_seats):
            seat = {'Number': seat_no + 1, 'Status': 'Free'}
            self.__seats.append(seat)

    def listAllSeats(self):
        return self.__seats

    def listFreeSeats(self):
        free_seats = []
        for seat in self.listAllSeats():
            if seat['Status'].lower() == 'free':
                free_seats.append(seat)

        return free_seats

    def listDeservedSeats(self):
        deserved_seats = []
        for seat in self.listAllSeats():
            if seat['Status'].lower() == 'deserved':
                deserved_seats.append(seat)

        return deserved_seats
