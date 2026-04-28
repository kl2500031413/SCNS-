import heapq
import random
from datetime import datetime

# -------------------------------
# CAMPUS GRAPH (Navigation)
# -------------------------------
campus_map = {
    "Gate": {"Admin": 2, "Library": 5},
    "Admin": {"Gate": 2, "Canteen": 4, "Lab": 6},
    "Library": {"Gate": 5, "Lab": 3},
    "Canteen": {"Admin": 4, "Hostel": 2},
    "Lab": {"Admin": 6, "Library": 3, "Hostel": 4},
    "Hostel": {"Canteen": 2, "Lab": 4}
}

# -------------------------------
# DIJKSTRA (Shortest Path)
# -------------------------------
def shortest_path(graph, start, end):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        (cost, node, path) = heapq.heappop(pq)

        if node in visited:
            continue

        path = path + [node]
        visited.add(node)

        if node == end:
            return cost, path

        for neighbor, weight in graph[node].items():
            heapq.heappush(pq, (cost + weight, neighbor, path))

    return float("inf"), []

# -------------------------------
# FACILITY MONITORING
# -------------------------------
facilities = {
    "Library": {"occupancy": 0, "power": "ON"},
    "Lab": {"occupancy": 0, "power": "ON"},
    "Canteen": {"occupancy": 0, "power": "ON"},
    "Hostel": {"occupancy": 0, "power": "ON"},
}

def update_facilities():
    for place in facilities:
        facilities[place]["occupancy"] = random.randint(0, 100)
        facilities[place]["power"] = random.choice(["ON", "OFF"])

def display_facilities():
    print("\n--- Facility Status ---")
    for place, data in facilities.items():
        print(f"{place}: Occupancy={data['occupancy']}%, Power={data['power']}")

# -------------------------------
# RESOURCE ANALYTICS
# -------------------------------
usage_log = []

def log_usage(location):
    usage_log.append((location, datetime.now()))

def show_analytics():
    print("\n--- Resource Analytics ---")
    count = {}
    for loc, _ in usage_log:
        count[loc] = count.get(loc, 0) + 1

    for loc, c in count.items():
        print(f"{loc} used {c} times")

# -------------------------------
# MAIN SYSTEM MENU
# -------------------------------
def main():
    while True:
        print("\n=== SCN-FMRA SYSTEM ===")
        print("1. Find Shortest Path")
        print("2. Show Facility Status")
        print("3. Log Facility Usage")
        print("4. Show Analytics")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            start = input("Enter start location: ")
            end = input("Enter destination: ")

            if start in campus_map and end in campus_map:
                cost, path = shortest_path(campus_map, start, end)
                print(f"Shortest Path: {' -> '.join(path)}")
                print(f"Distance: {cost}")
            else:
                print("Invalid location!")

        elif choice == "2":
            update_facilities()
            display_facilities()

        elif choice == "3":
            loc = input("Enter facility name: ")
            if loc in facilities:
                log_usage(loc)
                print("Usage logged!")
            else:
                print("Invalid facility!")

        elif choice == "4":
            show_analytics()

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid choice!")

# -------------------------------
# RUN PROGRAM
# -------------------------------
if __name__ == "__main__":
    main()
