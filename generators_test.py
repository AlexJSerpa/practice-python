def generate_number(*numbers):
    for i in numbers:
        yield i

numbers = generate_number(1,2,3,4)

print(next(numbers))

