squares = [x**2 for x in  range(5)]
print(squares)

even_numbers = [x for x in range(10) if x%2==0]
print(even_numbers)

results = ['pass' if score >= 60 else 'fail' for score in [75, 30, 85, 50]]
print(results)

names=['John', 'Jane', 'Jim']
name_lengths = [len(names) for name in names]
print(name_lengths)