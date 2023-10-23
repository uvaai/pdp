# Exam

This is a digital exam. The exam consists of programming exercises that are purely based on input, output, and calculations. You will use these exercises to show that you can create a program from scratch.

During the exam, it is not allowed to use the internet and there is no help from teaching assistants. You are allowed to use the pdp.mprog.nl website and the code you have written for this course. _You will not be graded on design, but only on the correctness of your code._ You do not have to comment your code, nor do you have to abide by any other styling rules (though this can greatly help you understand your code).

This exam consists of 4 exercises. Each of the exercises can be made separately and are fully independent of each other.

# Rules

- Finish all exercises in a file named `exam.py` and submit this file
- Each exercise should be done in (at least) **one** function
- Outputs should be done within the exercise's function with `return`, unless stated otherwise
- You are not allowed to use `numpy`, `pandas`, or other libraries in this exam
- You are allowed to use the pdp.mprog.nl website and the code you have written for this course.
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

<!-- # Exercises

Nothing here yet! The practice exam will be available on monday. -->

# 1. Supermarket discounts

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

**Hint:** Integer division `//` automatically rounds down the result of a division.

# 2. Short stories

Write a function `find_short_words(text, max_length)` that accepts a string and an integer as input: `text` and `max_length`. The function should find all words in `text` that are at most as long as `max_length`, and return them as a list. Assume that the text has no punctuation and that all words are separated by spaces.

    example_text = "The story so far in the beginning the universe was created This has made a lot of people very angry and been widely regarded as a bad move"
    short_words = find_short_words(example_text, 3)
    print(short_words)

Expected output:

    ['The', 'so', 'far', 'in', 'the', 'the', 'was', 'has', 'a', 'lot', 'of', 'and', 'as', 'a', 'bad']

Hint: You can split a text with spaces into a list of words using the `.split(' ')` method.

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


# 4. Shutouts

For this assignment you need to use the file [barca.csv](../data/barca.csv). This contains the results for football matches of F.C. Barcelona (from seasons 11/12 to 13/14). The file contains the following data:

    29/08/11,Villarreal,won,5,0,home
    10/09/11,Sociedad,draw,2,2,away
    17/09/11,Osasuna,won,8,0,home
    ...
    03/05/14,Getafe,draw,2,2,home
    11/05/14,Elche,draw,0,0,away
    17/05/14,Ath Madrid,draw,1,1,home

As you can see, the data fields are separated by a comma and contain the following information:

1. Date of the match
2. The opponent
3. The result: won/lost/draw
4. The number of goals for Barcelona
5. The number of goals for the opponent
6. The location: away/home

Write a function `shutouts(filename)`. That calculates how often Barcelona has won with a so-called shutout.
A shutout means that the opposing team has not scored during the entire game.

Example usage:

    wins = shutouts('barca.csv')
    print(wins)

Expected output:

    40

You can use the file [barca_short.csv](../data/barca_short.csv) to test and debug your own code. This file contains only 4 matches.


Example usage:

    wins = shutouts('barca.csv')
    print(wins)

Expected output:

    2
