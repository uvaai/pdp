# Exam

This is a digital exam. The exam consists of programming exercises that are purely based on input, output, and calculations. You will use these exercises to show that you can create a program from scratch.

During the exam, it is not allowed to use the internet and there is no help from teaching assistants. You are allowed to use the pdp.mprog.nl website. You will not be graded on design, but only on the correctness of your code. You do not have to comment your code, nor do you have to abide by any other styling rules (though this can greatly help you understand your code).

# Rules

- Finish all exercises in a file named `exam.py` and submit this file
- Each exercise should be done in (at least) **one** function
- Outputs should be done within the exercise's function with `return`, unless stated otherwise
- You are not allowed to use `numpy`, `pandas`, or other libraries in this exam
- Make sure the output for every exercise is printed to the screen when running your program. This is required to get the points for an exercise.

### Hints

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

# 1. Car expenses

Driving a car is expensive. To help you choose between different cars, and better understand the costs of your different options, you will write a program that can calculate the cost of driving a car. The price of fuel is €1.95 per liter, and the price of a new set of tires is €400. A tire wears out after 25.000km. Write a function `car_price_month(kilometers, fuel_economy)` that can calculate, given the driven kilometers per month (float, e.g. 2500), and the average fuel economy in liters per kilometer (float, e.g. 0.05), the average monthly cost of driving a car in euros.

For example, driving 2.500 `kilometers` with a `fuel_economy` of 0.05 would cost: €40 in tire-wear and €243,75 in fuel. Driving 1.000 `kilometers` with a `fuel_economy` of 0.1 would cost: €16 in tire-wear and €195 in fuel.

Test your code with the examples below:

    expense_total = car_price_month(2500, 0.05)
    print(expense_total)
    expense_total = car_price_month(1000, 0.1)
    print(expense_total)

Should print:

    283.75
    211.0


# 2. Triangular

*Triangular numbers* are numbers that are the result of the sum $1 + 2 + \ldots + i$ for a given value of $i$. The first *triangular number* is $1$, the second is $1 + 2 = 3$, the third is $1 + 2 + 3 = 6$, the fourth is $1 + 2 + 3 + 4 = 10$, etc..

Write a function named `triangular(n)` that returns a list of all the triangular numbers that are *smaller than* $n$.

    print(triangular(6))
    print(triangular(15))
    print(triangular(16))

Expected output:

    [1, 3]
    [1, 3, 6, 10]
    [1, 3, 6, 10, 15]

# 3. Last letters

Write a function `count_last_letters(text)` that counts the number of times letters occur as the last letter of a word in a given `text`. The function should return a dictionary that has each occurring last letter as keys, and the number of times that specific letter occurred as a value. For the text `"This is an example."` the keys would be `'s'`, `n`, and `e`. Their corresponding values would be `2`, `1`, and `1`.

    last_letters = count_last_letters('His target is another diploma is it Is it common going for more than one')
    print(last_letters)

Should print:

    {'s': 4, 't': 3, 'r': 2, 'a': 1, 'n': 2, 'g': 1, 'e': 2}

Note: You might get a different ordering when printing the keys in your dictionary. As dictionaries are essentially unordered, this is not a problem, as long as the key-value pairs in the dictionary are correct.

Hint: You can split a text with spaces into a list of words using the `.split(' ')` method.

# 4. More cars

[Download the `mgp.csv` file.](../data/mpg.csv)

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
