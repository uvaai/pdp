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

# 1. Pizza party

Write a function `pizza_party(people, pizzas)` that takes two arguments: the number of `people` and the number of `pizzas`. The function should calculate and return two values together as a tuple: first, the number of slices each person will get, and second, the number of slices that are left. Assume each of the `pizzas` has 8 slices and all slices are divided equally among the `people`.

You can test your function with the following examples:

    slices_per_person, leftover_slices = pizza_party(8, 4)
    print(f"Each person gets {slices_per_person} slices of pizza.")
    print(f"There are {leftover_slices} leftover slices.")

    slices_per_person, leftover_slices = pizza_party(10, 3)
    print(f"Each person gets {slices_per_person} slices of pizza.")
    print(f"There are {leftover_slices} leftover slices.")

Expected utput:

    Each person gets 4 slices of pizza.
    There are 0 leftover slices

    Each person gets 2 slices of pizza.
    There are 2 leftover slices.

# 2. Short

It can be very tedious to summarize text in a useful way. So let's not do that. If we want to reduce a text by 25%, it's much easier to remove every 4th word. So, the sentence "I was offended by the suggestion that my baby brother was a jewel thief." Would become "I was offended the suggestion that baby brother was jewel thief.", removing "by", "my" and "a", being the 4th, 8th and 12th word respectively.

Write a function `silly_abridge(text, step)` that removes every `step`-th word from a list `text` and returns the result.

Have a look at this example:

    alice = ['Oh,', 'how', 'I', 'wish', 'I', 'could', 'shut', 'up', 'like', 'a', 'telescope', 'I', 'think', 'I', 'could', 'if', 'only', 'I', 'knew', 'how', 'to', 'begin']

    silly = silly_abridge(alice, 4)
    print(silly)
    silly = silly_abridge(alice, 2)
    print(silly)

Expected output:

    ['Oh,', 'how', 'I', 'I', 'could', 'shut', 'like', 'a', 'telescope', 'think', 'I'
    , 'could', 'only', 'I', 'knew', 'to', 'begin']
    ['Oh,', 'I', 'I', 'shut', 'like', 'telescope', 'think', 'could', 'only', 'knew',
    'to']

**Hint:** Do not remove the elements from the list, but construct a new list with only the desired elements!

# 3. Distribution

We have a dictionary containing the grades of students for a specific test. We would like to generate a distribution of grades for that class (i.e., an overview showing the frequency of each grade.)

Write a function called `calculate_distribution(grades)` that takes a dictionary of students grade and returns a dictionary showing how often each grade was given.

You may assume that grades are on a scale of 1 to 10, and that grades are always whole numbers (integers). So the possible grades are: 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10.

Have a look at this example:

    grades1 = {'Albert': 7, 'Marie': 9, 'Olivier': 7, 'Tom': 9, 'Elio': 7}
    grades2 = {'Albert': 3, 'Marie': 8, 'Olivier': 8, 'Tom': 8, 'Elio': 9}
    dist1 = calculate_distribution(grades1)
    dist2 = calculate_distribution(grades2)
    print(dist1)
    print(dist2)

This should produce the following output:

    {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 3, 8: 0, 9: 2, 10: 0}
    {1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 3, 9: 1, 10: 0}

See for example that the first dictionary shows that in `grades1` three students got a 7.

# 4. Classics

[Download the `film.csv` file.](../data/film.csv)

The file `film.csv` contains data of over a 1000 films from before the 2000s. In this exercise, you will use `film.csv` to answer a question about the data. The contents of the file look as follows:

    Year;Length;Title;Subject;Actor;Actress;Director;Popularity;Awards
    1990;111.0;Tie Me Up! Tie Me Down!;Comedy;Banderas, Antonio;Abril, Victoria;Almodvar, Pedro;68.0;No
    1991;113.0;High Heels;Comedy;Bos, Miguel;Abril, Victoria;Almodvar, Pedro;68.0;No
    1983;104.0;Dead Zone, The;Horror;Walken, Christopher;Adams, Brooke;Cronenberg, David;79.0;No
    ...
    1987;103.0;Heat;Mystery;Reynolds, Burt;Young, Karen;Jameson, Jerry;69.0;No
    1947;87.0;Night Is My Future;Drama;Malmsten, Birger;Zetterling, Mai;Bergman, Ingmar;17.0;No
    1990;92.0;Witches, The;Science Fiction;Fisher, Jasen;Zetterling, Mai;Roeg, Nicolas;18.0;No

As you can see, the fields in this file are separated by semicolons (`';'`). The films have no particular order, and for each film the file contains the following information:

1. Year: the year in which the film was released
2. Length: the duration of the film in minutes
3. Title: the title of the film
4. Subject: the genre of the film
5. Actor: the name of the main actor in the movie
6. Actress: the name of the main actress in the movie
7. Director: the name of the director of the movie
8. Popularity: the popularity of the movie on a scale from 0 to 100
9. Awards: whether the movie has gotten an award (Yes/No)

The columns with names always only contain one name.

Write a function `get_popularity_person(filename, person)` that given a `filename` and the name of a `person` can count the number of films that had that person as an **actor, actress, or director**. You do not have to re-format the person's name.

    filename = 'film.csv'
    person = 'Hitchcock, Alfred'
    popularity = get_popularity_person(filename, person)
    print(f'The number of films that {person} worked on is: {popularity}')

    person = 'Eastwood, Clint'
    popularity = get_popularity_person(filename, person)
    print(f'The number of films that {person} worked on is: {popularity}')

    person = 'Streisand, Barbra'
    popularity = get_popularity_person(filename, person)
    print(f'The number of films that {person} worked on is: {popularity}')

Should print:

    The number of films that Hitchcock, Alfred worked on is: 28
    The number of films that Eastwood, Clint worked on is: 18
    The number of films that Streisand, Barbra worked on is: 4

Note that sometimes, a person is both an actor/actress **and** a director in a film. In that case, we still only count that film once.
