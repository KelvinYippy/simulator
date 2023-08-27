from bs4 import BeautifulSoup
from utils import fetch

def fetch_teams_util(url: str):
    fetch_html = fetch(url)
    soup = BeautifulSoup(fetch_html, "html.parser")
    team_table = soup.find("table").find("tbody")
    teams = team_table.find_all("tr")
    teams = list([
        {
            "name": team.find("td", class_="col-name-wide").find_all("div", class_="ellipsis")[0].text,
            "link": team.find("td", class_="col-name-wide").find_all("a")[0]["href"],
            "logo": team.find("td", class_="col-avatar").find("img")["data-src"].replace("60.png", "120.png")
        } for team in teams
    ])
    return teams

def fetch_trending_teams():
    return fetch_teams_util("https://sofifa.com/teams")

def fetch_national_teams():
    return fetch_teams_util("https://sofifa.com/teams?type=national")

def fetch_club_teams():
    return fetch_teams_util("https://sofifa.com/teams?type=club")
