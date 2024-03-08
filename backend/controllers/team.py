from bs4 import BeautifulSoup
from utils import fetch

def fetch_teams_util(url: str):
    fetch_html = fetch(url)
    soup = BeautifulSoup(fetch_html, "html.parser")
    team_table = soup.find("table").find("tbody")
    teams = team_table.find_all("tr")
    print(teams)
    teams = list([
        {
            "name": team.find("td", class_="s20").find("a").text,
            "link": team.find("td", class_="s20").find("a")["href"],
            "logo": team.find("td", class_="a1").find("img")["data-src"].replace("60.png", "120.png")
        } for team in teams
    ])
    return teams

def fetch_trending_teams():
    return fetch_teams_util("https://sofifa.com/teams")

def fetch_national_teams():
    return fetch_teams_util("https://sofifa.com/teams?type=national")

def fetch_club_teams():
    return fetch_teams_util("https://sofifa.com/teams?type=club")
