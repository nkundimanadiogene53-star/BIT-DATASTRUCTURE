# ---------------- Project 93: Road Traffic Count ---------------- #

import array

# === Integers ===
# Sample traffic count data (vehicles counted at different points in a day) 
traffic_counts = [120, 250, 175, 300, 95, 410, 220]

total = sum(traffic_counts)
average = total / len(traffic_counts)
minimum = min(traffic_counts)
maximum = max(traffic_counts)
print("=== Integers ===")
print(f"Traffic Data: {traffic_counts}")
print(f"Total: {total}, Average: {average}, Min: {minimum}, Max: {maximum}\n")


# === Strings (Formatted report with f-strings) ===
report = (
    f"Road Traffic Report\n"
    f"Total vehicles counted: {total}\n"
    f"Average vehicles per checkpoint: {average:.2f}\n"
    f"Minimum recorded: {minimum}, Maximum recorded: {maximum}\n"
)
print("=== Strings ===")
print(report)


# === Booleans (Threshold condition with compound logic) ===
threshold = 200
# Compound condition: average > threshold AND maximum > 300
if average > threshold and maximum > 300:
    print("Status: Above Standard (High Traffic)\n")
else:
    print("Status: Below Standard (Normal Traffic)\n")


# === Lists ===
print("=== Lists ===")
traffic_list = traffic_counts.copy()
print("Original List:", traffic_list)

# Add a new element
traffic_list.append(180)
print("After Adding 180:", traffic_list)

# Remove values below 100 (condition-based removal)
traffic_list = [x for x in traffic_list if x >= 100]
print("After Removing <100:", traffic_list)

# Sort the list
traffic_list.sort()
print("After Sorting:", traffic_list, "\n")


# === Arrays ===
print("=== Arrays ===")
traffic_array = array.array("i", traffic_counts[:5])  # fixed-size subset
array_sum = sum(traffic_array)

print("Array Data:", traffic_array)
print("Array Sum:", array_sum)
print("Compare with List Sum (first 5):", sum(traffic_counts[:5]), "\n")


# === Dictionaries ===
print("=== Dictionaries ===")
traffic_records = [
    {"id": 1, "name": "Checkpoint A", "value": 120},
    {"id": 2, "name": "Checkpoint B", "value": 250},
    {"id": 3, "name": "Checkpoint C", "value": 175},
    {"id": 4, "name": "Checkpoint D", "value": 300},
]

# Update record
traffic_records[1]["value"] = 270  # Update B from 250 -> 270

# Delete record (remove C)
traffic_records = [rec for rec in traffic_records if rec["id"] != 3]

# Compute total values
dict_total = sum(rec["value"] for rec in traffic_records)

print("Traffic Records:", traffic_records)
print("Total Vehicles from Records:", dict_total)

print("\n--- Project Complete ---")
