import json
from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


def save_json(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()
date_now = datetime.now()


@app.template_filter()
def str_to_datetime(date_string):
    """
    function used to convert a string representation
    of a date and/or time into a datetime object, registered using
     the template_filter() decorator.
     """
    return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    """
     Function checking whether the entered email address is valid and registered.
     If valid and registered : display List of competitions.
     Else: display error.
    """
    # list of club corresponding to the submitted email.
    club_list = [club for club in clubs if club['email'] == request.form['email']]
    if not club_list:
        flash("That email was not found in the database. Please try again.")
        return redirect(url_for('index'))
    return render_template('welcome.html',
                           club=club_list[0],
                           competitions=competitions,
                           date_now=date_now
                           )


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    if competition and club:
        if placesRequired < 0:
            flash('You cannot book negative competition places.')
        elif placesRequired == 0:
            flash('Please chose a number between 1 and 12.')
        elif placesRequired > 12:
            flash('You cannot book more than 12 places.')
        elif placesRequired > int(competition['numberOfPlaces']):
            flash('You cannot book more than there are places available.')
        elif placesRequired > int(club['points']):
            flash('You do not have enough points to book this number of places.')
        else:
            # New competition places.
            competition['numberOfPlaces'] = str(int(competition['numberOfPlaces']) - placesRequired)

            # New club points.
            club['points'] = str(int(club['points']) - placesRequired)

            # Save competition places in JSON file
            # save_json('competitions.json', {'competitions': competitions})

            # Save club points in JSON file
            # save_json('clubs.json', {'clubs': clubs})

            # Display booking confirmation.
            flash('Great-booking complete!')
    else:
        flash("Something went wrong-please try again.")
    return render_template('welcome.html', club=club, competitions=competitions, date_now=date_now)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
