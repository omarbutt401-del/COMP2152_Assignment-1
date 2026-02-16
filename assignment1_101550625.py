"""
Author: Omar Butt
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"
preferred_weight_kg = 20.5
highest_reps = 25
membership_active = True


# Step c: Create a dictionary named workout_stats
workout_stats = {
    "Omar": (30, 45, 20), 
    "Jamie": (40, 35, 30),
    "Taylor": (25, 50, 35)
}


# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend, minutes in list(workout_stats.items()):
    total_minutes = sum(minutes)
    workout_stats[friend + "_Total"] = total_minutes


# Step e: Create a 2D nested list called workout_list

workout_list = [
    list(workout_stats["Omar"]),
    list(workout_stats["Jamie"]),
    list(workout_stats["Taylor"])
]


# Step f: Slice the workout_list
print("Yoga and Running minutes for all friends:")
for row in workout_list:
    print(row[:2])

print("\nWeightlifting minutes for the last two friends:")
for row in workout_list[1:]:
    print(row[2])


# Step g: Check if any friend's total >= 120

for friend in ["Omar", "Jamie", "Taylor"]:
    total = workout_stats[friend + "_Total"]
    if total >= 120:
        print(f"Good job staying active, keep it up {friend}!")


# Step h: User input to look up a friend
friend_name = input("\nEnter a friend's name: ")

if friend_name in workout_stats and isinstance(workout_stats[friend_name], tuple):
    yoga, running, weightlifting = workout_stats[friend_name]
    total = workout_stats[friend_name + "_Total"]

    print(f"\nWorkout details for {friend_name}:")
    print(f"Yoga: {yoga} minutes")
    print(f"Running: {running} minutes")
    print(f"Weightlifting: {weightlifting} minutes")
    print(f"Total: {total} minutes")
else:
    print(f"Friend {friend_name} not found in the records.")


# Step i: Friend with highest and lowest total workout minutes

totals = {
    "Alex": workout_stats["Alex_Total"],
    "Jamie": workout_stats["Jamie_Total"],
    "Taylor": workout_stats["Taylor_Total"]
}

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print("\nWorkout Summary:")
print(f"Highest total workout minutes: {highest_friend} ({totals[highest_friend]} minutes)")
print(f"Lowest total workout minutes: {lowest_friend} ({totals[lowest_friend]} minutes)")
