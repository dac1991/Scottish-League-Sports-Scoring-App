import pdb, operator
from operator import itemgetter
from datetime import datetime
from flask import Flask, render_template
from flask import Blueprint

import repositories.league_repository as league_repository
import repositories.team_repository as team_repository
import repositories.stat_repository as stat_repository
import repositories.match_repository as match_repository

leagues_blueprint = Blueprint("leagues", __name__)

@leagues_blueprint.route("/leagues")
def leagues():
    teams = team_repository.select_all()
    matches = match_repository.select_all()
    stats = stat_repository.generate_stats(teams, matches)
    games_won = stat_repository.generate_games_won(teams, matches)
    games_drawn = stat_repository.generate_games_drawn(teams, matches)
    games_lost = stat_repository.generate_games_lost(teams, matches)
    goals_for = stat_repository.generate_goals_for(teams, matches)
    goals_against = stat_repository.generate_goals_against(teams, matches)
    games_form = stat_repository.generate_games_form(teams, matches)

    league_points = stat_repository.generate_league_points(teams, matches)
    today = datetime.now()
    today = today.strftime("%d/%m/%Y %H:%M:%S")

    return render_template("leagues/show.html", teams = teams, stats = stats, games_won = games_won, games_drawn = games_drawn, games_lost = games_lost, league_points = league_points, goals_for = goals_for, goals_against = goals_against, games_form = games_form, today = today)

