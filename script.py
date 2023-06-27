destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
    count = 0
    index = count - 1
    for i in destinations:
        count += 1
        index = count - 1
        if i == destination:
            destination_index = index
            return destination_index

def get_traveler_location(traveler):
    return traveler[1]

test_destination_index = get_destination_index(get_traveler_location(test_traveler))
print(test_destination_index)