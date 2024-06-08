from datetime import datetime, timedelta

# Calculate the date for last week
last_week_date = datetime.today() - timedelta(weeks=1)
last_week_date = last_week_date.strftime('%Y-%m-%d %H:%M:%S')

# Calculate the date for next week
next_week_date = datetime.today() + timedelta(weeks=1)
next_week_date = next_week_date.strftime('%Y-%m-%d %H:%M:%S')

# Calculate the date for next week
next_month_date = datetime.today() + timedelta(weeks=4)
next_month_date = next_month_date.strftime('%Y-%m-%d %H:%M:%S')


def clubs_test_data():
    return [
        {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
        {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
        {"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "12"}
    ]


def competitions_test_data():
    return [
        {"name": "Test Festival Leixlip", "date": last_week_date, "numberOfPlaces": "25"},
        {"name": "Spring Festival", "date": next_week_date, "numberOfPlaces": "25"},
        {"name": "Fall Classic", "date": next_month_date, "numberOfPlaces": "4"}
    ]
