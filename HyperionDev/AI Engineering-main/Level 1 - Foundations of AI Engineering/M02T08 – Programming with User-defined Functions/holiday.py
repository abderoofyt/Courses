# 1. Create a Python file called 
# holiday.py.

# Remember, each city will have different flight costs). plane_cost()
print("Available cities:\n1. London\n2. Paris\n3. New York\n4. Tokyo")

# Create a dictionary to handle both number and name input
city_map = {
    "1": "London",
    "London": "London",
    "2": "Paris",
    "Paris": "Paris",
    "3": "New York",
    "New York": "New York",
    "4": "Tokyo",
    "Tokyo": "Tokyo"
}

# 3. First, get the following user inputs:
raw_city_input = input("Enter the city name or number you will be flying to: ").strip().title()

# ● city_flight: The city they will be flying to (you can create some options for them. 
city_flight = city_map.get(raw_city_input, "Unknown")

# ● num_nights: The number of nights they will be staying at a hotel.
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))

# ● rental_days: The number of days for which they will be hiring a car.
rental_days = int(input("Enter the number of days you will be hiring a car: "))

# 4. Next, create the following four functions hotel_cost(), plane_cost(), car_rental(), holiday_cost():
def hotel_cost(num_nights):
    #This function will take num_nights as an argument and return a 
    # total cost for the hotel stay (you can choose the price per night charged at the hotel).
    price_per_night = 100
    return num_nights * price_per_night

def plane_cost(city_flight):
    #This function will take city_flight as an argument and return a cost 
    # for the flight. Hint: use if/else statements in the function to retrieve a price based on the chosen city.
    if city_flight == "London":
        return 250
    elif city_flight == "Paris":
        return 300
    elif city_flight == "New York":
        return 500
    elif city_flight == "Tokyo":
        return 800
    else:
        return 0

def car_rental(rental_days):
    #This function will take rental_days as an argument and return the 
    # total cost of the car rental (you can choose the daily rental cost).
    daily_rental_cost = 40
    return rental_days * daily_rental_cost

def holiday_cost(num_nights, city_flight, rental_days):
    #This function takes three arguments: num_nights, city_flight, and rental_days. 
    # Using these three arguments, call the hotel_cost(), plane_cost(), and car_rental() functions 
    # with their respective arguments, and finally return the total cost for the holiday.
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)

# 5. Print out all the details about the holiday in a way that is easy to read.
print("\n------ Holiday Summary ------")
print(f"Destination: {city_flight}")
print(f"Hotel stay for {num_nights} nights: R{hotel_cost(num_nights)}")
print(f"Flight to {city_flight}: R{plane_cost(city_flight)}")
print(f"Car rental for {rental_days} days: R{car_rental(rental_days)}")

# 2. Your task will be to calculate a user’s total holiday cost, 
# which includes the plane cost, hotel cost, and car rental cost.
print(f"Total holiday cost: R{holiday_cost(num_nights, city_flight, rental_days)}")
