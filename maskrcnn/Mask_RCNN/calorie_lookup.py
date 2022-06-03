import csv

# Get the calorific values of the food item from the CSV

def get_calories(calories_datafile, food_list):
  calorific_value = 0
  file = open(calories_datafile)
  csvreader = csv.reader(file)
  calories_dict = dict((rows[0],rows[1]) for rows in csvreader)
  file.close()
  for item in food_list:
        calorific_value+=int(calories_dict[item])
    
  return calorific_value


calories_data = "calories_data.csv"
#category = ['cup_cakes']

# total_calories = get_calories(calories_data, category)
#print(total_calories)