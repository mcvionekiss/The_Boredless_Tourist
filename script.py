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

attractions = [[] for i in range(5)]
def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


def find_attractions(destination, interests):
    destination_index  = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for item in attractions_in_city:
        possible_attraction = item
        attraction_tags = possible_attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ["art"])
print(la_arts)