import random

PATH = "ADMIN/FileGeneration/"


def write_file(filename, arr):
  with open(PATH + filename, "w") as file:
    for i in range(len(arr)):
      txt = str(arr[i])
      if i < len(arr) - 1:
        txt += ", "
      file.write(txt)

def read_file(filename, delimiter = "\n"):
  with open(PATH + filename, "r") as file:
    data = file.read()
  return data.split(delimiter)
  
def get_male_name():
  name = random.choice(read_file("male-names.txt"))
  return name.capitalize()

def get_female_name():
  name = random.choice(read_file("female-names.txt"))
  return name.capitalize()

def get_surname():
  surname = random.choice(read_file("family-names.txt"))
  return surname.capitalize()

def create_full_name():
  gender = random.randint(1,2)
  name = ""
  if gender == 1:
    name = get_male_name()
  else:
    name = get_female_name()
  return name + " " + get_surname()

def create_user_data():
  data = []
  dataset = 1000
  for i in range(dataset):
    name = create_full_name()
    birth_year = random.randint(1950, 2000)
    data.append(name + " " + str(birth_year))
  write_file("EmployeeData.txt", data)


def create_speed_data(size=10):
  data = []
  for i in range(size):
    low = 5
    high = 30
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
create_user_data()