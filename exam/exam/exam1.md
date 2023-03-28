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

# 1. Tax Calculation

Write a function `calculate_tax(income)` that takes one argument: `income`. The function should calculate and return the amount of tax owed on the given `income` based on the following marginal tax rates:

    Income up to $10,000 is taxed at a rate of 10%
    Income above $10,000 is taxed at a rate of 25%

An income of \\$60,000 should result in a total tax of \$13,500;

- \$1,000 for the part up to \$10,000 (10% of \$10,000)
- \$12,500 for the part over \$10,000 (25% of \$50,000)

Note that for any

Example usage:

    print(calculate_tax(60000))
    print(calculate_tax(15000))
    print(calculate_tax(5000))

Output:

    13500.0
    2250.0
    500.0

# 2. Vowels

Write a function `count_vowels(text)` that expects a `text` as its input and returns the number of vowels (a, e, i, o, u) in the text. Remember to count capitals as well!

    example_text = "Hello, world!"
    print(count_vowels(example_text))

Expected output:

    3

And:

    example_text = "Excellent eggs!"
    print(count_vowels(example_text))

Should output:

    4

# 3. Average Grades

Write a function `average_grades(grade_dict)` that takes a dictionary of student names and their grades, where the _keys_ are strings representing the student names and the _values_ are lists of integers representing their grades. The function should return a *new* dictionary where the keys are the same student names as in the input dictionary, and the values are the average grades for each student.

    grades = {
        'Alice': [6, 8, 5, 10],
        'Bob': [4, 3, 10, 10, 9],
        'Charlie': [6, 6, 6]
    }
    average_grades_dict = average_grades(grades)
    print(average_grades_dict)

Should output:

    {'Alice': 7.25, 'Bob': 7.2, 'Charlie': 6}

# 4. Cars cars cars

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

Write a function `avg_weight_cylinders(filename, cylinders)` that given a `filename` and a number of `cylinders` can calculate the average `'weight'` for all cars that have that number of cylinders. Round the weight to 2 decimals. You are allowed to assume that there are always cars that have the number of cylinders in the data.

*Note: Remember that you are not allowed to use `pandas`!*

    filename = 'mpg.csv'
    cylinders = 4
    weight = avg_weight_cylinders(filename, cylinders)
    print(f'The average weight of a car with {cylinders} cylinders is: {weight}')

Should print:

    The average weight of a car with 4 cylinders is: 2308.13
