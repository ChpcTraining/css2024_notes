# Exploring Python

## Jupyter Notebook

Up till now we have been using the Spyder IDE or the Python coding environment. I hope you have become familiar with it. Now there are many others out there built for different purposes. Like PyCharm and VS Code, and many many more. However, if you are learning Python and applying it to some data science application, then you have to know about Jupyter Notebooks. 

A Jupyter Notebook is an interactive web applications that facilitate creating and sharing documents that contain live code, equations, visualizations, and narrative text. They are widely used in data science, scientific research, and education.

Many teachers use it to present content, as you will see in week 2. Many tutorials on line use Jupyter Notebooks to convey ideas and principles. So it is quite important to understand how to use it, if you want to follow a tutorial or lesson. 

There is a newer version of Jupyter Notebook called Jupyter Lab, but essentialy the same thing. The latter just have more features.

### Getting Started

So the call thing about the Anaconda workspace you installed is that it has Jupyter Notebook installed already for you. So if go to you windows app, and type "Jupyter", you should see:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/41143f23-2e3c-42c7-9749-00baa74e2f51)

Click on that and you should see a windows terminal pop up and a browser window:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/41b75678-384d-40f8-a49f-1d3492d891e6)

Go to the "New" tab and click on "Python 3 (ipykernal")

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/1a0d0608-54b4-4bf1-a92b-06479e6a1cb1)

You should then see the following:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/d6f57945-a452-4a34-97a5-1ada1ce26fa9)

So what is the difference between Jupyter Notebook and a Python script file. 

Well it is more interactive, it is like a combination of a Python script and the console. You can also write in two modes, the is code the other is like a word document. This helps to explain what your doing throughout the document.

Let us see a few examples in action.

Let us go back to the one of our first lessons when we were using the country_data.csv file. We first learnt to input this data into lists. Let us do the same in a Jupyter Notebook. Enter the following list and click on "Run":

```
age = [30,40,30,49,22,35,22,46,29,25,39]
```

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/78a26b20-73cf-4156-92c9-9a315389890e)

Now to print the data of "age" to the screen we can just input "age" and click on "Run":

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/bef151c4-5232-4980-9169-baafc96234c3)

Similar to what we get in a Python console. However, now you can remove or add a cell, like you do in a script. Note you can also use the `print()` function to display it but it is not necessary.

Instead of press run you can press "Shift" + "F5" to run a cell.

Now you will notice there is drop-down that says code, if you click on you will see a few text options:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/41d27805-49d5-4ea1-8a59-1965a7205741)

Now I added some text, not code, and then an image at the end:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/93a44532-9eba-462c-a5cc-567292da3a9c)

This is what makes Jupyter Notebook really usefull for teaching as you can easily add non-code items to you Jupyter Notebook, and essentially tell a story of your code.

### Pandas

Let us try read in some data.

Let us first upload the file, do that by going to File->Open:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/8b78cef7-e037-4502-883d-0d0753a3613d)

Then click on the "Upload" button and the select the "country_data.csv":

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/776fbaa2-901c-458c-b851-b7b72bd54ae4)

Go back to your Jupyter Notebook and input the following code:

```
import pandas as pd

df = pd.read_csv("country_data.csv")

df
```

When you click on "Run", you get the following:

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/548031e9-3cc5-4b3b-b764-ba951dc83e25)

Which is quite a nice representation.

### Visualization

Now we are going to look at plotting some graphs.

