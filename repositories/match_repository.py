from db.run_sql import run_sql
from models.league import League
from models.team import Team
from models.match import match

def select_all():
    matches = []

    sql = "SELECT * FROM matches"
    
    results = run_sql(sql)

    for row in results:
        match = match(row['home_team_id'], row['away_team_id'], row['match_date'], row['match_result'], row['league_id'], row['id'])
        matches.append(match)

    return matches

def save(match):
    sql = "INSERT INTO matches(home_team_id, away_team_id, match_date, match_result, league_id) VALUES ( %s, %s, %s, %s, %s ) RETURNING id"
    values = [match.home_team_id, match.away_team_id, match.match_date, match.match_result, match.league_id]
    results = run_sql( sql, values )
    match.id = results[0]['id']
    return match

def delete(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select(id):
    match = None
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        match = match(result['home_team_id'], result['away_team_id'], result['match_date'], result['match_result'], result['league_id'], result['id'] )
    return match

def update(match):
    sql = "UPDATE matches SET (home_team_id, away_team_id, match_date, match_result, league_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [match.home_team_id, match.away_team_id, match.match_date, match.match_result, match.league_id, match.id]
    run_sql(sql, values)