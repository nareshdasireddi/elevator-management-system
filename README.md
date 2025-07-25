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
Enter the maximum acceptable waiting time for an elevator (in seconds): 30
Enter the floor height (in meters): 3
Enter preferred elevator capacity (press Enter to skip):

--- Elevator System Recommendation ---
... (summary output) ...

Proceeding to elevator scheduling with 3 elevators, each with capacity 12.

--- User-Driven Elevator Scheduling ---
Elevator status:
Elevator 1 at floor 1 (idle)
Elevator 2 at floor 1 (idle)
Elevator 3 at floor 1 (idle)
Enter your current floor (1-10): 1
You are on the lowest floor. Only 'up' direction is allowed.
Enter your destination floor (1-10, not 1): 5
Elevator 1 assigned to you.
  - Current floor: 1
  - Status: idle
  - Estimated arrival time: 0.0 seconds.
  - Your destination floor: 5
You have boarded Elevator 1 at floor 1.
Elevator 1 has reached your destination floor 5.
  - Current floor: 5
  - Status: idle
--- Request Summary ---
  Request: Floor 1 -> 5 (up)
  Assigned Elevator: 1
----------------------
```

## License
MIT 