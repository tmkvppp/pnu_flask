#!/usr/bin/env python3
import cgi
import cgitb
import html
import http.cookies
import os

cgitb.enable()

form = cgi.FieldStorage()

delete_cookies = form.getvalue("delete_cookies")

if delete_cookies:
    print("Set-Cookie: form_counter=0")
    form_counter_from_cookie = 0
else:
    cookies = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))

    form_counter = int(cookies.get("form_counter", "0").value)
    form_counter += 1

    cookies["form_counter"] = form_counter

    print("Set-Cookie: form_counter={}".format(form_counter))

    form_counter_from_cookie = int(cookies.get("form_counter", "0").value)

print("Content-type: text/html\n")


def get_form_value(field_name):
    if field_name in form:
        return form[field_name].value
    else:
        return None


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
    <p><strong>Form Submission Counter:</strong> {4}</p>

    <form action="/cgi-bin/beer_form.py" method="post">
        <input type="submit" name="delete_cookies" value="Delete Cookies">
    </form>
</body>
</html>
""".format(
    beer_name,
    beer_type,
    food_pairing_str,
    beer_rating,
    form_counter_from_cookie
))
