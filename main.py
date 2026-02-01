#!/usr/bin/env python3
"""
CLI: number -> person info
Usage:
  python3 main.py 101
  python3 main.py --add
  python3 main.py --update 101
  python3 main.py --list
"""
import json
import argparse
import os
import sys

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def show_info(number, data):
    key = str(number)
    info = data.get(key)
    if not info:
        print(f"No record found for number {number}")
        return
    print(f"--- Information for {number} ---")
    print(f"Name       : {info.get('name', '')}")
    print(f"Address    : {info.get('address', '')}")
    print(f"Father Name: {info.get('father', '')}")
    print(f"Mother Name: {info.get('mother', '')}")
    print("-------------------------------")


def add_entry(data):
    number = input("Enter number (unique id): ").strip()
    if not number:
        print("Number is required.")
        return
    if number in data:
        print("Number already exists. Use update to change it.")
        return
    data[number] = {
        "name": input("Name: ").strip(),
        "address": input("Address: ").strip(),
        "father": input("Father Name: ").strip(),
        "mother": input("Mother Name: ").strip(),
    }
    save_data(data)
    print("Saved.")


def update_entry(data, number):
    key = str(number)
    if key not in data:
        print("No record to update for that number.")
        return
    print("Press Enter to keep current value.")
    for field in ("name", "address", "father", "mother"):
        cur = data[key].get(field, "")
        val = input(f"{field.capitalize()} [{cur}]: ").strip()
        if val:
            data[key][field] = val
    save_data(data)
    print("Updated.")


def list_entries(data):
    if not data:
        print("No entries.")
        return
    for k, v in sorted(data.items(), key=lambda x: int(x[0]) if x[0].isdigit() else x[0]):
        print(f"{k}: {v.get('name','')}")


def main():
    parser = argparse.ArgumentParser(description="Number -> Information lookup")
    parser.add_argument("number", nargs="?", help="Number to lookup")
    parser.add_argument("--add", action="store_true", help="Add new entry")
    parser.add_argument("--update", help="Update entry by number")
    parser.add_argument("--list", action="store_true", help="List all entries")
    args = parser.parse_args()

    data = load_data()

    if args.add:
        add_entry(data)
    elif args.update:
        update_entry(data, args.update)
    elif args.list:
        list_entries(data)
    elif args.number:
        show_info(args.number, data)
    else:
        # interactive loop
        try:
            while True:
                q = input("Enter number (or 'q' to quit): ").strip()
                if q.lower() in ("q", "quit", "exit", ""):
                    break
                show_info(q, data)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")


if __name__ == "__main__":
    main()
