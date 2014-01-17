# The turtle prize!

## Introduction

The turtle prize was created to encourage programming skills in KS3. 
It was created by [cpd for teachers](http://cpdforteachers.com), and sponsored by:

* [raspberry pi](http://raspberrypi.org).
* [piffin electronics kits](http://piffin.co.uk).

Students learn to program by creating graphics using python's turtle library. After spending some time creating graphics, students can enter their results into the turtle prize to win a raspberry pi computer and an electronics kit.

## Learning objectives

Students will learn that programs are made up of a sequence of computer codes that have to be written exactly.

Students will learn to write a python program that draws a simple picture.

Students will understand what a computer library is.

## Resources

* Python 2.x installed on computers. 
* 15 copies of lesson 1 handout

### Checking python before the lesson

Start Idle, which comes with python. A window will pop up called the `shell`. Type in this command and press enter:

~~~ python
from turtle import *
~~~

There should be no errors or visible result from this command. If there are any errors, then probably python 3 (instead of python 2) is installed.

# Lesson Summary

* An introduction to the turtle prize
* Program your robot game
* Draw your initial with the turtle library

# An introduction to the turtle prize - 5 minutes

Tell students about the turtle prize, that we're going to create some
graphics using a computer. But we're not going to use a graphics package (that someone else wrote), we're going to write our own program!

The first lesson will be about learning some of the basics of computer programming, and learning how to draw the initial of your name with computer codes.

The second lesson will be spent creating entries for the turtle prize.

The winning entry will be judged on originality and how good it looks. The winner across all entrants and schools will win a raspberry pi and experiemnters kit.

# Programming your robot - 25 minutes

The most fundamental part of programming a computer is understanding that programs are made up of a sequence of commands.

It’s important for us to also understand that a computer doesn’t have any intelligence - it has to be told exactly what to do. So when the program is wrong, the computer does the wrong thing.

Split the students up into groups of about 7. Ask the students to design an obstacle course by moving tables or chairs about.

Tell the students one from each group will be a robot, who has to navigate from the start to the end of the course. They have to follow the instructions given to them exactly.

Ask the students what commands the robot will need, and to write them down on their handouts. For example `forward(10)` will make the robot take 10 steps.

Explain that the `10` is called an argument. Some codes need arguments, others don't.

Most courses can be solved with the following:

* left(degrees)
* right(degrees)
* forward(steps)

And we always have a `start` and `stop` code with associated sound effects!

Now ask the students to move to a obstacle course they've not created, and to write down a program using only the commands everyone's agreed on.

When all the groups are ready, get them to see how well their program works. 

You can also try it with the robot's eyes closed!

# Draw your initial - 25 minutes

Get the students to work in pairs on a computer. Show the students how to start Idle, and explain that this is the program they'll use to write the codes.

In Idle, create a new program by clicking `file->new`.

Then ask the students to copy out the first turtle program from the handout into this new window.

When everyone has finished, they need to save their files. Ask them to save their file as a combination of their names with a `.py` at the end.

| Saving the file as `turtle.py` will break the program!

So for example, Alice and Bob would save as `alicebob.py`

After all students have saved, ask them to press `f5` to run the program. If they've correctly typed the program they should have a window popped up with a horizontal line in it. Check everyone's screen to see this has happened.

Explain that everytime they make a change they should save the file `ctrl+s` and then run it with `f5`.

Now ask the students to take it in turns to create their initials using the *useful turtle commands* in the handout. 

# Plenary - 5 minutes

Ask how a computer runs a program. Check that the students understand that computers have to follow specific instructions in a sequence. If any instructions are badly written the computer will complain with an error. 

Ask what a computer library is. Check that students understand a library is a set of codes written that we can borrow instead of having to write our own. We are using the turtle library in this lesson to make it easy to draw pictures.

# Homework

Students to experiment further with the turtle library by using this [interactive turtles website](http://interactivepython.org/courselib/static/thinkcspy/PythonTurtle/helloturtle.html)

# Outcome

## All students

* Understand that computer programs are written in a sequence of instructions
* Computers are stupid, and all instructions have to be written correctly
* Can recognise basic syntax errors
* Have used python to create some simple graphics

## Most students

* Have used the turtle library to create their initial

## Some students

* Have further experimented with the other turtle commands
