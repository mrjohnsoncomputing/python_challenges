import math

def read_file(filename):
  with open(filename, "r") as file:
    data = file.read()
  return data.split(",")

def check_for_speeding(filename):
  data = read_file(filename)
  rng = math.ceil(len(data)/3)
  for i in range(rng):
    position = i * 3
    time1 = int(data[position])
    time2 = int(data[position+1])
    plate = data[position+2].strip()
    travel_time = time2 - time1
    distance = 10
    speed = distance/(travel_time/60)
    if speed > 50:
      print("A car with the registration {} has been caught going at {}mph".format(plate, round(speed, 2)))

check_for_speeding("speed_camera/data.txt")