INSERT INTO leagues (league_name, league_size) VALUES ('Scottish Premiership', 12);
INSERT INTO teams (team_name, league_id) VALUES ('Rangers', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Celtic', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Aberdeen', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Hibernian', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Livingston', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Dundee United', 1);
INSERT INTO teams (team_name, league_id) VALUES ('St Mirren', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Kilmarnock', 1);
INSERT INTO teams (team_name, league_id) VALUES ('St Johnstone', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Motherwell', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Ross County', 1);
INSERT INTO teams (team_name, league_id) VALUES ('Hamilton Academical', 1);

INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (1, 2, '01-01-2021', '2-0', 1);
INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (1, 3, '08-01-2021', '3-0', 1);
INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (4, 1, '15-01-2021', '1-2', 1);
INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (1, 5, '22-01-2021', '5-2', 1);

INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (2, 4, '01-01-2021', '2-1', 1);
INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (5, 2, '08-01-2021', '1-1', 1);
INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (2, 12, '15-01-2021', '2-1', 1);


INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (3, 4, '01-01-2021', '1-1', 1);
INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (3, 11, '08-01-2021', '1-1', 1);
INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (8, 3, '15-01-2021', '1-1', 1);


INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (5, 6, '20-01-2021', '2-3', 1);
INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (7, 8, '20-01-2021', '1-0', 1);
INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (9, 10, '20-01-2021', '1-1', 1);
INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (3, 12, '20-01-2021', '3-2', 1);
INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (4, 11, '20-01-2021', '3-2', 1);


INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (5, 7, '20-01-2021', '2-0', 1);
INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (6, 8, '20-01-2021', '1-1', 1);
INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (9, 11, '20-01-2021', '1-1', 1);
INSERT INTO matches (home_team_id, away_team_id, match_date, match_result, league_id) VALUES (10, 12, '20-01-2021', '3-3', 1);