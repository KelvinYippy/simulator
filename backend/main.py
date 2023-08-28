from fastapi import FastAPI
from simulator import NewSimulator
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from controllers.team import fetch_trending_teams, fetch_club_teams, fetch_national_teams

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SimulatorTeamRequest(BaseModel):
    name: str
    link: str

@app.get("/")
async def root():
    return {
        "message": "Welcome to the simulator!"
    }

@app.post("/match")
async def simulate_sofifa_match(home_team: SimulatorTeamRequest, away_team: SimulatorTeamRequest):
    match = NewSimulator(home_team.name, away_team.name, home_team.link, away_team.link).run_simulator()
    return {
        "goals": [match.home_goals, match.away_goals],
        "events": match._events
    }

@app.get("/teams")
async def get_trending_teams():
    return fetch_trending_teams()

@app.get("/clubs")
async def get_clubs():
    return fetch_club_teams()

@app.get("/national_teams")
async def get_national_teams():
    return fetch_national_teams()