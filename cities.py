from geographiclib.geodesic import Geodesic
from typing import Dict


class Location:
    def __init__(self, circuit_name: str, city: str, country: str) -> None:
        self.circuit_name = circuit_name
        self.city = city
        self.country = country

    def __repr__(self) -> str:
        return f"{self.circuit_name},{self.city},{self.country}"

    def __str__(self) -> str:
        return (
            f"Circuit: {self.circuit_name}\n"
            f"City: {self.city}\n"
            f"Country: {self.country}\n"
        )


class GrandPrix:
    _geod = Geodesic.WGS84

    def __init__(
        self,
        latitude: float,
        longitude: float,
        location: Location,
    ) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.location = location
        self.distance_list: Dict[Location, float] = {}

    def __repr__(self) -> str:
        return f"{self.latitude},{self.longitude}," + repr(self.location)

    def __str__(self) -> str:
        return str(self.location) + (
            f"Latitude: {self.latitude}\n" f"Longitude: {self.longitude}\n"
        )

    # https://peps.python.org/pep-0484/#forward-references
    def calculate_distance(self, other: "GrandPrix") -> float:
        distance: float = round(
            self._geod.Inverse(
                self.latitude, self.longitude, other.latitude, other.longitude
            )["s12"]
            / 1000,
            3,
        )
        return distance

    def add_distance_list_entry(self, other: "GrandPrix") -> None:
        self.distance_list[other.location] = self.calculate_distance(other)

    def print_distance_list(self):
        print(
            f"distances to all tracks from {self.location.circuit_name} (in km): {self.distance_list}"
        )
