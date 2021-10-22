# Exam

This is a digital exam. The exam consists of programming exercises that are purely based on input, output, and calculations. You will use these exercises to show that you can create a program from scratch.

During the exam, it is not allowed to use the internet and there is no help from teaching assistants. You are allowed to use the pdp.mprog.nl website. You will not be graded on design, but only on the correctness of your code. You do not have to comment your code, nor do you have to abide by any other styling rules (though this can greatly help you understand your code).

# Rules

- Finish all exercises in a file named `exam.py` and submit this file
- Each exercise should be done in (at least) **one** function
- Outputs should be done within the exercise's function with `return`, unless stated otherwise
- You are not allowed to use `numpy` or other libraries in this exam
- Make sure the output for every exercise is printed to the screen when running your program. This is required to get the points for an exercise.

## Hints

The following steps should help you find solutions to the exercises:

1. Get an overview of the problem at hand:
  - What is the input? I.e., what external information does the function need?
  - What information is set? You might want to pre-define some values that will never change
  - What is the output? What should the function return?
2. Think of two examples, and predict what the output of the program should be given these examples. Determine how you would come to these answers
3. Propose a procedure in pseudocode, and try to find elements you will need to further work out
4. Implement your program in Python, include code that can be used to test your program
5. Test your program extensively using the examples you thought of in step 2, and see if you can find any edge cases where the program gives an unexpected output.
6. Finish your program and submit your solutions. *Before you leave the exam room, check with the proctor that your submission was correctly submitted!*

# 1. Temperatures

Kelvin $$K$$ and degrees Celsius $$C$$ are related by $$273+C=K$$. Degrees Celsius $$C$$ and degrees Fahrenheit $$F$$ are related by $$\frac{18C + 320}{10}=F$$. Write a function `degree_table()` that **prints** a neat table with three columns (Celsius, Kelvin, and Fahrenheit) from which you can read the corresponding temperature values. _This function should not return anything._ The table starts at 40 degrees Celsius below zero, increases in steps of 5 degrees and ends at (it should include) the boiling point of water at normal pressure (i.e. 100 degrees Celsius).

    degree_table()

Should print the following:

    Celsius Kelvin  Fahrenheit
    -40      233     -40
    -35      238     -31
    -30      243     -22
    -25      248     -13
    -20      253     -4
    -15      258     5
    -10      263     14
    -5       268     23
    0        273     32
    5        278     41
    10       283     50
    15       288     59
    20       293     68
    25       298     77
    30       303     86
    35       308     95
    40       313     104
    45       318     113
    50       323     122
    55       328     131
    60       333     140
    65       338     149
    70       343     158
    75       348     167
    80       353     176
    85       358     185
    90       363     194
    95       368     203
    100      373     212

**Hint:** You can neatly format the table using tabs, which can be printed using `'\t'`. The first two lines of the output above, for example, can be formatted as follows:

    print(f'Celsius\tKelvin\tFahrenheit')

    celsius = -40
    kelvin = 233
    fahrenheit = -40

    print(f'{celsius}\t{kelvin}\t{fahrenheit}')

Of course, the intended solution is to create the table programmatically (using a loop and calculations), and not to hardcode the table into a set of prints.

# 2. First letters

Write a function `find_alliterations(text, letter)` that accepts two strings as input: `text` and `letter`. The function should find all words in `text` starting with `letter`, and return them as a list. You can assume that `letter` is never more than one letter.

    example_text = "David Donald Doo dreamed a dozen doughnuts and a duck-dog, too."
    alliterations = find_alliterations(example_text, "d")

    print(alliterations)

Expected output:

    ['david', 'donald', 'doo', 'dreamed', 'dozen', 'doughnuts', 'duck-dog']

# 3. Water of life

A whisky lover has made a Python dictionary of their favorite whiskies. In this dictionary, for a couple of brands, the region of origin is noted. However, now they would like to know for each origin what brands there are. It is way too much work to search through each of the regions every time, so they have decided that they need another dictionary that is ordered the other way around. Write a function `values_to_keys()` that accepts a dictionary with brand names as keys and for each key a region as value. It should create a new dictionary that has the regions as keys, and a list of the brands that are from that region as values.

    whisky_brands = {'Hibiki': 'Japan', 'Bushmills': 'Ireland', 'anCnoc': 'Scotland', 'Teeling': 'Ireland', 'Starward': 'Australia', 'Four Roses': 'USA', 'Aberlour': 'Scotland', 'Nikka': 'Japan', 'Bulleit': 'USA', 'Tullibardine': 'Scotland'}

    whisky_origins = values_to_keys(whisky_brands)

    print(whisky_origins)

Should print:

    {'Japan': ['Hibiki', 'Nikka'], 'Ireland': ['Bushmills', 'Teeling'], 'Scotland':
    ['anCnoc', 'Aberlour', 'Tullibardine'], 'Australia': ['Starward'], 'USA': ['Four
    Roses', 'Bulleit']}

**Note:** the order in which this result is printed does not need to be the same as the example above. Check whether each origin has all of it's brands. If this is the case, your code probably works!

# 4. More cars

[Download the `mgp.csv` file.](/../data/mpg.csv)

The file `mpg.csv` ("mpg" stands for "miles per gallon") contains data of cars from three different areas of the world: Europe, Japan, and USA. In this exercise, you will use `mpg.csv` to answer a question about the data. The contents of the file look as follows:

    mpg,cylinders,displacement,horsepower,weight,acceleration,model_year,origin,name
    18.0,8,307.0,130.0,3504,12.0,70,usa,chevrolet chevelle malibu
    15.0,8,350.0,165.0,3693,11.5,70,usa,buick skylark 320
    ...
    44.0,4,97.0,52.0,2130,24.6,82,europe,vw pickup
    32.0,4,135.0,84.0,2295,11.6,82,usa,dodge rampage
    28.0,4,120.0,79.0,2625,18.6,82,usa,ford ranger
    31.0,4,119.0,82.0,2720,19.4,82,usa,chevy s-10

As you can see, there are fields separated by commas. For each car the file contains the following information:

1. mpg: the miles per gallon
2. cylinders: the number of cylinders in the engine
3. displacement: the total volume of all cylinders the engine in centiliters
4. horsepower: the power of the engine in horsepower
5. weight: the weight of the car in pounds
6. acceleration: time in seconds to accelerate to 60 mph
7. model_year: the model year
8. origin: the area of origin
9. name: the full name of this model of car

Write a function `displacement_timeframe_cars(filename, year_start, year_end)` that can calculate the average `'displacement'` of all cars that have a `model_year` from `year_start` up to and including `year_end`.

    filename = 'data/mpg.csv'
    year_start = 72
    year_end = 80
    displacement = displacement_timeframe_cars(filename, year_start, year_end)
    print(f'The average displacement of cars between {year_start} and {year_end} is {displacement} centiliters')

Should print:

    The average displacement of cars between 72 and 80 is 195.83807829181495 centiliters
