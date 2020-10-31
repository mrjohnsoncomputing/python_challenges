import time, os, datetime

# Could be irrelevant
def get_leap_years(starting_year):
  current_year = time.gmtime(time.time()).tm_year
  total = 0
  for i in range(starting_year, current_year+1):
    if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
      total += 1
  return total

# Calculates time passed since given rocket launched
def get_time(rocket):  
  # Extract data from time (as stored in voyager1)
  launch_date = time.strptime(rocket["launch_date"], "%A %d %B %Y %H:%M:%S")
  
  # Convert time into seconds since Epoch (01/01/1970 00:00:00)
  launch_date_in_seconds = time.mktime(launch_date)
  

  # Calculate all leap years since launch
  # launch_year = time.gmtime(launch_date_in_seconds).tm_year
  # leap_years = get_leap_years(launch_year)
  #launch_month = time.gmtime(launch_date_in_seconds).tm_month
  #current_month = time.gmtime(time.time()).tm_month
  #months = current_month - launch_month

  # Subract above amount of seconds from current time (also in seconds since epoch)
  seconds = time.time() - launch_date_in_seconds

  # // = floor division 
  # % = modulus division

  # Find total amount of minutes
  minutes = seconds // 60

  # Find left over amount of seconds
  seconds = round(seconds % 60)
  
  # Find total amount of hours
  hours = minutes // 60 
  
  # Find left over amount of minutes
  minutes = round(minutes % 60)
  
  # Find total amount of days
  days = (hours // 24) 
  
  # Find left over amount of hours
  hours = round(hours % 24)
  
  # Find total amount of years
  years = round(days // 365.25)
  
  # Find left over amount of days
  # 365.25 is important to account for leap years
  days = round(days % 365.25)
  print("############")
  print(rocket["name"])
  print("------------")
  # print to console
  print("Years:{}\nDays:{}\nHours:{}\nMinutes:{}\nSeconds:{}".format(years, days, hours, minutes, seconds))#, end="\r")

# ship object literals - to be developed to support external data files
launches = [{"launch_date": "Monday 5 September 1977 12:56:00", "name":"Voyager 1"},{"launch_date": "Saturday 20 August 1977 14:29:00", "name":"Voyager 2"}]

def menu():
  continuing = True
  while continuing:
    list_end = 0
    for i in range(len(launches)):
      print("{}: {}".format(i+1, launches[i]["name"]))
      list_end = i + 2
    print("{}: Exit".format(list_end))
    choice = input("Please enter the number of your choice\n")
    try:
      choice = int(choice)
      continuing = False
      if choice == list_end:
        return - 1
      else:
        return choice - 1
    except ValueError:
      print("Please only enter a number")
      continuing = True


def timer_display(rocket):
  continuing = "y"
  while continuing == "y":
    for i in range(10):
      get_time(rocket)
      time.sleep(1)
      os.system("clear")
    continuing = input("Continue? y/n").lower()

# Main program Loop
def main():
  while True:
      rocket = menu()
      if rocket >= 0:
        timer_display(launches[rocket])
      else:
        break
  print("Exiting, Goodbye!")
      


# Run main program
main()