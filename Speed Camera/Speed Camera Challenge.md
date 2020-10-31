---
title: "Speed Camera Challenge"
author: MrJohnsonComputing
keywords:
  - 
  - 
  - 
  - 
  - 
  - 
id: 20201031170655
tags: #python
...
# Speed Camera
## Introduction
Hello! Thank goodness you are here!

We have a file called `data.txt` jam packed full of **data** that we are hoping you can use your expertise on.

The data is from a pair of motorway average speed cameras which have malfunctioned and are now no longer sending out automated fines. 

They *should* be fining all cars going above **50mph**, as there are roadworks; speeds above that number will be seriously endangering the lives of our contruction engineers. 

Luckily for us, the cameras are still recording the number plate of the cars that pass through as well as the time *(in minutes)* that each car passes through both the first camera and then the second camera, which is **10 miles** away from the first camera. 

With these times from the two cameras, we can subtract the time the car passed the first camera from the time the car passed the second camera, which will leave us with how long it took the car to travel from one camera to the other. 

We can then plug that time, as well as the distance into the below formula to work out how fast each car was travelling:
```
speed = distance / time
```
Remember that the time recorded by the cameras is in minutes, so to get the speed in miles per hour, we should probably divide our time figure by 60.

e.g. if the time was 06:30, then the speed camera would record that time as 390 *(minutes)*. 
6 *(hours)* \* 60 = 360
30 *(minutes)* + 360 = 390

## The Rules
The rules for who should get fined, and how much, are quite simple:
- Anyone going over 50mph and less than or equal to 60mph should be fined £100
- Anyone going over 60mph and less than or equal to 70mph should be fined £130
- Anyone going over 70mph and less than or equal to 99mph should be fined £200
- Anyone going equal to or over 100mph should be fined £1000 and banned from driving for 5 years. 
- Anyone driving slower than 30mph should be fined £50 also, as such slow speeds on a motorway can be just as dangerous.

## The Breif
We would like you to use your programming skills to analyse the data in `data.txt`, and print out the registration, speed and amount of the fine for each car in contravention of the rules as laid out above.  Our agents shall then use this to issue any neccessary fines.

## Consulting
Oh, one last thing, we've given you a consultant programmer to help, should you need him. He's called `Derek` and you can find him in `Consulting.md`.