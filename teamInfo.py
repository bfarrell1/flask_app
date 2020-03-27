from flask import Flask, render_template


app = Flask(__name__)
application = app

import csv

def convert_to_dict(filename):
    """
    Convert a CSV file to a list of Python dictionaries
    """
    # open a CSV file - note - must have column headings in top row
    datafile = open(filename, newline='')

    # create DictReader object
    my_reader = csv.DictReader(datafile)

    # create a regular Python list containing dicts
    list_of_dicts = list(my_reader)

    # close original csv file
    datafile.close()

    # return the list
    return list_of_dicts
    #run teamInfo.py at localhost:5000
teamInfo_list = convert_to_dict("teamInfo.csv")

pairs_list = []
for t in teamInfo_list:
    pairs_list.append( (t['team-number'], t['team-name']) )


@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, team = {}, the_title="National Hockey League Teams Index")


@app.route('/team/<num>')
def detail(num):
    try:
        teams_dict = teamInfo_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for team: {num}</h1>"
    # a little bonus function, imported on line 2 above
    return render_template('team.html', team=teams_dict, the_title=teams_dict['team-name'])

if __name__ == '__main__':
    app.run(debug=True)
