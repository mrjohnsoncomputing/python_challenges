import random, time

def write_file(filename, arr):
  with open(filename, "w") as file:
    for i in range(len(arr)):
      txt = str(arr[i])
      if i < len(arr) - 1:
        txt += ", "
      file.write(txt)
  

def create_data(size=10):
  data = []
  for i in range(size):
    low = 5
    high = 30
    distance = 10
    hour = random.randint(0,23)
    minute = random.randint(0, 60)
    time1 = (hour * 60) + minute
    time2 = time1 + random.randint(low, high)
    data.append(time1)
    data.append(time2)
    plate = ""
    for l in range(7):
      if len(plate) == 4:
        plate += " "
      elif len(plate) != 2 and len(plate) !=3: 
        letter = chr(random.randint(65, 90))
        plate += letter
      else:
        dates = [0, 1, 5, 6]
        number = random.choice(dates)
        plate += str(number)
        number = random.randint(0,9)
        plate += str(number)
    data.append(plate)
    #time_taken = time2 - time1
    #print(mph)
    #mph = distance/(time_taken/60)
    #print("Time1: {}\nTime2: {}\nAverage Speed: {}".format(time1, time2, mph))
  return data

print("Starting speed_camera/file_generator.py")
print("File Writing Turned Off - No action was performed")
#write_file("speed_camera/data.txt", create_data(10000))
print("Ending speed_camera/file_generator.py")