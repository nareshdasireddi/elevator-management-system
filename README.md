# Elevator Management System

A unified Python program for elevator planning, estimation, and user-driven scheduling in buildings.

## Features
- Estimates the optimal number and capacity of elevators for a building based on user input
- Schedules elevators for user requests (current floor, direction, destination)
- Assigns and displays the most suitable elevator for each request
- Simulates elevator movement and updates status as it reaches the user and their destination
- Respects elevator capacity limits
- User-friendly command-line interface
- Modular and extensible code structure

## Requirements
- Python 3.x
- No external dependencies (uses only the Python standard library)

## How It Works
1. **Estimation Phase:**
    - Enter building details: number of floors, total people during peak hours, max acceptable wait time, floor height, and (optionally) preferred elevator capacity.
    - The program calculates and displays the recommended number and capacity of elevators.
2. **Scheduling Phase:**
    - The program uses the recommended number and capacity of elevators.
    - For each request, enter:
        - Your current floor
        - The direction you want to go (up or down; only valid options are shown)
        - Your destination floor
    - The system assigns the best elevator, simulates its movement, and shows a summary for each request.

## Usage
1. Run the program:
   ```bash
   python elevator_management_system.py
   ```
2. Follow the prompts for building details and elevator requests.
3. After each request, view the elevator assignment and status summary.
4. Continue making requests or exit as desired.

## Example
```
=== Elevator Management System ===

Enter the number of floors in the building: 10
Enter the total number of people during peak hours: 100
Enter the maximum acceptable waiting time for an elevator (in seconds): 10
Enter the floor height (in meters): 4
Enter preferred elevator capacity (press Enter to skip): 12

--- Elevator System Recommendation ---
Number of floors: 10
Total people (peak): 100
Max acceptable wait time: 10.0 seconds
Floor height: 4.0 meters
Elevator capacity: 12 persons
Assumed average round trip time: 98.0 seconds
Estimated trips per elevator in peak period: 3.06
People served per elevator in peak period: 36.73

Recommended number of elevators: 3
Recommended capacity per elevator: 12 persons

--- Calculation Logic & Assumptions ---
- Average stop time per floor: 10 seconds
- Elevator speed: 1.5 m/s
- Peak period: 300 seconds (5 minutes)
- Default elevator capacity: 12 persons

This tool is intended for preliminary planning, estimation, and user-driven scheduling purposes only.


Proceeding to elevator scheduling with 3 elevators, each with capacity 12.

--- User-Driven Elevator Scheduling ---

Elevator status:
Elevator 1 at floor 1 (idle)
Elevator 2 at floor 1 (idle)
Elevator 3 at floor 1 (idle)
Enter your current floor (1-10): 5
Enter direction you want to go (up/down): up 
Enter your destination floor (1-10, not 5): 10
Elevator 1 assigned to you.
  - Current floor: 1
  - Status: moving
  - Estimated arrival time: 10.7 seconds.
  - Your destination floor: 10
You have boarded Elevator 1 at floor 5.
Elevator 1 has reached your destination floor 10.
  - Current floor: 10
  - Status: idle
--- Request Summary ---
  Request: Floor 5 -> 10 (up)
  Assigned Elevator: 1
----------------------
Do you want to make another request? (y/n): y

Elevator status:
Elevator 1 at floor 10 (idle)
Elevator 2 at floor 1 (idle)
Elevator 3 at floor 1 (idle)
Enter your current floor (1-10): 2
Enter direction you want to go (up/down): up
Enter your destination floor (1-10, not 2): 10
Elevator 2 assigned to you.
  - Current floor: 1
  - Status: moving
  - Estimated arrival time: 2.7 seconds.
  - Your destination floor: 10
You have boarded Elevator 2 at floor 2.
Elevator 2 has reached your destination floor 10.
  - Current floor: 10
  - Status: idle
--- Request Summary ---
  Request: Floor 2 -> 10 (up)
  Assigned Elevator: 2
----------------------
Do you want to make another request? (y/n): y

Elevator status:
Elevator 1 at floor 10 (idle)
Elevator 2 at floor 10 (idle)
Elevator 3 at floor 1 (idle)
Enter your current floor (1-10): 10
You are on the highest floor. Only 'down' direction is allowed.
Enter your destination floor (1-10, not 10): 5
Elevator 1 assigned to you.
  - Current floor: 10
  - Status: moving
  - Estimated arrival time: 0.0 seconds.
  - Your destination floor: 5
You have boarded Elevator 1 at floor 10.
Elevator 1 has reached your destination floor 5.
  - Current floor: 5
  - Status: idle
--- Request Summary ---
  Request: Floor 10 -> 5 (down)
  Assigned Elevator: 1
----------------------
Do you want to make another request? (y/n): y

Elevator status:
Elevator 1 at floor 5 (idle)
Elevator 2 at floor 10 (idle)
Elevator 3 at floor 1 (idle)
Enter your current floor (1-10): 1
You are on the lowest floor. Only 'up' direction is allowed.
Enter your destination floor (1-10, not 1): 5
Elevator 3 assigned to you.
  - Current floor: 1
  - Status: moving
  - Estimated arrival time: 0.0 seconds.
  - Your destination floor: 5
You have boarded Elevator 3 at floor 1.
Elevator 3 has reached your destination floor 5.
  - Current floor: 5
  - Status: idle
--- Request Summary ---
  Request: Floor 1 -> 5 (up)
  Assigned Elevator: 3
----------------------
Do you want to make another request? (y/n): y

Elevator status:
Elevator 1 at floor 5 (idle)
Elevator 2 at floor 10 (idle)
Elevator 3 at floor 5 (idle)
Enter your current floor (1-10):
```

## License
MIT 