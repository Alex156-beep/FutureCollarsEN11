import sys
import os
import csv
import json
import pickle


# ==================================================
#   BASE CLASS
# ==================================================

class FileEditor:
    def __init__(self, path):
        self.path = path
        self.data = []

    def load(self):
        raise NotImplementedError

    def save(self, path):
        raise NotImplementedError

    def apply_change(self, change):
        parts = change.split(",")

        if len(parts) != 3:
            print("Invalid change format:", change)
            return

        x_str, y_str, value = parts

        if not x_str.isdigit() or not y_str.isdigit():
            print("Invalid indexes:", change)
            return

        x = int(x_str)
        y = int(y_str)

        if y >= len(self.data) or x >= len(self.data[y]):
            print("Out of range:", change)
            return

        self.data[y][x] = value

    def print_data(self):
        for row in self.data:
            print(",".join(row))


# ==================================================
#   CSV EDITOR
# ==================================================

class CSVEditor(FileEditor):
    def load(self):
        with open(self.path, newline="") as f:
            self.data = list(csv.reader(f))

    def save(self, path):
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.data)


# ==================================================
#   JSON EDITOR
# ==================================================

class JSONEditor(FileEditor):
    def load(self):
        with open(self.path, "r") as f:
            self.data = json.load(f)

    def save(self, path):
        with open(path, "w") as f:
            json.dump(self.data, f)


# ==================================================
#   PICKLE EDITOR
# ==================================================

class PickleEditor(FileEditor):
    def load(self):
        with open(self.path, "rb") as f:
            self.data = pickle.load(f)

    def save(self, path):
        with open(path, "wb") as f:
            pickle.dump(self.data, f)


# ==================================================
#   FACTORY FUNCTION
# ==================================================

def get_editor(path):
    if path.endswith(".csv"):
        return CSVEditor(path)
    if path.endswith(".json"):
        return JSONEditor(path)
    if path.endswith(".pickle"):
        return PickleEditor(path)

    return None


# ==================================================
#   MAIN PROGRAM
# ==================================================

if len(sys.argv) < 3:
    print("Usage: python reader.py <src> <dst> <change1> <change2> ...")
    sys.exit()

src = sys.argv[1]
dst = sys.argv[2]
changes = sys.argv[3:]

if not os.path.isfile(src):
    print("Error: file does not exist:", src)
    print("Files in directory:")
    for f in os.listdir("."):
        print(" -", f)
    sys.exit()

editor = get_editor(src)

if editor is None:
    print("Unsupported file type.")
    sys.exit()

# Load file
editor.load()

# Apply changes
for change in changes:
    editor.apply_change(change)

# Print result
print("\nModified file content:\n")
editor.print_data()

# Save output
editor.save(dst)
print("\nSaved to:", dst)