# Lists

A list in Python is a useful way of grouping data so they can be interacted with as a whole. This way calculations can be performed on the entire collection in one go instead of each number individually.

This video, in Dutch, explains some simple applications.

![embed](https://player.vimeo.com/video/287247201)

In English, read about [lists](http://greenteapress.com/thinkpython/html/thinkpython011.html) at Think Python.

## Reference

The following code creates a new list called `staff` filled with strings (in this case names):

    staff = ["Martijn", "Ivo", "Jelle", "Maarten", "Huub", "Marianne"]

You can request a single element of a list with `[`, `]`. The following code prints "Jelle"

    my_name = staff[2]
    print(my_name)

Beware that you start counting at `0` when indexing lists. So the following code prints "Martijn":

    my_name = staff[0]
    print(my_name)

You can also manipulating the contents of a list. The following code changes the 4th element of the list, which is at index `3`, because we start with counting at `0`.

    staff[3] = "Vera"

So now the list `staff` is: `["Martijn", "Ivo", "Jelle", "Vera", "Huub", "Marianne"]`

You can add an element to the end of the list (i.e, extending it):

    staff.append("Tom")

You can loop through the elements of a list using `for`:

    measurements_science_park = [12.7, 18.8, 24.9, 14.5, 19.0]
    measurements_science_park.append(20.5)
    for measurement in measurements_science_park:
        print(f"The measurement was {measurement} degrees.")

A different way to loop through the list is by going through possible indices using `range()` and the `len()` function which gives us the number of elements in a list:

    measurements_science_park = [12.7, 18.8, 24.9, 14.5, 19.0]
    measurements_science_park.append(20.5)
    print("In total, we have {len(measurements_science_park)} measurements:")
    for i in range(len(measurements_science_park)):
        print(f"Measurement #{i} was {measurements_science_park[i]} degrees.")

This will print:

    In total, we have 5 measurements:
    Measurement #0 was 12.7 degrees.
    Measurement #1 was 18.8 degrees.
    Measurement #2 was 24.9 degrees.
    Measurement #3 was 14.5 degrees.
    Measurement #4 was 19.0 degrees.

Remember that `range()` basically returns a sequence of numbers, that can be determined as a list. This second method of going over the elements in a list can be very useful wwhen you also need the index of each element.
