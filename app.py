#!/usr/bin/env python3
"""
Simple Flask web UI for Number -> Information.
Run: python3 app.py
"""
from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = "change-this-secret"  # local use only

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except Exception:
            return {}


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@app.route("/", methods=["GET", "POST"])
def index():
    data = load_data()
    result = None
    if request.method == "POST":
        number = request.form.get("number", "").strip()
        result = data.get(number)
        if not result:
            flash(f"No record found for number {number}", "warning")
    return render_template("index.html", result=result)


@app.route("/list")
def list_all():
    data = load_data()
    items = sorted(data.items(), key=lambda x: int(x[0]) if x[0].isdigit() else x[0])
    return render_template("list.html", items=items)


@app.route("/add", methods=["GET", "POST"])
def add():
    data = load_data()
    if request.method == "POST":
        number = request.form.get("number", "").strip()
        if not number:
            flash("Number is required.", "danger")
            return redirect(url_for("add"))
        if number in data:
            flash("Number already exists. Use update.", "danger")
            return redirect(url_for("add"))
        data[number] = {
            "name": request.form.get("name", "").strip(),
            "address": request.form.get("address", "").strip(),
            "father": request.form.get("father", "").strip(),
            "mother": request.form.get("mother", "").strip(),
        }
        save_data(data)
        flash("Saved.", "success")
        return redirect(url_for("list_all"))
    return render_template("form.html", action="Add", entry={})


@app.route("/update/<number>", methods=["GET", "POST"])
def update(number):
    data = load_data()
    entry = data.get(number)
    if not entry:
        flash("No such entry.", "danger")
        return redirect(url_for("list_all"))
    if request.method == "POST":
        entry["name"] = request.form.get("name", "").strip()
        entry["address"] = request.form.get("address", "").strip()
        entry["father"] = request.form.get("father", "").strip()
        entry["mother"] = request.form.get("mother", "").strip()
        data[number] = entry
        save_data(data)
        flash("Updated.", "success")
        return redirect(url_for("list_all"))
    return render_template("form.html", action="Update", entry=entry, number=number)


if __name__ == "__main__":
    # For Termux / local use only. In production use proper WSGI server.
    app.run(host="0.0.0.0", port=5000, debug=True)
