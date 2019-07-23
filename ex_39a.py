#mapping statement of abrv
states = {
    'oregeon': 'OR',
    'florida': 'FL',
    'california': 'CA',
    'New york': 'NY',
    'michicigan': 'MI'
}

#create basid set of states and cities in them
cities = {
    'CA':'san fransicio',
    'MI':'Detrioit',
    'FL': 'Jacksonville'
}

#add some more ciiteis
cities['NY'] = 'New york'
cities['OR'] = 'portand'
print(states)
print(cities)

print('-' * 10)
print("Ny state has :", cities['NY'])
print("OR state has :", cities['OR'])

print('-' * 10)
print("michigan abbrveaiton is:", states['michicigan'])
print("florida's abbrveaiton is:", states['florida'])

print('-' * 10)
print('michigan has: ', cities[states['michicigan']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviate to {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviate {abbrev}")
    print(f"and has the city {cities[abbrev]}")

print('-' * 10)
#safely get a abbreviation by a state that might not be there
state = states.get('Texas')

if not state: 
    print('sorry no texas')

#get a city with  a deafualt value
city = cities.get('TX', "Does not exist")
print(f"the city of the state 'TX is {city}")