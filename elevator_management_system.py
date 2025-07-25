"""
Elevator Management System
- Determines the optimal number and capacity of elevators for a building
- Schedules elevators based on user-driven requests (current floor and direction)
- Prompts user for: number of floors, total people (peak), max wait time, floor height, (optional) preferred elevator capacity
- Validates all user inputs
- Uses standard elevator planning logic and reasonable assumptions
- Outputs recommendations and a summary of calculation logic
- Schedules elevator pick-up for user requests, simulates movement, and outputs assignment and ETA
- User-friendly CLI, modular and extensible
- Compatible with Python 3.x
- Intended for preliminary planning and estimation purposes only
"""

import math

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a positive number.")

def get_optional_positive_int(prompt):
    value = input(prompt)
    if not value.strip():
        return None
    try:
        value = int(value)
        if value > 0:
            return value
        else:
            print("Invalid value. Skipping preferred capacity.")
            return None
    except ValueError:
        print("Invalid value. Skipping preferred capacity.")
        return None

def get_direction(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ["up", "down"]:
            return value
        print("Invalid input. Please enter 'up' or 'down'.")

def calculate_elevator_requirements(floors, total_people, max_wait_time, floor_height, preferred_capacity=None):
    # Assumptions
    avg_stop_time = 10  # seconds per stop (door open/close, passenger movement)
    elevator_speed = 1.5  # meters per second (typical)
    peak_period = 300  # seconds (5 minutes)
    default_capacity = 12  # persons

    # Calculate round trip time (simplified):
    travel_time = (floors - 1) * floor_height / elevator_speed * 2  # up and down
    stops = floors // 2  # average stops per trip (up and down)
    stop_time = stops * avg_stop_time
    avg_trip_time = travel_time + stop_time

    # Elevator capacity
    elevator_capacity = preferred_capacity if preferred_capacity else default_capacity

    # Number of trips per elevator in peak period
    trips_per_elevator = peak_period / avg_trip_time
    people_per_elevator = trips_per_elevator * elevator_capacity

    # Number of elevators required (ceiling division)
    elevators_required = int(-(-total_people // people_per_elevator))

    # Prepare summary
    summary = {
        "floors": floors,
        "total_people": total_people,
        "max_wait_time": max_wait_time,
        "floor_height": floor_height,
        "elevator_capacity": elevator_capacity,
        "avg_trip_time": avg_trip_time,
        "trips_per_elevator": trips_per_elevator,
        "people_per_elevator": people_per_elevator,
        "elevators_required": elevators_required,
        "assumptions": {
            "avg_stop_time": avg_stop_time,
            "elevator_speed": elevator_speed,
            "peak_period": peak_period,
            "default_capacity": default_capacity
        }
    }
    return summary

def print_summary(summary):
    print("\n--- Elevator System Recommendation ---")
    print(f"Number of floors: {summary['floors']}")
    print(f"Total people (peak): {summary['total_people']}")
    print(f"Max acceptable wait time: {summary['max_wait_time']} seconds")
    print(f"Floor height: {summary['floor_height']} meters")
    print(f"Elevator capacity: {summary['elevator_capacity']} persons")
    print(f"Assumed average round trip time: {summary['avg_trip_time']:.1f} seconds")
    print(f"Estimated trips per elevator in peak period: {summary['trips_per_elevator']:.2f}")
    print(f"People served per elevator in peak period: {summary['people_per_elevator']:.2f}")
    print(f"\nRecommended number of elevators: {summary['elevators_required']}")
    print(f"Recommended capacity per elevator: {summary['elevator_capacity']} persons")
    print("\n--- Calculation Logic & Assumptions ---")
    print(f"- Average stop time per floor: {summary['assumptions']['avg_stop_time']} seconds")
    print(f"- Elevator speed: {summary['assumptions']['elevator_speed']} m/s")
    print(f"- Peak period: {summary['assumptions']['peak_period']} seconds (5 minutes)")
    print(f"- Default elevator capacity: {summary['assumptions']['default_capacity']} persons")
    print("\nThis tool is intended for preliminary planning and estimation purposes only.\n")

# --- User-Driven Scheduling Section ---
class Elevator:
    def __init__(self, eid, capacity, current_floor=1):
        self.eid = eid
        self.capacity = capacity
        self.current_floor = current_floor
        self.direction = 0  # 1 for up, -1 for down, 0 for idle
        self.passengers = 0
        self.stops = set()
        self.idle = True

    def estimated_arrival(self, request_floor, avg_stop_time, floor_height, elevator_speed):
        travel_floors = abs(self.current_floor - request_floor)
        travel_time = travel_floors * floor_height / elevator_speed
        # Add stop time if elevator is at a stop
        return travel_time + (avg_stop_time if not self.idle else 0)

    def assign_request(self, request_floor, direction):
        self.stops.add(request_floor)
        self.direction = 1 if direction == "up" else -1
        self.idle = False

    def move_to(self, request_floor):
        self.current_floor = request_floor
        self.stops.discard(request_floor)
        if not self.stops:
            self.idle = True
            self.direction = 0

    def __str__(self):
        return f"Elevator {self.eid} at floor {self.current_floor} ({'idle' if self.idle else 'moving'})"

def schedule_elevator(elevators, request_floor, direction, avg_stop_time, floor_height, elevator_speed):
    # Find the best elevator (closest and either idle or moving in the right direction)
    best_elevator = None
    best_eta = float('inf')
    for elev in elevators:
        if elev.idle or (elev.direction == (1 if direction == "up" else -1)):
            eta = elev.estimated_arrival(request_floor, avg_stop_time, floor_height, elevator_speed)
            if eta < best_eta:
                best_eta = eta
                best_elevator = elev
    return best_elevator, best_eta

def user_driven_scheduling(floors, num_elevators, elevator_capacity, floor_height):
    avg_stop_time = 10
    elevator_speed = 1.5
    elevators = [Elevator(eid=i+1, capacity=elevator_capacity) for i in range(num_elevators)]
    print("\n--- User-Driven Elevator Scheduling ---")
    while True:
        print("\nElevator status:")
        for elev in elevators:
            print(elev)
        request_floor = get_positive_int(f"Enter your current floor (1-{floors}): ")
        if not (1 <= request_floor <= floors):
            print(f"Invalid floor. Please enter a value between 1 and {floors}.")
            continue
        direction = get_direction("Enter direction you want to go (up/down): ")
        dest_floor = get_positive_int(f"Enter your destination floor (1-{floors}, not {request_floor}): ")
        if not (1 <= dest_floor <= floors) or dest_floor == request_floor:
            print(f"Invalid destination. Please enter a value between 1 and {floors}, not equal to your current floor.")
            continue
        best_elevator, eta = schedule_elevator(elevators, request_floor, direction, avg_stop_time, floor_height, elevator_speed)
        if best_elevator is None:
            print("No available elevator at the moment. Please wait.")
            continue
        best_elevator.assign_request(request_floor, direction)
        print(f"Elevator {best_elevator.eid} assigned to you.")
        print(f"  - Current floor: {best_elevator.current_floor}")
        print(f"  - Status: {'idle' if best_elevator.idle else 'moving'}")
        print(f"  - Estimated arrival time: {eta:.1f} seconds.")
        print(f"  - Your destination floor: {dest_floor}")
        # Simulate elevator moving to the request floor
        best_elevator.move_to(request_floor)
        print(f"You have boarded Elevator {best_elevator.eid} at floor {request_floor}.")
        # Simulate elevator moving to the destination floor
        best_elevator.move_to(dest_floor)
        print(f"Elevator {best_elevator.eid} has reached your destination floor {dest_floor}.")
        print(f"  - Current floor: {best_elevator.current_floor}")
        print(f"  - Status: {'idle' if best_elevator.idle else 'moving'}")
        print(f"--- Request Summary ---")
        print(f"  Request: Floor {request_floor} -> {dest_floor} ({direction})")
        print(f"  Assigned Elevator: {best_elevator.eid}")
        print(f"----------------------")
        # Optionally, ask if the user wants to make another request
        another = input("Do you want to make another request? (y/n): ").strip().lower()
        if another != 'y':
            break
    print("\n--- End of User-Driven Scheduling ---\n")

def main():
    print("\n=== Elevator Management System ===\n")
    print("Select mode:")
    print("1. Estimation (number and capacity of elevators)")
    print("2. Scheduling (user-driven elevator requests)")
    mode = input("Enter 1 or 2: ").strip()
    if mode == "1":
        floors = get_positive_int("Enter the number of floors in the building: ")
        total_people = get_positive_int("Enter the total number of people during peak hours: ")
        max_wait_time = get_positive_float("Enter the maximum acceptable waiting time for an elevator (in seconds): ")
        floor_height = get_positive_float("Enter the floor height (in meters): ")
        preferred_capacity = get_optional_positive_int("Enter preferred elevator capacity (press Enter to skip): ")
        summary = calculate_elevator_requirements(
            floors, total_people, max_wait_time, floor_height, preferred_capacity
        )
        print_summary(summary)
    elif mode == "2":
        floors = get_positive_int("Enter the number of floors in the building: ")
        num_elevators = get_positive_int("Enter the number of elevators: ")
        elevator_capacity = get_positive_int("Enter the capacity of each elevator: ")
        floor_height = get_positive_float("Enter the floor height (in meters): ")
        user_driven_scheduling(floors, num_elevators, elevator_capacity, floor_height)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main() 