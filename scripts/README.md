# Distance Correction Script

This Python script updates the FWD50 Ottawa restaurant guide with accurate walking distances from Rogers Centre Ottawa to each restaurant.

## Overview

The `correct_distances.py` script contains manually verified walking distances based on actual Google Maps measurements from Rogers Centre Ottawa (55 Colonel By Drive) to each restaurant in the guide.

## Why This Script Exists

During the development of the FWD50 Ottawa food guide, it was discovered that initial distance estimates were significantly inaccurate. For example:
- Art-Is-In Bakery was estimated at 5 minutes but is actually 25 minutes walk
- Beckta was estimated at 8 minutes but is actually 24 minutes walk

This script ensures all distances in the CSV database are accurate and based on real-world Google Maps measurements.

## Features

- **Manually Verified Distances**: All distances have been manually checked using Google Maps
- **Multiple Transport Options**: Includes both walking and driving times where relevant
- **CSV Integration**: Updates the main `places.csv` file with corrected distances
- **Progress Reporting**: Shows which restaurants are being updated

## Usage

```bash
# From the project root directory
python3 scripts/correct_distances.py
```

The script will:
1. Read the current `data/places.csv` file
2. Update distances for restaurants that have corrections
3. Write the updated data back to the CSV file
4. Display which restaurants were updated

## Distance Format

Distances are formatted as:
- `~X min walk` for short distances
- `~X min walk or Y min drive` for longer distances  
- `~X min drive - too far to walk` for very long distances

## Requirements

- Python 3.x
- No external dependencies required (uses only standard library)

## File Structure

```
scripts/
├── correct_distances.py    # Main distance correction script
└── README.md              # This documentation file
```

## Accuracy

All distances in this script have been manually verified using Google Maps directions from Rogers Centre Ottawa to each restaurant address. These measurements reflect real walking routes and typical travel times.

## Contributing

If you find any distance inaccuracies:
1. Verify the correct distance using Google Maps from Rogers Centre Ottawa
2. Update the `DISTANCE_CORRECTIONS` dictionary in `correct_distances.py`
3. Run the script to update the CSV file
4. Submit a pull request with your corrections

## Last Updated

October 2025 - All distances verified for FWD50 2025 conference