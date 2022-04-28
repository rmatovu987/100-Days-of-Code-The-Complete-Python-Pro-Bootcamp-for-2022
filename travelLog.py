#!/usr/bin/env python3
"""Program to add a travel log"""
from typing import List

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "German",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]


def add_new_country(country: str, visits: int, cities: List):
    """Function to add to travel log"""
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
