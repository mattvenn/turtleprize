# Conditional statements

In our programs so far we have only covered sequences and looped sequences. When we want our program to do something different depending on its environment, we need to use conditionals.

A conditional statement allows us to test if something is true, and if it is then do something different. This example does 3 different things depending on what the variable `a` is set to.

***conditional_demo.py

We have these to choose from:

* `==` exactly the same as. 2 equals signs for comparison, 1 for variable assignment.
* `>=` more than or equal to
* `>` more than
* `<=` less than or equal to
* `<` less than
* `!=` not equal to

# More turtle codes

## Filling

We can fill areas by starting a fill, moving the turtle, then ending the fill. The main functions for filling are:


* `fill_color("red")` - fills the shape with red.
* `start_fill()` - starts the fill
* `end_fill()` - ends the fill

Here's an example for a filled triangle:

***fill_demo.py

## Stamping

We can also make shapes by stamping, like a stamp and ink pad. The two main functions for this are:

* `shape()` - which selects the shape
* `stamp()` - which stamps that shape wherever the turtle is

Here's an example of changing the shape to a square and stamping it:

***stamp_demo.py

You can find out which [shapes are available for stamping here](http://docs.Python.org/2/library/turtle.html#turtle.shape)

# Enter your code to win a Raspberry Pi!

Put your name, class, school and teacher's email at the top of your entry using comments:

~~~ python
# Alice and Bob
# class 11a
# Pickwick High School
# Mrs.Smith@pickwick.sch.uk
~~~

Then email your code to us at [entries@turtleprize.com](email:entries@turtleprize.com).
We'll let your teacher know if you've won!
