# Exam

This is a digital exam. The exam consists of programming exercises that are purely based on input, output, and calculations. You will use these exercises to show that you can create a program from scratch.

During the exam, it is not allowed to use the internet and there is no help from teaching assistants. You will not be graded on design, but only on the correctness of your code. You do not have to comment your code, nor do you have to abide by any other styling rules (though this can greatly help you understand your code).

# Rules

- Finish all exercises in a file named `exam.py` and submit this file
- Each exercise should be done in (at least) **one** function
- Outputs should be done within the exercise's function with `return`, unless stated otherwise
- You are not allowed to use `numpy` or other libraries in this exam
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

Driving a car is expensive. To help you choose between different cars, and better understand the costs of your different options, you will write a program that can calculate the cost of driving a car. The price of fuel is €1.95 per liter, and the price of a new set of tires is €400. A tire wears out after 25.000km. Write a function `car_price_month(kilometers, fuel_economy)` that can calculate, given the driven kilometers per month (float, e.g. 2500), and the average fuel economy in liters per kilometer (float, e.g. 0.05), the monthly cost of driving a car in euros.

    expense_total = car_price_month(2500, 0.05)
    print(expense_total)

Should print:

    283.75

# 2. Speech synthesis

A number can be divided into digits. For example, the number 423 consists of the digits 4, 2 and 3. We want to use a speech synthesizer to pronounce numbers, digit by digit. So the number 423 should be pronounced as "four", "two", "three". Write a function `number_speech(number)` that accepts a number as an argument, and splits the number into separate digits. The function should return the separate digits as a list, and the result can then be printed as follows:

    numbers = number_speech(1903)
    for number in numbers:
        print(number)

Which should print the following:

    one
    nine
    zero
    three

**Hint:** remember that you can access the individual characters in a _string_ in the same way you can get the individual elements from a list.

# 3. Booklist

For school, you are required to read books from a prescribed booklist. Instead of asking you to read at least 5 books from that list, the teacher asks you to read at least 1000 pages. Of course, even though you are an eager student, you don't want to read way too much. Write a function `count_pages(book_page_count, read_books)` that, given a dictionary of books (with the title of the book as a key, and the number of pages in that book as value) and a list of titles you have read, can calculate the total number of pages in the books that you have read. The function doesn't need to take into account invalid book titles.

    books_page_count = {'Nineteen Eighty-Four': 328, 'The Very Hungry Catterpillar': 22, 'Gulliver\'s Travels': 352, 'Frankenstein': 280, 'David Copperfield': 624, 'Moby-Dick': 736, 'Ulysses': 730, 'Lord of the Flies': 224, 'To Kill a Mockingbird': 281, 'The Picture of Dorian Gray': 272,'The Hobbit': 310}

    read_books = ['The Very Hungry Catterpillar', 'The Hobbit', 'Frankenstein', 'Lord of the Flies']

    page_total = count_pages(books_page_count, read_books)
    print(f'The books {read_books} have {page_total} pages in total.')


Should print:

    The books ['The Very Hungry Catterpillar', 'The Hobbit', 'Frankenstein', 'Lord of the Flies'] have 836 pages in total.


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

  In the file are several fields separated by commas. For each car, the file contains the following information:

1. mpg: the miles per gallon
2. cylinders: the number of cylinders in the engine
3. displacement: the total volume of all cylinders the engine in centiliters
4. horsepower: the power of the engine in horsepower
5. weight: the weight of the car in pounds
6. acceleration: time in seconds to accelerate to 60 mph
7. model_year: the model year
8. origin: the area of origin
9. name: the full name of this model of car

Write a function `avg_mpg_origin(filename, origin)` that given a string containing the `origin` (`'usa'`, `'europe'`, or `'japan'`) can calculate the average `'mpg'` for all cars of that specific origin. You are allowed to assume that only existing origins get passed to the function.

    filename = 'data/mpg.csv'
    country = 'japan'
    avg_japan = avg_mpg_origin(filename, country)
    print(f'The average mpg for {country} is: {avg_japan}')

Should print:

    The average mpg for japan is: 30.450632911392397
