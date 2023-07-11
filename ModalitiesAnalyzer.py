def state(data):
   choice = "a"
   while(True):
      try:
         choice = input("Which state would you like to get the stats of?")
         break
      except:
         print("Invalid state name.")
         continue
   schools = []
   for school in data:
      if(school[7] == choice):
         schools.append(school[3])
   modality = dict()
   #get dict
   for i in schools:
      modality[i] = modality.get(i, 0) + 1
   for k, d in modality.items():
      tempr = []
      for song in modality:
         if k == song[3]:
            tempr.append(song)
      print(f"There were {d} students who attended class in {k} in the state of {choice}.")
   
def dates(data):
   temp = []
   string = ""
   for date in data:
      if date[2] not in temp:
         temp.append(date[2])
   for date in temp:
      print(date[:-12])

def year(data):
   date = ""
   state = ""
   num = 0
   schoolz = 0
   while(True):
      try:
         print("Enter the two digit code (CA, MO, IL, TX, etc.) for a state or 'all' for all states.")
         state = input("State (2 digit code or 'all'):")
         date = input("Date (MM/DD/YYYY): ")
         break
      except:
         print("Invalid.")
         continue
   print("----------------------")
   
   schools = []
   if(state != "all"):
      for school in data:
         if(school[7] == state):
            if(school[2][:-12] == date):
               schools.append(school)
               if(school[5] != ""):
                  num = num + int(school[5])
               else:
                  if(school[5] == ""):
                     num = num + 1
               if(school[4] != ""):
                  schoolz = schoolz + int(school[4])
               else:
                  if(school[4] == ""):
                     schoolz = schoolz + 1
                     
   if(state == "all"):
      for school in data:
         if(school[2][:-12] == date):
            schools.append(school)
            if(school[5] != ""):
               num = num + int(school[5])
            else:
               if(school[5] == ""):
                  num = num + 1
            if(school[4] != ""):
               schoolz = schoolz + int(school[4])
            else:
               if(school[4] == ""):
                  schoolz = schoolz + 1
         
   print(f"Date: {date}")
   print(f"Description: {state}")
   print(f"{schoolz} schools")
   print(f"{num} students")
   count1 = 0
   count2 = 0
   count3 = 0
   count4 = 0
   count5 = 0
   count6 = 0
   for school in schools:
      if(school[3] == "In Person"):
         if(school[4] != ""):
            count1 = count1 + int(school[4])
         else:
            count1 = count1 + 1
         if(school[5] != ""):
            count4 = count4 + int(school[5])
         else:
            count4 = count4 + 1
      if(school[3] == "Hybrid"):
         if(school[4] != ""):
            count2 = count2 + int(school[4])
         else:
            count2 = count2 + 1
         if(school[5] != ""):
            count5 = count5 + int(school[5])
         else:
            count5 = count5 + 1
      if(school[3] == "Remote"):
         if(school[4] != ""):
            count3 = count3 + int(school[4])
         else:
            count3 = count3 + 1
         if(school[5] != ""):
            count6 = count6 + int(school[5])
         else:
            count6 = count6 + 1
         
   print("Schools per modality: ")
   print(f" *{count1} ({round((count1/schoolz)*100,1)}%) In Person")
   print(f" *{count2} ({round((count2/schoolz)*100,1)}%) Hybrid")
   print(f" *{count3} ({round((count3/schoolz)*100,1)}%) Remote")
   print(f"Students per modality: ")
   print(f" *{count4} ({round((count4/num)*100,1)}%) In Person")
   print(f" *{count5} ({round((count5/num)*100,1)}%) Hybrid")
   print(f" *{count6} ({round((count6/num)*100,1)}%) In Person")
         
   
def dates(data):
   temp = []
   string = ""
   for date in data:
      if date[2] not in temp:
         temp.append(date[2])
   for date in temp:
      print(date[:-12])

def dataset(data):
   while(True):
      print(f"\n{len(data)} data sets are in this file.")
      z = input("Would you like to check how many data sets are in this file again?")
      if(z == 'y' or z == 'Y'):
         continue
      else:
         break


headers = []
data = []

#open file/get header
print("Learning Modalities Analyzer")
z = ""
while True:
   try:
      name = input("Please type file path followed by a '.csv' or if home directory just type filename with .csv at the end: ")
      f = open(name)
      headers = f.readline().split(',')
      for line in f:
         data.append(line.split(','))
      f.close()
      break
   except:
      print("invalid filename or data.")
      continue


while(True):
   print("\nData analysis options:\n1. List dates.\n2. Learning modality by state on date.\n3. Number of datasets in file.\n4.Exit\n")
   choice = int(input("Enter the number of the option (1, 2, 3, or 4):"))
   if(choice == 1):
      dates(data)
   if(choice == 2):
      year(data)
      continue
   if(choice == 3):
      dataset(data)
   if(choice == 4):
      print("Thank you for using this data analyzer.")
      break

