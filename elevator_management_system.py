"""
Elevator Management System
- Determines the optimal number and capacity of elevators for a building
- Prompts user for: number of floors, total people (peak), max wait time, floor height, (optional) preferred elevator capacity
- Validates all user inputs
- Uses standard elevator planning logic and reasonable assumptions
- Outputs recommendations and a summary of calculation logic
- User-friendly CLI, modular and extensible
- Compatible with Python 3.x
- Intended for preliminary planning and estimation purposes only
"""

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

def main():
    print("\n=== Elevator Management System ===\n")
    floors = get_positive_int("Enter the number of floors in the building: ")
    total_people = get_positive_int("Enter the total number of people during peak hours: ")
    max_wait_time = get_positive_float("Enter the maximum acceptable waiting time for an elevator (in seconds): ")
    floor_height = get_positive_float("Enter the floor height (in meters): ")
    preferred_capacity = get_optional_positive_int("Enter preferred elevator capacity (press Enter to skip): ")

    summary = calculate_elevator_requirements(
        floors, total_people, max_wait_time, floor_height, preferred_capacity
    )
    print_summary(summary)

if __name__ == "__main__":
    main() 