total_seats = 10
booked_seats = [2, 5, 7]
book_seat = 3
cancel_seat = 5

def book_ticket(book_seat):
    if book_seat > total_seats or book_seat <= 0:
        return "Out of Range"
    if book_seat in booked_seats:
        return "Seat is already booked"
    booked_seats.append(book_seat)
    return f"Seat {book_seat} booked successfully."

def cancel_ticket(cancel_seat):
    if cancel_seat > total_seats or cancel_seat <= 0:
        return "Out of Range"
    if cancel_seat not in booked_seats:
        return "Seat is not booked"
    booked_seats.remove(cancel_seat)
    return f"Seat {cancel_seat} cancelled successfully."

def available_seats():
    return [i for i in range(1, total_seats + 1) if i not in booked_seats]

print(book_ticket(book_seat))
print(cancel_ticket(cancel_seat))
print("Available seats:", available_seats())
