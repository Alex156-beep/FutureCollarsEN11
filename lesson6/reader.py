import sys
import os
import csv

# --- Check arguments ---
if len(sys.argv) < 3:
    print("Usage: python reader.py <src> <dst> <change1> <change2> ...")
    sys.exit()

src = sys.argv[1]
dst = sys.argv[2]
changes = sys.argv[3:]

# --- Check if source file exists ---
if not os.path.isfile(src):
    print("Error: file does not exist:", src)
    print("Files in this directory:")
    for f in os.listdir("."):
        print(" -", f)
    sys.exit()

# --- Load CSV ---
with open(src, newline="") as file:
    data = list(csv.reader(file))

# --- Apply all changes ---
for change in changes:
    parts = change.split(",")

    if len(parts) != 3:
        print("Invalid format:", change)
        continue

    col_str, row_str, value = parts

    if not col_str.isdigit() or not row_str.isdigit():
        print("Invalid indexes:", change)
        continue

    col = int(col_str)
    row = int(row_str)

    if row >= len(data) or col >= len(data[row]):
        print("Out of range:", change)
        continue

    data[row][col] = value

# --- Print updated CSV ---
for row in data:
    print(",".join(row))

# --- Save output ---
with open(dst, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("\nSaved to:", dst)