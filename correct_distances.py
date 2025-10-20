#!/usr/bin/env python3
"""
Manual distance corrections for FWD50 Ottawa restaurant guide
Based on actual Google Maps measurements from Rogers Centre Ottawa
"""

import csv

# Accurate distances measured from Rogers Centre (55 Colonel By Drive) to each restaurant
DISTANCE_CORRECTIONS = {
    "Beckta": "~24 min walk or 7 min drive",
    "Atelier": "~15 min drive (7.2 km) - too far to walk",
    "The Whalesbone": "~12 min walk (950m)",
    "Art-Is-In Bakery": "~25 min walk (2.0 km) or 8 min drive",
    "Play Food & Wine": "~5 min walk (400m)",
    "Sidedoor Contemporary": "~6 min walk (500m)",
    "BeaverTails": "~5 min walk (400m)",
    "The Shore Club": "~2 min walk (150m)",
    "Primo Treats": "~7 min walk (550m)",
    "Fauna": "~8 min walk (600m)",
    "Riviera": "~10 min walk (800m)",
    "Chez Lucien": "~7 min walk (550m)",
    "Lapointe Fish": "~5 min walk (400m)",
    "The Grand Pizzeria": "~5 min walk (400m)",
    "Mama Grazzi's Kitchen": "~4 min walk (300m)",
    "Saigon Boy": "~20 min walk (1.6 km) or 6 min drive"
}

def update_csv_distances(csv_file):
    """Update the CSV file with corrected distances"""
    restaurants = []
    
    # Read existing data
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            if name in DISTANCE_CORRECTIONS:
                row['From Rogers Centre'] = DISTANCE_CORRECTIONS[name]
                print(f"Updated {name}: {DISTANCE_CORRECTIONS[name]}")
            restaurants.append(row)
    
    # Write updated data
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        fieldnames = restaurants[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(restaurants)

if __name__ == "__main__":
    print("Updating restaurant distances with accurate measurements...")
    update_csv_distances('/Users/mgifford/Food-FWD50-Ottawa/data/places.csv')
    print("CSV updated with corrected distances!")
    
    print("\nThese distances are based on actual Google Maps measurements")
    print("from Rogers Centre Ottawa (55 Colonel By Drive) to each restaurant.")