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

### 1. Passwords

A website that you work for wants users to use more secure passwords. The passwords need to have at least 8 characters *(these can be letters, digits, punctuation, etc.)* and never contain two of the same character directly next to each other. The password "americano" would be an accepted password, since it has 9 letters and no character occurs twice in direct sequence. The password "espre*ss*o" would not be accepted because the character "s" occurs twice directly after one another.

Write a function `check_password(password)`, that accepts a password and returns a boolean (`True` or `False`) that indicates whether the password meets the requirements listed above. You can assume that all letters will always be lower case.

Example usage:

    passwords = ["secret", "pa55word", "sinkhole234", "1bigbeard", "butterknife", "abcdefg8", "aabbccdd18", "1two"]
    for password in passwords:
        valid = check_password(password)
        if valid:
            print(f'"{password}" is a good password')
        else:
            print(f'"{password}" is a bad password')

Expected output:

    "secret" is a bad password
    "pa55word" is a bad password
    "sinkhole234" is a good password
    "1bigbeard" is a good password
    "butterknife" is a bad password
    "abcdefg8" is a good password
    "aabbccdd18" is a bad password
    "1two" is a bad password

### 2. Cumulative Distance

We're going on a roadtrip and we have a list of the distances between each of the stops we're going to make. We would like to compute a new list with the cumulative distances instead, which gives the total distance from the start to that stop.

Write a function called `cumulative(distances)`. This function takes a list of distances and returns a new list with cumulative distances (i.e., the distances summed from the start up to that point).

Example usage:

    distances = [2, 2, 1]
    cumulative_distances = cumulative(distances)
    print(cumulative_distances)

Expected output:

    [2, 4, 5]

Example usage:

    distances = [19, 32, 7, 1, 5, 1]
    cumulative_distances = cumulative(distances)
    print(cumulative_distances)

Expected output:

    [19, 51, 58, 59, 64, 65]


### 3. Groceries and recipes

You'd like to do groceries for two recipes. In order to know how much to buy of each ingredient, you're going to write a program that can combine the ingredient overview of two recipes. The ingredients for each recipe are stored in a dictionary. It is up to you to merge them.

Write the function `combine_ingredient_dictionaries(dictionary1, dictionary2)`. That takes two dictionaries with ingredients. The output should be a new combined dictionary. If the two recipes have an overlap of ingredients, the quantities should, of course, be summed.  

Have a look a this example:

    ingredients_banana_bread = {"banana (pcs)": 3, "butter (g)": 80, "baking soda (tsp)": 0.5, "sugar (g)": 150, "egg (pcs)": 1, "flour (g)": 200}
    ingredients_brownies = {"butter (g)": 225, "sugar (g)": 450, "egg (pcs)": 5, "flour (g)": 110, "chocolate (g)": 140, "cocoa powder (g)": 55}

    shopping_list = combine_ingredient_dictionaries(ingredients_banana_bread, ingredients_brownies)
    print(shopping_list)

This should produce the output:

    {'banana (pcs)': 3, 'butter (g)': 305, 'baking soda (tsp)': 0.5, 'sugar (g)': 600, 'egg (pcs)': 6, 'flour (g)': 310, 'chocolate (g)': 140, 'cocoa powder (g)': 55}

### 4. BTTS

For this assignment you need to use the file [barca.txt](../data/barca.csv). This contains the results for football matches of F.C. Barcelona (from seasons 11/12 to 13/14). The file contains the following data:

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

Write a function `both_teams_to_score(filename)`. This function computes the percentage of matches where both teams scored and rounds it to two decimals.

Example usage:

    btts = both_teams_to_score('barca.txt')
    print(btts)

Expected output:

    0.57

You can use the file [barca_short.txt](../data/barca_short.csv) to test and debug your own code. This file contains only 4 matches.

Example usage:

    btts = both_teams_to_score('barca_short.txt')
    print(btts)

Expected output:

    0.5

Tip: You can open and load files using: `with open(filename, 'r') as f:`
