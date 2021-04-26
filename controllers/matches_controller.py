import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint

matches_blueprint = Blueprint("matches", __name__)

import repositories.league_repository as league_repository
import repositories.matches_repository as matches_repository
import repositories.team_repository as team_repository

from models.match import match

@matches_blueprint.route("/matches")
def matches():
    matches = matches_repository.select_all()
    teams = team_repository.select_all()

    return render_template("matches/index.html", matches=matches, teams = teams)

@matches_blueprint.route("/matches/show", methods=["GET"])
def show_matches():
    matches = match_repository.select_all()
    teams = team_repository.select_all()

    return render_template("matches/show.html", matches=matches, teams = teams)

@matches_blueprint.route("/matches/new", methods=["GET"])
def new_match():
    teams = team_repository.select_all()
    return render_template("matches/new.html", teams = teams)

@matches_blueprint.route("/matches", methods=['POST'])
def create_match():
    home_team_id = request.form['home_team_id']
    away_team_id = request.form['away_team_id']
    match_date = request.form['match_date']
    match_result = request.form['match_result']

    league_id = 1

    match = Match(home_team_id, away_team_id, match_date, match_result, league_id)
    match_repository.save(match)
    return redirect('/matches')


@matches_blueprint.route("/matches/<id>/delete", methods=['POST'])
def delete_match(id):
    match_repository.delete(id)
    return redirect('/matches')

@matches_blueprint.route("/matches/<id>/team_matches", methods=["GET"])
def show_team_matches(id):
    matches = match_repository.select_all()
    teams = team_repository.select_all()

    return render_template("matches/team_matches.html", matches=matches, teams=teams, team_name = id)
    
@matches_blueprint.route("/matches/<id>/edit", methods=['GET'])
def edit_match(id):
    match = match_repository.select(id)

    home_team = team_repository.select(match.home_team_id)
    away_team = team_repository.select(match.away_team_id)

    teams = team_repository.select_all()
    return render_template('matches/edit.html', match = match, home_team = home_team, away_team = away_team, teams = teams)
    
@matches_blueprint.route("/matches/<id>", methods=['POST'])
def update_match(id):
    home_team_id = request.form['home_team_id']
    away_team_id = request.form['away_team_id']
    match_date = request.form['match_date']
    match_result = request.form['match_result']

    league_id = 1
    match = match(home_team_id, away_team_id, match_date, match_result, league_id, id)
    match_repository.update(match)
    return redirect('/matches')
