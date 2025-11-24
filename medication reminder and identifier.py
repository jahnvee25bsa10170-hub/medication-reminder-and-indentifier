# medication reminder and identifiera
import json
import time
import datetime
import os

FILE = "meds_data.json"

# create file if it doesn't exist
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        f.write("[]")


# I will just keep a tiny pill list here for ID
pill_list = [
    {"name": "Aspirin", "color": "white", "shape": "round", "imprint": "AP"},
    {"name": "Tylenol", "color": "red", "shape": "capsule", "imprint": "TY"},
    {"name": "Ibuprofen", "color": "orange", "shape": "round", "imprint": "IBU"}
]


def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)


def add_med():
    print("\n-- add medication --")
    nm = input("name: ").strip()
    tm = input("time (HH:MM): ").strip()

    stuff = load_data()
    stuff.append({"name": nm, "time": tm})
    save_data(stuff)

    print("saved.")


def identify():
    print("\n-- pill identifier --")
    c = input("color: ").lower().strip()
    sh = input("shape: ").lower().strip()
    im = input("imprint: ").upper().strip()

    matched = None
    for p in pill_list:
        if p["color"] == c and p["shape"] == sh and p["imprint"] == im:
            matched = p
            break

    if matched:
        print("this is probably:", matched["name"])
    else:
        print("no idea. not in my small list.")


def reminders():
    print("\n(reminders running... keep this on)")
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        meds = load_data()

        for m in meds:
            if m["time"] == now:
                print("\n>>> reminder:", m["name"], "at", now)

        time.sleep(60)     # check every minute


def main_menu():
    while True:
        print("\n=== meds app ===")
        print("1. add medication")
        print("2. identify pill")
        print("3. start reminders")
        print("4. exit")

        ch = input("> ").strip()

        if ch == "1":
            add_med()
        elif ch == "2":
            identify()
        elif ch == "3":
            reminders()
        elif ch == "4":
            break
        else:
            print("?? invalid")


# running
if __name__ == "__main__":
    main_menu()
