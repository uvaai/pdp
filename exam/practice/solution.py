# Assignment 1
def degree_table():
    print(f'Celsius\tKelvin\tFahrenheit')

    for celsius in range(-40, 101, 5):
        kelvins = 273 + celsius
        fahrenheit = (18 * celsius + 320) // 10

        print(f'{celsius}\t{kelvin}\t{fahrenheit}')

degree_table()

# Assignment 2
def find_alliterations(text, letter):

    output = []
    for word in text.split():
        word = word.lower()
        if word[0] == letter:
            output.append(word)

    return output

example_text = "David Donald Doo dreamed a dozen doughnuts and a duck-dog too."
alliterations = find_alliterations(example_text, "d")

print(alliterations)

# Assignment 3
def values_to_keys(whisky_brands):
    output = {}
    for key in whisky_brands:
        value = whisky_brands[key]

        if value not in output:
            output[value] = []

        output[value].append(key)

    return output

whisky_brands = {'Hibiki': 'Japan', 'Bushmills': 'Ireland', 'anCnoc': 'Scotland', 'Teeling': 'Ireland', 'Starward': 'Australia', 'Four Roses': 'USA', 'Aberlour': 'Scotland', 'Nikka': 'Japan', 'Bulleit': 'USA', 'Tullibardine': 'Scotland'}

whisky_origins = values_to_keys(whisky_brands)

print(whisky_origins)

# Assignment 4
def displacement_timeframe_cars(filename, year_start, year_end):
    total = 0
    count = 0

    linenumber = 0

    with open(filename, 'r') as infile:

        for line in infile:
            line = line.split(',')
            if linenumber > 0:
                year = int(line[6])
                displacement = float(line[2])

                if year_start <= year <= year_end:
                    total += displacement
                    count += 1

            linenumber += 1

    return total / count

filename = 'mpg.csv'
year_start = 72
year_end = 80
displacement = displacement_timeframe_cars(filename, year_start, year_end)
print(f'The average displacement of cars between {year_start} and {year_end} is {displacement} centiliters')
