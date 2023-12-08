#!/usr/bin/env python3
import cgi
import html  # Import the html module for escaping

print("Content-type: text/html\n")

form = cgi.FieldStorage()

# Get and escape form values
beer_name = html.escape(form.getvalue("beer_name", ""))
beer_type = html.escape(form.getvalue("beer_type", ""))
has_beer_food_pairing = form.getlist("beer_food_pairing")  # Use getlist to get multiple values as a list
beer_rating = html.escape(form.getvalue("beer_rating", ""))

# Join the list elements into a single string
food_pairing_str = ', '.join(has_beer_food_pairing)

# HTML response with escaped values
print("""
<!DOCTYPE html>
<html>
<head>
    <title>Results of the Beer Form</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Results of the Beer Form</h1>
    <p><strong>Beer Name:</strong> {0}</p>
    <p><strong>Beer Type:</strong> {1}</p>
    <p><strong>Food Pairing:</strong> {2}</p>
    <p><strong>Beer Rating:</strong> {3}</p>
</body>
</html>
""".format(
    beer_name,
    beer_type,
    food_pairing_str,
    beer_rating
))
