# Session 1 Workbook - Physical Computing

<p align="center">
    <img src="images/ICAHLOGO.png" alt="ICAHLOGO" width="300">
</p>

## How to use this workbook

Welcome back to the Physical Computing Theme!

This session will be a workshop with lots of practical exercises that you can work through at your own pace. This is to ensure that you all gain something from this course, independent of your current Python and general programming knowledge.

We will work through this sheet as follows. For each of the following chapters, the tasks are grouped into **ascending order of difficulty**. Please attempt all tasks within the Chapter, starting with the easiest, until we reach a **Checkpoint** at which I will ask you to move on to the next Chapter.

We will also cover some basics together as a class at the beginning of each chapter.

## Homework for the next Session

If you have exercises left before wrapping up today's session, please finish them as homework for the next session. **This is mandatory.** For assessing your homework, we expect a coded solution. However, if you really get stuck with an exercise, this is not a problem, and instead of program code, we need you to explain as well as you can where and how you got stuck. It is just as useful being able to describe what the problem is as it is to solve it.

## Writing Python programs on Raspberry Pi

### The Raspberry Pi computer

Raspberry Pi is a small computer the size of a credit card that you can plug into a monitor, keyboard and mouse. You can use it in the same way as you would use your desktop PC or laptop. You can generate spreadsheets, do word processing, browse the internet, and play games. It also plays high-definition video.

However, what will make it interesting for us is its capability for use in electronics projects! The main aim of the Raspberry Pi is to teach anyone how to use programming and electronics to realise their ideas. Raspberry Pi comes with a free Linux operating system that runs from an SD card, and it is powered by a USB phone charger.

<p align="center">
    <img src="images/pi3card.png" alt="The Raspberry Pi (version 3)" width="300">
    <figcaption align="center">The Raspberry Pi (version 3)</figcaption>
</p>

### The tools of the trade - the Linux terminal and a code editor

But how about (a) writing, and (b) executing Python programs on the Rasberry Pi?

For writing programs, we suggest using **Geany**, which is one of the pre-installed code editors on your Raspberry Pi. It has the handy feature that it highlights (i.e., colour-annotates) our programs as we write them, which helps a lot with their readability.

You find Geany in the Programming menue, as shown in the following picture.

<p align="center">
    <img src="images/Geany_menu_item.png" alt="Geany menue item" width="800">
    <figcaption align="center">Opening the Geany script editor</figcaption>
</p>

The user interface is rather self-explanatory, with commands like CTRL+S (save), CTRL+O (open a file) etc. working as expected. It looks like shown below. Note that the program text has been coloured automatically.

<p align="center">
    <img src="images/Geany_window.png" alt="Geany window" width="800">
    <figcaption align="center">The Geany user interface</figcaption>
</p>

But how to actually run the program, so the computer can do what we ask it to do? That's where the Linux terminal comes in handy. Look again at the main menu bar in the Figure above. The terminal is the black symbol with <kbd>**>\_**</kbd> in it, at the top of the screen. Once you've clicked on it, the below window appears.

<p align="center">
    <img src="images/Terminal_window.png" alt="The Linux terminal" width="600">
    <figcaption align="center">The Linux terminal</figcaption>
</p>

We will show you how you can run a program from within the Terminal. The most important Terminal commands are listed in the table below.

| Command       | Effect     | 
| ------------- |:-------------| 
| ```ls``` | List the contents of the current folder |
| ```cd``` _folder_ | **C**hange **d**irectory into _folder_ |
| ```cd ..``` | Change into the parent folder of the current folder |
| ```cd``` | ```cd``` without argument changes back to the user's home folder (/home/pi) |
| ```pwd``` | **P**resent **w**orking **d**irectory. This prints out the location of the current folder. |
| ```python3``` _program.py_ | Run the program called _program.py_ in Python 3 |

Hint: You can use tab completion. For example, when typing ```cd```+<kbd>Tab</kbd>, the Terminal automatically lists all possible folders that are available for changing into.

Long story short - the Terminal is much like a text-based file explorer, bolted together with a powerful general "command centre" for your computer. You can also start the usual programs from within the terminal. Just type ```chromium```+<kbd>Enter</kbd>.

## Chapter 1 - Consolidating our Python skills

First off, are there any questions from the last session or the homework?

### Basic Python: Variables, Operators, Data Types

Most programming languages hold data in variables. Just like in Mathematics, variables in Python are a convenient way to refer to a quantity through a memorable name.

You can try this out in your notebook:

```Python
number_of_hands = 2 # Hold the value 2 in a variable called "number_of_hands"
fingers_per_hand = 5 # Hold the value 3 in a variable called "fingers_per_hand"
number_of_fingers = number_of_hands * fingers_per_hand # What value will this be?
```

Note that variable names must start with a letter and should only contain letters, numbers and underscores.

In this example, we used hashtags at the beginning of code lines to mark **comments**, which are not executed.

Programming languages use different **data types** for different types of data. It's horses for courses with this, and unsurprisingly Python supports text, integers, floating point and Boolean data, to name a few.

