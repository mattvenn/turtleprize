# Conditionals

~~~ { .python .numberLines }
a = 5
if a == 3:
    print "a equals 3"
elif a > 10:
    print "a is more than 10"
else:
    print "a is less than 10, and not 3"
~~~

# More turtle codes

## Filling

We can fill areas by starting a fill, moving the turtle, then ending the fill. The main functions for filling are:


* `fill_color("red")` - fills the shape with red.
* `start_fill()` - starts the fill
* `end_fill()` - ends the fill

Here's an example for a filled triangle:

***fill_triangle.py

## Stamping

We can also make shapes by stamping, like a stamp and ink pad. The two main functions for this are:

* `shape()` - which selects the shape
* `stamp()` - which stamps that shape wherever the turtle is

Here's an example of changing the shape to a square and stamping it:

***stamp_example.py
