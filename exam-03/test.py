class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        seat_map = [['O' for j in range(self._cols)] for i in range(self._rows)]
        self._seats[id] = seat_map
        show_tuple = (id, movie_name, time)
        self._show_list.append(show_tuple)

    def book_seats(self, customer_name, phone_number, show_id, seat_list):
        if show_id not in self._seats:
            print(f"Invalid show id: {show_id}")
            return
        seat_map = self._seats[show_id]
        for seat in seat_list:
            row, col = seat
            if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
                print(f"Invalid seat: ({row}, {col})")
                return
            if seat_map[row][col] == 'X':
                print(f"Seat ({row}, {col}) already booked")
                return
            seat_map[row][col] = 'X'
        self._seats[show_id] = seat_map
        print(f"Booking successful for {customer_name} ({phone_number})")
        print(f"Seats booked: {seat_list}")

    def view_show_list(self):
        print("Shows running:")
        for show in self._show_list:
            print(f"Id: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self._seats:
            print(f"Invalid show id: {show_id}")
            return
        seat_map = self._seats[show_id]
        print(f"Available seats for show {show_id}:")
        for i in range(self._rows):
            for j in range(self._cols):
                if seat_map[i][j] == 'O':
                    print(f"({i}, {j})", end=" ")
            print()

# creating a hall and adding it to Star_Cinema
hall1 = Hall(5, 5, 1)

# adding a show to the hall
hall1.entry_show(101, "Avengers: Endgame", "10:00 AM")

# viewing the show list
hall1.view_show_list()

# viewing available seats for the show
hall1.view_available_seats(101)

# booking seats for a customer
hall1.book_seats("John Doe", "1234567890", 101, [(0, 0), (1, 1)])

# viewing available seats for the show again
hall1.view_available_seats(101)

# booking invalid seats
hall1.book_seats("Jane Doe", "0987654321", 101, [(0, 0), (6, 6), (-1, -1)])

# trying to book seats for an invalid show id
hall1.book_seats("Jim Doe", "5678901234", 102, [(0, 0), (1, 1)])
