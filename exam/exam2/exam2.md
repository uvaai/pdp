# Exam

This is a digital exam. The exam consists of programming exercises that are purely based on input, output, and calculations. You will use these exercises to show that you can create a program from scratch.

During the exam, it is not allowed to use the internet and there is no help from teaching assistants. You are allowed to use the pdp.mprog.nl website. You will not be graded on design, but only on the correctness of your code. You do not have to comment your code, nor do you have to abide by any other styling rules (though this can greatly help you understand your code).

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

# 1. Salary

A supermarket often has products with the promotion: "three for the price of two". When a client buys a specific number of such a product, the supermarket needs to compute the total discount.

You have to implement the function `compute_three_for_two_discount(product_price, number_of_items)` that computes the discount. The function accepts a float `product_price` (the price of a specific product), and an integer `number_of_items` (the amount of items the client bought). Think what to do when the number of items are not divisible by three: You only get a discount for every three items.

    avocado_price = 2.35
    discount1 = compute_three_for_two_discount(avocado_price, 3)
    discount2 = compute_three_for_two_discount(avocado_price, 6)
    discount3 = compute_three_for_two_discount(avocado_price, 7)
    print(f'The amount of discount for 3 avocados: {discount1}')
    print(f'The amount of discount for 6 avocados: {discount2}')
    print(f'The amount of discount for 7 avocados: {discount3}')


The expected output:


    The amount of discount for 3 avocados: 2.35
    The amount of discount for 6 avocados: 4.7
    The amount of discount for 7 avocados: 4.7


# 2. Short stories

Write a function `find_short_words(text, max_length)` that accepts a string and an integer as input: `text` and `max_length`. The function should find all words in `text` that are at most as long as  `max_length`, and return them as a list.

    example_text = "The story so far: in the beginning, the universe was created." \
                   "This has made a lot of people very angry and been widely" \
                   "regarded as a bad move."
    short_words = find_short_words(example_text, 3)
    print(short_words)

Expected output:

    ['The', 'so', 'far', 'in', 'the', 'the', 'was', 'has', 'a', 'lot', 'of', 'and', 'as', 'a', 'bad']


**Hint1:** You can use `text.split()` to split a string into a list of words.
**Hint2:** There is a tricky part: After splitting, some words will still contain punctuation marks. You can remove that using `word.strip(',.:')`.

# 3. Expense

You're writing a program that keeps track of your expenses. You're using a dictionary that keeps track of the monthly expenses in euros per category (_food_, _rent_, _internet_, _utilities_, _social activities_, etc.). Now you would like to know what percentages of you monthly expenses these categories represent.

Write a function  `euros_to_percentage()` that accepts a dictionary containing the expenses in euros. It should create a new dictionary containing the expenses in percentages.

Have a look a this example:

    expenses_january_in_euros = {'rent': 735, 'utlities': 221,
                                 'food': 167, 'social activities': 185,
                                 'internet + netflix + spotify': 58, 'phone': 25}
    expenses_january_in_percentages = euros_to_percentage(expenses_january_in_euros)
    print(expenses_january_in_percentages)

This should produce the output:

    {'rent': 52.83968368080517, 'utlities': 15.88785046728972, 'food': 12.005751258087706, 'social activities': 13.299784327821712, 'internet + netflix + spotify': 4.169662113587347, 'phone': 1.7972681524083394}

**Note:** the order in which this result is printed does not need to be the same as the example above. Check whether each category has the right value. If this is the case, your code probably works!

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

Write a function `max_cylinders(filename, origin)` that can find the maximum amount of cylinders that any car of a given `origin` has. E.g., cars from Europe have a maximum of 6 cylinders (in this dataset), but from the USA there are cars with 8 cylinders.

    filename = 'mpg.csv'
    max_cylinders_usa  = max_cylinders(filename, 'usa')
    max_cylinders_europe  = max_cylinders(filename, 'europe')
    max_cylinders_japan = max_cylinders(filename, 'japan')
    print('The car with te most cylinders in...')
    print(f'- the USA has {max_cylinders_usa} cylinders')
    print(f'- the Europe has {max_cylinders_europe} cylinders')
    print(f'- the Japan has {max_cylinders_japan} cylinders')

Should print:

    The car with te most cylinders in...
    - the USA has 8 cylinders
    - the Europe has 6 cylinders
    - the Japan has 6 cylinders
