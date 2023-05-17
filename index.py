"""A typical car can hold four passengers and one driver, allowing
five people to travel around. Given n number of people, return how
many cars are needed to seat everyone comfortably."""

def how_many_cars(number_of_people):
    car_capacity = 5
    number_of_vehichles = number_of_people / car_capacity

    if number_of_people % car_capacity > 0:
        number_of_vehichles += 1
    return int(number_of_vehichles)

print(how_many_cars(11))