Let's try this out! In your notebook, type the following:

```python
x  = 1
some_text = "Hello World!"
some_boolean = False
print(x)
print(some_text)
print(some_boolean)
```

The first three lines assign values to three variables called `x`, `some_text`, `some_boolean`, and the last three lines use Python's built-in `print` function that prints them out. When you've typed this into a cell, press the `run cell, select below` button.

We can perform mathematical calculations in Python using the basic operators +, -, \*, /, \*\*, %. Try it out in your notebook (no need to use the print function in this case):

```python
4 + 5
4 - 3
2 * 3
3 / 4
2 ** 3
10 % 7 # Returns the remainder of a division
```

In Python, the [standard order of operations](https://en.wikibooks.org/wiki/Python_Programming/Basic_Math) is from left to right, and respects the mathematical precedence of operations (memorised by many as PEMDAS):

| Name        | Syntax     | Description  |
| ------------- |:-------------:| :-----|
| **P**arentheses     | ( ... ) | Happening before operating on anything else.|
| **E**xponents     | **  |  Exponents are evaluated before multiplication and division. |
| **M**ultiplication and **D**ivision | * / |  Multiplication is rapid addition and must happen first. |
| **A**ddition and **S**ubtraction | + -  |     |

Let's try it:

```python
3 / 4 * 5  # First division and then multiplication
3.0 / 4 * 5
(3.0 / 4) * 4
2 ** 8
10 % 7 # Remainder of a division
```

The following table lists Python's comparison operators:

| Name        | Syntax     |
| :-------------: |:-------------|
| < | Less than|
| > | Greater than|
| <=| Less than or equal to|
|>=	| Greater than or equal to|
|==	| Equal to|
|!=	| Not equal to|

You can check how these work in your notebook:

```python
2 == 3
3 == 3
2 < 3
True == (False != True)
```

The output will be

```python
False
True
False
True # Can you explain this?
```

There are more operators, which you can read about [here](https://www.tutorialspoint.com/python/python_basic_operators.htm).

### Strings, Lists and Indexing

The data stored in memory can be of different types; Python has five: **Numbers** and **Strings**, which we have encountered above, and also **List**, which we will touch upon below. (We won't have time to cover the [**Tuple**](https://www.tutorialspoint.com/python/python_tuples.htm) and [**Dictionary**](https://www.tutorialspoint.com/python/python_dictionary.htm) types.)

You can check the data types in your notebook:

```python
type(number_of_hands) # Number
type(fingers_per_hand)
type(some_text) # String
```

**Strings** in Python are a set of characters represented by the quotation marks. Python allows either a pair of single or double quotes.

**Lists** are the most versatile data types in Python. A list contains items separated by commas and enclosed in square brackets `[ ... ]`. In Python, all the items belonging to a list can be of different data type.

The values stored in a list can be accessed using the slice operator ([] and [:]) with indexes **starting at 0 at the beginning of the list**. The last point is a popular stumbling block, so beware!

The plus (+) sign is the list concatenation operator, and the asterisk (\*) is the repetition operator.

```python
list = [ 'abc', 12 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list            # Prints complete list
print list[0]         # Prints first element of the list
print list[1:3]       # Prints elements starting from 2nd till 3rd
print list[2:]        # Prints elements starting from 3rd element
print tinylist * 2    # Prints list two times
print list + tinylist # Prints concatenated lists
'abc' + 'fgb' # Strings behave very similarly to lists, and concatenation works the same
```

### User input

The following python code accepts user input and stores it in the variable `user_name`.

```python
user_name = ''
user_name = input('Please tell me your name! ')
print('Hello, ' + user_name + ', nice to meet you.')
```

### Control Flow

We have so far seen many small bits of software that fulfil one specific task at a time (like assigning a value to a variable, or accepting user input). In order to tackle more complex tasks, we need to combine many of these items into one larger computer program. Think of programs as cooking recipes: They are a sequence of statements (i.e., lines of code), to be executed by a very quick and accurate, but also adhere-to-the-letter type of cook (your Raspberry Pi).

As programmers, we set up “paths” for the program to follow.

One simple path is shown in the figure below. Can you tell the output of the program?

<p align="center">
<img src="images/Flow1.png" alt="pin" width="90">
</p>

### Functions



### Exercises

Following on from the Introductory Session and your homework, can you solve the following tasks?

1. <p align="center"><img src="images/Flow1.png" alt="pin" width="90"></p> Implement this program in Python.
1. 
1. String manipulation. Check whether a word is a palindrome. _Palindromes_ are words that read the same forwards and backwards, for example _madame_ or _racecar_.
1. Can you program Erathostenes sieve? Can you create a program that gives all prime numbers between a lower and an upper number, for example to find all primes between 10,000 and 11,000? [More information here](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
1. Using http library. Familiarise yourself with the basic interface of the http library. can you write a program that grabs the current temperature and wind speed for a user-input location and displays it nicely in the terminal? 

## Chapter 3 - Physical Computing and the gpiozero library

TODO: include pinout image from gpiozero

### Teaching stint

### Exercises


```python

```
