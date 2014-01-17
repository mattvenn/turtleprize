% The Turtle Prize - Lesson 2
% CPD for teachers
%

# Introduction

In lesson 1, students learnt that computer programs are written as a sequence of codes and that computers follow those codes exactly. They also started to use the python turtle library to create simple graphics.

In the 2nd lesson, students will learn more about python, the turtle library, and get better at spotting errors in their code.

# Learning objectives

* Students will learn about loops and variables
* Students will get better at spotting errors

# Resources

* 15 copies of [lesson 2 handout](lesson-2-handout.html)

# Lesson Summary

* Loops, variables and operators
* Work on your competition entry
* Sabotage!

## Hangman - 10 minutes

Start off by playing a version of hangman on the white board. This version teaches the importance of variables.

Don't record the wrong guesses, and have the students in a line, come up one by one to the board. They whisper their guess and if it's right, add the letter. If it's wrong tell them it's wrong but don't record it.

Play for a while and ask why it's harder than normal. The reason is that nobody knows all the wrong guesses because they haven't been recorded. 

As people, we take our short term memory for granted, but computers need to be told to remember important things, using a variable.

Variables have 3 important features:

* They can store some data
* They can recall that data
* The data they store can be changed

The variables we'll be using will be storing numbers.

## Variables in python - 10 minutes

Ask the students to start Idle and make a new file. Ask them to type the *variables* code in the handout. Ask them to save and run their file. Remember to add the `.py` to the end of their filename.

We use the single `=` to assign a number to a variable. Variables can be called pretty much anything, but there can be no spaces in the name. It's a good idea to call a variable a name that makes sense for what its storing.

When we use the `+` to add to the variable, we are using an `operator`. Common mathematical operators include `+, -, /, *`.

## Loops in python - 10 minutes

Ask the students to type in the code *looping* from their handouts. This can be added to the end of their current work.

Ask them to explain how the looping is working, and how it uses the variable to count the number of times the loop as run.

***loop_demo.py

1. create a new variable and store 0 inside
2. the line that creates the loop. It will only loop while loops < 20
3. prints 'hello'
4. adds 1 to the variable using the `+` operator.

## Sabotage! - 10 minutes

Explain they're going to play a game called sabotage. This game was invented by [Alan O'Donohoe](http://twitter.com/teknoteacher) to teach resiliance in dealing with syntax errors.

Each pair saves their program to a new file called 'sabotaged.py' using `file->save as`. They then make 5 deliberate syntax errors. Students will already have come across syntax errors as they are easily caused by:

* missing a : at the end of a line
* not indenting properly after a `while` loop
* getting case wrong - python is case sensitive
* not matching ( and ) brackets

After making 5 errors, one person from each team swaps to a different team. The person arriving has to try and fix the syntax errors, and it they get stuck the person who made them can give them clues.

This game is really good fun and worth using a few times until your students are really quick at spotting and fixing errors.

## Work on their turtle prize entry - 15 minutes

Encourage the students to use variables and loops in their turtle code.
The following picture shows you how to spot the ideas students are using.

\ ![looping and variables](turtlesequence.png)

1. on the left is a simple sequence
2. the center shows the same sequence, but looped 30 times with a rotation between each loop
3. the right shows the looped version, but the pattern gets a bit bigger everytime using a variable that increases every loop


## Plenary - 5 minutes

Ask how a computer remembers data. Ask for an example of when this is necessary - for instance counting the number of loops have already been run.

Ask how we repeat computer code. Ask why looping is important in coding. What python keyword do we use for creating a loop? The `while` keyword.

# Homework

* todo
* Students to continue working on their competition entry.
* code academy?

# Outcome

All students:

* Understand that a variable can be used to store and retrieve data
* That loops are used to repeat sequences of code
* That computers need the codes to be written perfectly, or syntax errors will result

Most students

* Have used a loop and a variable in their competition entry

Some students

* Have used a variable to change the drawing as a loop progresses
