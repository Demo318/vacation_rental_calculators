# Calculator for demonstrating the advantage to allowing
# three-night stays after calendar has been filled up with
# all possible 5-night stays.

import random

class Reservation:

    def __init__(self, check_in_night, length_of_stay, nightly_rate):
        self.length_of_stay = length_of_stay
        self.check_in_night = check_in_night
        self.nightly_rate = float(nightly_rate)
        self.value = float(nightly_rate * length_of_stay)

    def __str__(self):
        return f"{self.length_of_stay} Nights: Check-in {str(self.check_in_night).rjust(2, '0')}, Check-out {str(self.check_in_night + self.length_of_stay - 1).rjust(2, '0')}. Value: ${self.value}."

class BookingCalendar:

    def __init__(self, nightly_rate, mark_up):
        self.unbooked_nights = list(range(1, 31))
        self.reservations = list()
        self.nightly_rate = float(nightly_rate)
        self.mark_up = float(mark_up)

    def reservations_by_length_of_stay(self, length_of_stay):
        reservations = list()
        for reservation in self.reservations:
            if reservation.length_of_stay == length_of_stay:
                reservations.append(reservation)
        return reservations

    def list_eligible_check_in_nights(self, length_of_stay):
        eligible_nights = list(filter(lambda x: self.is_night_eligible(length_of_stay, x), self.unbooked_nights))
        return eligible_nights

    def is_night_eligible(self, length_of_stay, check_in_night):
        for night in range(0, length_of_stay + 1):
            check_night = check_in_night + night 
            if check_night <= 30 & check_night not in self.unbooked_nights:
                return False
        return True

    def sort_reservations(self, reservation):
        return reservation.check_in_night
    
    def add_reservation(self, check_in_night, length_of_stay, nightly_rate):
        self.reservations.append(Reservation(check_in_night, length_of_stay, nightly_rate))
        for night in range(0, length_of_stay):
            remove_night = night + check_in_night
            if type(remove_night) != int:
                print(remove_night)
            if remove_night <= 30:
                self.unbooked_nights.remove(remove_night)
        self.reservations.sort(key=self.sort_reservations)

    def book_all_nights(self, length_of_stay, mark_up):
        if mark_up == True:
            rate = self.nightly_rate * (self.mark_up + 1)
        else:
            rate = self.nightly_rate

        eligible_days = self.list_eligible_check_in_nights(length_of_stay)

        while len(eligible_days) > 0:
            check_in_night = random.choice(eligible_days)
            self.add_reservation(check_in_night, length_of_stay, rate)
            eligible_days = self.list_eligible_check_in_nights(length_of_stay)

nightly_rate = float(input("Enter your average nightly rate for a five-night stay (ex. $250 should be entered as 250):"))

mark_up = float(input("Enter your mark-up for a 3-night stay (ex. 20% should be entered as 20):")) * 0.01

booking_calendar = BookingCalendar(nightly_rate, 0.2)

booking_calendar.book_all_nights(5, False)

booking_calendar.book_all_nights(3, True)

print('5-night stays')
total_value = 0
for reservation in booking_calendar.reservations_by_length_of_stay(5):
    print(reservation)
    total_value += reservation.value
print(f"Value: ${total_value}")
print('\n')

print('3-night stays')
total_value = 0
for reservation in booking_calendar.reservations_by_length_of_stay(3):
    print(reservation)
    total_value += reservation.value
print(f"Value: ${total_value}")







