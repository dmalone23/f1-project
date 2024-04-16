from typing import List
from cities import Location, GrandPrix
from itertools import permutations

# with open("racetrack-locations.csv", "r") as f:
gp_list: List[GrandPrix] = []
with open("racetrack-locations.csv", "r", encoding="utf-8") as f:
    for line in f.readlines()[1:]:
        line_split = line.strip().split(",")
        circuit_name = line_split[0]
        city = line_split[1]
        country = line_split[2]
        latitude = float(line_split[3])
        longitude = float(line_split[4])
        gp_list.append(
            GrandPrix(latitude, longitude, Location(circuit_name, city, country))
        )

NA = ["Las Vegas", "Austin", "Miami", "Montréal", "Mexico City"]
EU = [
    "Silverstone",
    "Imola",
    "Monte Carlo",
    "Montemeló",
    "Spielberg",
    "Mogyoród",
    "Stavelot",
    "Zandvoort",
    "Monza",
]
ME = ["Sakhir", "Jeddah", "Baku", "Lusail", "Abu Dhabi"]
AP = ["Suzuka", "Shanghai", "Melbourne", "Singapore"]
BR = ["São Paulo"]

north_america = list(filter(lambda x: x.location.city in NA, gp_list))
europe = list(filter(lambda x: x.location.city in EU, gp_list))
middle_east_etc = list(filter(lambda x: x.location.city in ME, gp_list))
asia_pacific = list(filter(lambda x: x.location.city in AP, gp_list))
brazil = list(filter(lambda x: x.location.city in BR, gp_list))

print(north_america)
print(europe)
print(middle_east_etc)
print(asia_pacific)
print(brazil)


def get_distances(gp_list):
    for gp in gp_list:
        for gp2 in gp_list:
            if gp != gp2:
                gp.add_distance_list_entry(gp2)
    new_gp = gp_list.copy()
    return new_gp


na_distances = get_distances(north_america)
eu_distances = get_distances(europe)
me_distances = get_distances(middle_east_etc)
ap_distances = get_distances(asia_pacific)


def print_distances(gp_list):
    for gp in gp_list:
        gp.print_distance_list()


print_distances(na_distances)
print_distances(eu_distances)
print_distances(me_distances)
print_distances(ap_distances)

for p in permutations(na_distances):
    pass
