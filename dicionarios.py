people = [
  {'level': 'Júnior', 'salary': 1500}, 
  {'level': 'Pleno',  'salary': 3000}, 
  {'level': 'Sênior', 'salary': 5000}
]

junior_salaries = list()
others_salaries = list()
person = people[0]

if person['level'] == 'Júnior':
  junior_salaries.append(person['salary'])
else:
  others_salaries.append(person['salary'])
person = people[1]

if person['level'] == 'Júnior':
  junior_salaries.append(person['salary'])
else:
  others_salaries.append(person['salary'])
person = people[2]

if person['level'] == 'Júnior':
  junior_salaries.append(person['salary'])
else:
  others_salaries.append(person['salary'])
print(junior_salaries)
print(others_salaries)
