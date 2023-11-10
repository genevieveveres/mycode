#!/usr/bin/env python3

import sqlite3 as sql
import json
import uuid
from pprint import pprint
from flask import Flask, render_template, request, redirect, abort, make_response, session
from db_builder import *

app= Flask(__name__)
app.secret_key = "Let's get cooking!"

#Return a simple form
@app.route("/")
def index():
    return render_template("homepage.html")

#Return the collection of recipes
@app.route("/list")
def listrecipes():
    return "Recipes"

#Add a recipe to the collection
@app.route("/add", methods=["POST"])
def add recipe():
    if request.form.get("name"):
        dishname = request.form.get("name")
    else:
        return about(err,500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug = True)
