#!/usr/bin/env python3
import json
import sqlite3

# read in the prepared JSON data
with open("recipes.json") as jsonfile:
    jsondata= json.load(jsonfile)

def databaseTool(jsondata):
    connection = sqlite3.connect("recipes.db")
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS recipes')

    cursor.execute('''CREATE TABLE IF NOT EXISTS recipes
                    (id TEXT PRIMARY KEY NOT NULL,
                    name TEXT,
                    category TEXT,
                    calories INTEGER,
                    source TEXT);''')

    for recipeDict in jsondata:
        cursor.execute('''INSERT INTO recipes (id, name, category, calories, source) VALUES (:id, :name, :category, :calories, :source)''', recipeDict)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    databaseTool(jsondata)