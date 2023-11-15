import json

# Sample Data
data = {
      'name' : 'Massandje Cherif',
      'age': 22,
      'city': 'Seattle,WA',
      'interests': ['Makeup','Skincare','Reading'],
      'is_student' : True

}
# Writing data to a JSON file
with open('data.json', 'w') as json_file:
     
     json.dump(data, json_file, indent=4)

print('Data has been written to data.json')


#Reading from the JSON file
with open('data.json','r') as json_file:
     #Load the data
      loaded_data =  json.load(json_file)

print('Data loaded from data.json')
print(loaded_data)


  ##Modification to the json file created
loaded_data['age'] = 28
loaded_data['interests'].append('I like pink blush')


#Write modification to the file
with open('data.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)
print('Modified data to the data.json file')