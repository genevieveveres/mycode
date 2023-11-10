#!/usr/bin/env python3

import sqlite3
import json
import uuid
from flask import Flask, render_template, request, redirect, abort, url_for
from database_tool import *

app= Flask(__name__)
app.secret_key = "Let's get cooking!"

def dbHelper():
    connection = sqlite3.connect("recipes.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    #scoop the data, dump the data
    cursor.execute("SELECT * from recipes")
    rows = cursor.fetchall()

    rowDictionaries= []

    for row in rows:
        aRowDictionary = dict(row)
        rowDictionaries.append(aRowDictionary)

    return rowDictionaries

#Return a simple form
@app.route("/")
def index():
    return render_template("homepage.html")

#Render the form to add a new recipe
@app.route("/form")
def addform():
    return render_template("recipeform.html")

#Return the collection of recipes
@app.route("/list")
def listrecipes():
    allRows = dbHelper()
    return render_template("recipelist.html",rows=allRows)

#Add a recipe to the collection
@app.route("/add", methods=["POST"])
def addrecipe():
    try:
        id = str(uuid.uuid4()) #I mean, it definitely won't be 1 2 3 4 5 or 6...
        dishname = request.form.get("name")
        category = request.form.get("cat")
        calories = request.form.get("cals")
        source = request.form.get("src")

    except Exception as err:
        return abort(err,500)
    
    with sqlite3.connect("recipes.db") as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO recipes (id, name, category, calories, source) VALUES (?, ?, ?, ?, ?)", (id, dishname, category, calories, source))
        connection.commit()
    return redirect(url_for("listrecipes"))

@app.route("/data")
def data():
    allRows= dbHelper()
    return allRows

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug = True)
