d1 = dict()  # empty dict
d2 = {'AZ': 'Phoenix', 'NC': 'Raleigh', 'CA': 'Sacramento'}
d3 = {}

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(airports['YCC'])
airports['DFW'] = 'Dallas-Fort Worth'
print(airports, '\n')
print(airports['DFW'])
airports['RDU'] = 'Durham-Raleigh'
print(airports)

print('RDU' in airports)
print('ELM' in airports)

del airports['SMF']
print(airports)

print(airports.get('JFK'))
print(airports.get('JFK', 1000))
print(airports.setdefault('JFK', "Kennedy"))
print(airports)

print(len(airports))

print(airports.keys())
print(airports.values())
print(airports.items())
print()

for abbr, name in airports.items():
    print(abbr, name)
print()










