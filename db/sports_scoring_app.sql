DROP TABLE matches;
DROP TABLE players;
DROP TABLE teams;
DROP TABLE leagues;


CREATE TABLE leagues (
  id SERIAL PRIMARY KEY,
  league_name VARCHAR(255),
  league_size INT
);

CREATE TABLE teams (
  id SERIAL PRIMARY KEY,
  team_name VARCHAR(255),
  league_id INT REFERENCES leagues(id)
);


CREATE TABLE matches(
  id SERIAL PRIMARY KEY,
  home_team_id INT REFERENCES teams(id),
  away_team_id INT REFERENCES teams(id),
  match_date DATE,
  match_result VARCHAR(7),
  league_id INT REFERENCES leagues(id)
);