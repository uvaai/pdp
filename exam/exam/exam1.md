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

# 1. Power

Utility costs are rising quick, and it is very important to know what your monthly expenses will be depending on current utility prices. To aid yourself in making a proper estimate of the monthly cost of your electricity bill, you will write a program that can calculate this. Electricity bills are made up of 2 parts: a fixed yearly usage fee of €240 and a rate for every kWh of electricity used.

We have also installed some solar panels, which can provide electricity. This produced electricity can be deducted from our used electricity. When more electricity is produced than used, the electricity company will pay us back for each kWh at the same variable rate that electricity would cost. We always pay the yearly fee of €240.

Write a function `montly_cost_electricity(usage, production, rate)` that can calculate, given the electricity `usage` per year in kWh, the electricity `production` per year from our solar panels in kWh, and the variable electricity `rate` in euros per kWh, the average **monthly** cost of electricity.

    monthly_cost = monthly_cost_electricity(0, 0, 0.48)
    print(monthly_cost)

    monthly_cost = monthly_cost_electricity(2400, 0, 0.50)
    print(monthly_cost)

    monthly_cost = monthly_cost_electricity(0, 1200, 0.10)
    print(monthly_cost)

    monthly_cost = monthly_cost_electricity(2400, 3600, 0.15)
    print(monthly_cost)

Should print:

    20.0
    120.0
    10.0
    5.0

# 2. Square pairs

Write a function `find_square_pairs(number_list)` that accepts a list of numbers, and searches for sequential pairs of numbers where the second number is the square of the first number. The function should return a list of tuples with each pair of numbers to which this rule applies.

In the list `[1, 4, 16]` for example, there are two sequential pairs: `(1, 4)` and `(4, 16)`. `4` is not the square of `1`, so our rule does not apply to the first pair. `16` is the square of `4`, so the second pair meets our requirements. In this case our function should return `[(4, 16)]`.

    number_list = [1, 4, 16]
    print(find_square_pairs(number_list))

    number_list = [1, 1, 2, 3, 9, 27, 54, 9, 81, 9]
    print(find_square_pairs(number_list))

    number_list = [9, 3, 42, 1, 4, 7, 54, 1, 21, 9]
    print(find_square_pairs(number_list))

Should print:

    [(4, 16)]
    [(1, 1), (3, 9), (9, 81)]
    []

# 3. Last letters

Write a function `count_last_letters(text)` that counts the number of times letters occur as the last letter of a word in a given `text`. The function should return a dictionary that has each occurring last letter as keys, and the number of times that specific letter occurred as a value. For the text `"This is an example."` the keys would be `'s'`, `n`, and `e`. Their corresponding values would be `2`, `1`, and `1`.

    last_letters = count_last_letters('His target is another diploma is it Is it common going for more than one')
    print(last_letters)

Should print:

    {'s': 4, 't': 3, 'r': 2, 'a': 1, 'n': 2, 'g': 1, 'e': 2}

Note: You might get a different ordering when printing the keys in your dictionary. As dictionaries are essentially unordered, this is not a problem, as long as the key-value pairs in the dictionary are correct.

Hint: You can split a text with spaces into a list of words using the `.split(' ')` method.

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
