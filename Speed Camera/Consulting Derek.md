---
title: "Consulting Derek"
author: MrJohnsonComputing
keywords:
  - 
  - 
  - 
  - 
  - 
  - 
id: 20201031170842
tags: #python
...
# Consulting Derek
Oioi, Derek 'ere, looks like the old bill have breifed you ta snitch on a bunch of speeders. Fair play though, those speeders are pu'in innocent lives at risk, seems legit to fine 'em.

If you fink you got this, then crack on n ignore the rest. If you're wonderin' 'ow to get started or got stuck on a cer'ain part, 'opefully me advice 'ere can be some 'elp.

## Part 1 - Loading the Data
Okay, so first fing's first, we need ta load in this huge data file into our program so we can 'ave a good look a' it. 

To make our lives easier, we'll **define** a function to do this for us and call it somefin like `read_file(filename)`.

The function we're writin' should have an argument for the `filename`, so that we could use it for multiple files if we want to. 

Inside that function, we're gunna use a cheeky bit of code:
```
with open(filename, "r") as data_file:
```
This first line is real good, cos using the `with` keyword means that once we're done with readin' the file, pyfon will automa'ically close the file down for us. Just makes fings dat little bit more efficient. 

We are then usin' the `open()` function, tellin' it what filename to use and what mode to open the file in. By sayin' `"r"`, we are tellin' pyfon to use *read mode* which will let us read the con'ents of the file. 

Finally, we give the file we're opening a **variable name**, so that we can work with it in our code. I called it `data_file` in the example above, but you coulda called it anyfin, as long as it makes sense. 

Inside that `with`, we'll read the file and store it to a variable. We can use this kind of fing `data_file.read()` and store it in a **variable** in order to get all the text out of a file. 

Now outside of the `with` we will `return` that **variable** you created and stored the text of the file in, but we will use the `.split(",")` command on the end of it. 

This will mean our file will be chopped up and put into an array. It will chop it at each part that is separated by a `","` - that's why we put a comma in the brackets `()` of the `.split()` function. 
Having the data in an array will make it much easier to work with.

Finally, lets test out our function works.
You should be able to paste the following lines at the bottom of your code and get the text file printed out to your screen, chopped up into an array:
```python3
data = read_file(filename)
print(data)
```
Remember, I ain't told you everyfin you need to do, I'm leavin' the basics to you, so if it ain't workin', read through your code and check you ain't missed anyfin impor'ant out.

