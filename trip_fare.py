trips = [5, 10, 3]

# **Base fare**: $50
# - **Distance fare**: $10/km
base_fare=50;
distance_fare=10
def total_fare_fun(trips):
    total_fare=0
    for i in range(len(trips)):
        trip=trips[i]
        price=base_fare+trip*distance_fare
        print(f"Trip {i+1}: ${price}")
        total_fare+=price
    print(f"Total Fare: ${total_fare}")

total_fare_fun(trips)