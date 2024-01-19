# Pre-Course Training: Python Basics

"The most disastrous thing that you can ever learn is your first programming language." - Alan Kay

## 1. Using Spyder

Start Spyder as was shown in the setup process:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/0708707a-a29c-433e-8d13-4c3907ae70c1)

Ignore the New Spyder Version in window and uncheck Check for updates at startup. Select Ok.

Then select the Start tour button which will give you a brief overview of the Spyder environment. We will spend time going through the tour together:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/fe329940-8877-4a7d-a08c-81de2fac2783)

Once done, you will see the following screen:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/4934f7fa-709e-47d0-937f-a5e1669d645e)

You are ready to start coding in Python!

"A good programmer is someone who always looks both ways
before crossing a one-way street." - Doug Linder

## 2. Python Basics - An Excel Example

Let us start with a simple example from an excel spreadsheet:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/9c7251df-c6fd-42c9-b868-70aed0fc1d12)

This is quite a simple data set that has age, gender, and country for 11 people. Imagine we want to extract some useful information from this table of data. Maybe let us also get some statistics on the age column, like the minimum, maximum, average, and standard deviation metrics:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/7ec5a666-999f-4dfa-af8f-4e7b81a22a69)

For example we only want to see people above the age of 30, who are male and are from South Africa. This is quite straight forward to do in excel by using the filter tab for example:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/12a2354b-65cf-40bf-8b17-403c1b4cbf9c)

Finally, let us draw a graph of age distribution:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/81b2d52b-8ff1-442f-b8c1-f65efdf50ccb)

These were simple tasks that were performed on this dataset. Now, we will be using Python to do the exact same thing…and more! Python is just another tool that you can use to analyse and process your data. So you will be learning the necessary tools to be able to achieve what we did in excel.

## 3. Writing Python Code

We will learn to use Python in a terminal which is also known as the Python interpreter. Open up Spyder and focus on the terminal which is found on the bottom right of your screen:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/e7435570-571b-4d4c-8fe9-0564284e74f2)

Input the following print("Hello World") in the terminal and press Enter:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/b90a5d6f-827b-4ee4-8278-ce92ba49a171)

You have just written and executed your first line of Python code. Python has a print command which we rather refer to as a function. What it does is it displays the contents that is inside the brackets to the screen. Let us explore some more examples, input the following:

```
print(40+2) 
name = "Python" 
print(name) 
x = 40 
y = 2 
sum = x + y 
print(sum)
```

Output:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/76ff2f1c-1b5d-414b-95c8-268991786109)

Now, we can display a lot more than just text to the screen. We can display a calculation as well, like with print(40+2). We also showed how we can create a variable called name and store the value Python inside it and then display that variable with print(name). Using variables in Python we can store numbers with x = 40 and y = 2 and create a calculation variable sum = x + y and then display it with print(sum).

You can perform some more math calculations, try the following out:

```
print(10 - 20)
print(10*20)
print(10/20)
print(10**2)
```

Output:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/32a12f23-a44e-4a39-bc68-d4d84aac15cf)

That should be straight forward to understand. The only calculation to take note of is working out the power of a number uses ** double stars.

## 4. Print Function

We can do many things with the print() function, more than we have done so far. 
We can print multiple lines of text using \n and create shapes as well. 
Input the following: print("this is line 1 \n this is line 2 \n")

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/60f68295-8fa6-4b82-9fc9-eab822a9e884)

And then input this: print("*****\n*****\n*****\n*****\n"):

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/1597a9ed-8074-4da3-b9ac-e7161e5da4f9)

We can use the print function to do many things.

## 5. Debugging

In computer coding, a "bug" refers to an error, flaw, or unintended behavior in a program's source code that causes it to produce incorrect or unexpected results.
Bugs can range from simple typos to more complex logical errors and can impact the functionality of the software.

You will make mistakes! The important thing is that you learn from them. Thankfully, Python helps you along and guides if you do make a mistake in most situations. 
For example input the following print(myname):

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/873feb16-af97-429f-9dd7-1ddc10ee3953)

You will get an error that stated NameError: name 'myname' is not defined. That is true, we are trying to display the variable myname but we have not given it a value before. This would work:

```
myname = "Mr Python Coder"
print(myname)
```

Output:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/7ed48146-08af-4516-baf9-5bfd226c8afc)

Many times things won’t work as it is expected. Remember a computer programme only does what it is told. It cannot think for you!

When things go wrong, like we saw above with NameError you will have to figure out how to fix it. Steps to take:

1. Look at your code and check if everything makes logical sense
2. Delete previous lines of code until you get to a point where you code runs and then figure it what line of code you need to fix
3. If you can’t figure it out – ask for help. Google is your friend! There are many sites like stackoverflow and similar that have posts where people have mentioned similar issues and solutions to it. You can also post questions and people will help.
4. Keep on trying!


