---
title: "Username Generator Challenge"
author: MrJohnsonComputing
keywords:
  - 
  - 
  - 
  - 
  - 
  - 
id: 20201031165917
tags: #python
...
# Username Generator Challenge

At MrJohnsonComputing Inc. HQ, each member of staff is given a unique username.

The username is made of three elements:

- The first letter of the person's first name
- The first four letters of the person's surname
- The last two digits of the person's birth year.

For example, Derek Jones, born in 1971, would be given the username `DJone71`.

Unfortunately Karen, the office admin, has been too busy complaining to customer service and demanding to speak to the manager that usernames have not been generated for new employees of MrJohnsonComputing Inc.

It has gotten so bad that 1,000 employees are without usernames. All of their data is stored in the file called `EmployeeData.txt`.

## Task

**Create a python program that, when it is run, will go through all of the employee data and convert it into usernames for the new staff.**

You should output the 1,000 new usernames in a file called `EmployeeUsernames.txt`.

## Extension

### Half Names
Instead of the first four letters of the person's surname, make is the first half of the person's surname. You can choose whether to round up or down on a name with an odd amount if letters.

### Storage Space
Mr Johnson will now need to store these usernames in a database. Considering his database is using extended ASCII to store characters, how much storage will these 1,000 new usernames take up?

### Longest Username
How many characters long is the longest username?