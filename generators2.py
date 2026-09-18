def generate_city(*cities):
    for city in cities:
        yield city

cities = generate_city("Bogota", "Montería", "Armenia", "Sincelejo")

print(next(cities))
print(next(cities))

def generate_cities(*cities):
    for city in cities:
        yield from city

cities_from = generate_cities("Bogota", "Montería", "Armenia", "Sincelejo")


print(next(cities_from ))
print(next(cities_from ))
print(next(cities_from ))
print(next(cities_from ))
print(next(cities_from ))
print(next(cities_from ))