import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists('env.py'):
    import env
# ignore warning since secret key is called using os.environ

# importing regex package
import re

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

# Routing


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/team")
def team():
    team_data = []
    with open("data/team.json", "r") as team_json:
        team_data = json.load(team_json)
    return render_template("team.html", page_title="The Team", team=team_data)


@app.route("/team/<playername>")
def player_details(playername):
    player_data = {}
    with open("data/team.json", "r") as team_json:
        team_data = json.load(team_json)
        for each_player_obj in team_data:
            if each_player_obj["url"] == playername:
                player_data = each_player_obj
    return render_template("player.html", player=player_data)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if request.method == "POST":
        if request.form.get("name") == '' or request.form.get("email") == '' or request.form.get("message") == '' or email_regex.match(request.form.get("email")) == None:
            flash("Hey, please check the entry! / email format")
        else:
            flash("Hey {}, we just received your message!".format(
                request.form.get("name")))
            flash("We will sent the confirmation to {} in 2 business days!".format(
                request.form.get("email")))
    return render_template("contact.html", page_title="Contact Us")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
