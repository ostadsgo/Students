import requests


Games = [dict[str, str | dict[str, dict[str, str | int]]]]


def get_data_list(url: str, key: str) -> list[str]:
    """
    Send request to url and extract the key from retrived data and return it.
    :param url: url of the request.
    :param key: key of the dict
    :return: return a dict contain values.
    """
    request = requests.get(url)
    data = request.json()
    value = data.get(key)
    return value


def get_data_dict(url: str, key: str) -> Games:
    """
    Send request to url and extract the key from retrived data and return it.
    :param url: url of the request.
    :param key: key of the dict
    :return: return a dict contain values.
    """
    request = requests.get(url)
    data = request.json()
    value = data.get(key)
    return value


def list_years() -> list[str]:
    """
    Returns list of played years.
    return: list of years
    """
    return get_data_list(
        "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api", "seasons"
    )


def list_teams(year: str) -> list[str]:
    """
    Returns list of aviable teams
    :param year: Year of the game
    return: list of teams' name
    """
    return get_data_list(
        f"http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api/{year}",
        "teams",
    )


def list_gamedays(year: str) -> list[str]:
    """
    Returns list of the days a game played.
    :param year: the year of the game
    return: list of gamedays.
    """
    return get_data_list(
        f"http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api/{year}",
        "gamedays",
    )


def list_games(year, day: str) -> Games:
    """
    Returns list of aviable game days.
    :param year: the year of the game days
    :param month: the month of the game days
    return: list of played games.
    """
    return get_data_dict(
        f"http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api/{year}/{day}",
        "games",
    )


def get_game_result(game, team_result):
    """Decide is the game result winner, loser or draw"""
    home = game["score"]["home"]
    away = game["score"]["away"]
    home_team_name = home["team"]
    away_team_name = away["team"]

    # If the home team win the game.
    if home["goals"] > away["goals"]:
        team_result[home_team_name]["wins"] += 1
        team_result[home_team_name]["points"] += 3
        team_result[away_team_name]["lose"] += 1
    # if away team win the game
    elif home["goals"] < away["goals"]:
        team_result[away_team_name]["wins"] += 1
        team_result[away_team_name]["points"] += 3
        team_result[home_team_name]["lose"] += 1
    # if the game were ended draw
    else:
        team_result[home_team_name]["draw"] += 1
        team_result[away_team_name]["draw"] += 1
        team_result[home_team_name]["points"] += 1
        team_result[away_team_name]["points"] += 1


def calculate_scoreboard(year: str) -> dict[str, dict[str, int]]:
    """Calculate scoreboard of a season (year).
    :param year: The year game played
    :returns : return a dict contains scores of a each team.
    """
    team_result = {}
    for team in list_teams(year):
        team_result[team] = {"wins": 0, "lose": 0, "draw": 0, "points": 0}
    for day in list_gamedays(year):
        for game in list_games(year, day):
            get_game_result(game, team_result)

    return team_result


def get_scoreboard(year: str) -> list[tuple[str, dict[str, int]]]:
    """Return socre table sorted by ascending order.
    :param year: the year of the game played.
    :return : A python dict contains teams information sorted by team points.
    """
    teams = calculate_scoreboard(year)
    return sorted(teams.items(), key=lambda item: item[1]["points"], reverse=True)