![image](https://github.com/ChpcTraining/css2024_notes/assets/157092105/c44058a9-b289-402e-98cf-b8db81942de1)


### Down Sides

While Jupyter Notebooks are a popular and powerful tool for data analysis, scientific computing, and interactive programming in Python, there are some downsides and reasons why they might not be recommended for beginners, especially when just starting to learn Python:

1. Non-linear Execution:

In Jupyter Notebooks, code can be executed out of order, leading to confusion for beginners. The order in which cells are executed matters, and this can make it challenging to understand the flow of the program.

2. Hidden State:

Variables and their values persist across cells, which can make it difficult to track the state of the program. This hidden state can be confusing for beginners who are still grasping the concept of variable scope and program flow.

3. Debugging Challenges:

Debugging in Jupyter Notebooks can be more challenging compared to traditional script-based environments. Beginners may find it harder to locate and fix errors, especially when dealing with non-linear execution and hidden state.

4. Lack of Encapsulation:

Jupyter Notebooks promote an interactive and exploratory style, but they may not encourage good programming practices such as encapsulation and modularization. Beginners might miss out on essential skills for writing clean, organized, and maintainable code.

5. Dependency on Order of Execution:

Rerunning cells or running cells in a different order can lead to unexpected results. This dependency on execution order can be confusing for beginners, who might expect code to behave the same way regardless of how it's executed.

6. Limited Code Editing Features:

While Jupyter Notebooks provide a good environment for experimenting with code, they lack some of the advanced code editing features found in Integrated Development Environments (IDEs). Beginners may benefit from features like code auto-completion, linting, and integrated debugging, which are often more robust in IDEs.

7. Version Control Challenges:

Version control systems (like Git) can be more challenging to use with Jupyter Notebooks compared to traditional scripts. Tracking changes in a collaborative environment can be less straightforward. Also you are not writing a Python script, its a Jupyter Notebook file in its own format.

8. Steep Learning Curve:

Jupyter Notebooks introduce additional concepts (e.g., cells, cell types) that beginners need to understand alongside learning Python itself. This can add to the initial learning curve and potentially hinder the learning process.

While Jupyter Notebooks have their downsides, it's important to note that they are excellent tools for certain tasks, especially in data science and research. However, for beginners focused on learning Python programming fundamentals, starting with a more traditional script-based approach using a text editor or an integrated development environment (IDE) might provide a more straightforward and structured learning experience. As users become more comfortable with Python, they can then explore and incorporate Jupyter Notebooks into their workflow as needed.


## GitHub

## VS Code

## Automate the Boring Stuff

## Numerical Calculations - stdev & R^2

### Stdev

One of the outputs we showed was the standard deviation of the age list from the excel data set. Now we can do this in Python too quite easily with a built-in function but for the purposes of learning we are going to do a manual approach since we learnt all the tools needed now to do it. To work out the population standard deviation we need to do the following:

1. Calculate the mean (average) of each data set.
2. Subtract the deviance of each piece of data by subtracting the mean from each number.
3. Square each deviation.
4. Add all the squared deviations.
5. Divide the value obtained in step four by the number of items in the data set.
6. Calculate the square root of the value obtained in step five.

We have partially done this before. Let us complete the entire process:

Step 1. Given the age list we first need to find the mean of the list:

```
age=[39, 25, 29, 46, 22, 35, 22, 49, 30, 40, 30]

mean = sum(age)/len(age)

print(mean)
```

Step 2. Now we need to subtract the mean from value in the list and square the result:

We are first going to create an empty list that will store the squared differences called sq_diff_list and then we are going to create a for loop to run through each value in the age list, subtract the mean, square the result and store in the sq_diff_list variable:

```
# Create empty list
sq_diff_list = []

# Setup for loop
for i in range(len(age)):
    
    # Take average from each value in age list and square outcome. Note we square use double asterisks
    # sq_diff we are just using as a temporary variable to store the result
    sq_diff = (age[i] - mean)**2
    
    # add the results to the `sq_diff_list` list 
    sq_diff_list.append(sq_diff)
    
    # print the result
    print(sq_diff)
```

Now we need to work out the mean of the sq_diff_list and square the result:

```
mean_sq_diff = sum(sq_diff_list)/len(sq_diff_list)
print(mean_sq_diff**0.5)
```

This process was quite tedious and in practice you would not do this as there is a built-in Python function to do it as shown below:

```
import numpy
age=[39, 25, 29, 46, 22, 35, 22, 49, 30, 40, 30]
print(numpy.std(age))
```

### R^2

Unfortunately, R-squared calculation is not implemented in numpy… so we will be doing it by hand using the following code:

```
import numpy as np
hours = [29, 9, 10, 38, 16, 26, 50, 10, 30, 33, 43, 2, 39, 15, 44, 29, 41, 15, 24, 50]
results = [65, 7, 8, 76, 23, 56, 100, 3, 74, 48, 73, 0, 62, 37, 74, 40, 90, 42, 58, 100]
x = np.asarray(hours)
y = np.asarray(results)
sum_x = np.sum(x)
sum_x_2 = np.sum(np.square(x))
sum_y = np.sum(y)
sum_y_2 = np.sum(np.square(y))
sum_xy = np.sum(x*y)
print(f"sum_x = {sum_x}")
print(f"sum_x_2 = {sum_x_2}")
print(f"sum_y = {sum_y}")
print(f"sum_y_2 = {sum_y_2}")
print(f"sum_xy = {sum_xy}")
n = len(x)
print(f"n = {n}")
top = n*sum_xy - sum_x*sum_y
print(f"top = {top}")
bot_a = np.sqrt(n*sum_x_2 - np.square(sum_x))
bot_b = np.sqrt(n*sum_y_2 - np.square(sum_y))
bot = bot_a*bot_b
print(f"bot = {bot}")
R_2 = np.square(top/bot)
print(f"R_2 = {R_2}")
```

Output:

```
sum_x = 553
sum_x_2 = 19345
sum_y = 1036
sum_y_2 = 72414
sum_xy = 36814
n = 20
top = 163372
bot = 174378.40331875964
R_2 = 0.8777480188408425
```

Practically, we should just use a Python library called sklearn that can do this for us but doing the manual approach allows us to learn more about Python. 

```
import numpy as np
from sklearn.metrics import r2_score

hours = [29, 9, 10, 38, 16, 26, 50, 10, 30, 33, 43, 2, 39, 15, 44, 29, 41, 15, 24, 50]
results = [65, 7, 8, 76, 23, 56, 100, 3, 74, 48, 73, 0, 62, 37, 74, 40, 90, 42, 58, 100]

model = np.polyfit(hours, results, 1)
predict = np.poly1d(model)

print(r2_score(results, predict(hours)))
```

Output:

```
0.8777480188408424
```




## Stack Overflow

## OfferZen

## Running Python Code on a Server

Bash Scripts + Python

## Streamlit

## Other Topics

### Is Python Enough?

## Review Topics

## Learning Resources



## HPC
