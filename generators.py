def generate_even_numbers(limit):
    num = 1;

    while num < limit: 

        yield num * 2

        num += 1

for i in generate_even_numbers(10):
    print(i)

    