from fastapi import FastAPI
from simulator import SoFIFASimulator
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/")
async def root():
    return {
        "message": "Welcome to the simulator!"
    }

@app.get("/match/{home_team}/{away_team}")
async def simulate_sofifa_match(home_team: str, away_team: str):
    match = SoFIFASimulator(home_team.replace("%20", " "), away_team.replace("%20", " ")).run_simulator()
    return {
        "goals": [match.home_goals, match.away_goals],
        "events": match._events
    }