import { Fragment } from "react"
import { SimulatorEvent, SimulatorScore, SimulatorStatus, Team, Player } from "../../types"
import './MatchPage.scss'
import { BackArrow } from "../../components/BackArrow/BackArrow"
import defaultPlayer from '../../assets/player.png'

interface MatchPageProps {
    goals: SimulatorScore,
    events: SimulatorEvent[],
    home: Team,
    away: Team,
    loading: SimulatorStatus,
    resetMatch?: () => void
}

export const MatchPage = ({goals, events, home, away, loading, resetMatch}: MatchPageProps) => {

    return (
        <div>
            {
                loading === SimulatorStatus.Simulating ? 
                <Fragment>
                    <h1>Waiting for Simulator to Load Results</h1> 
                    <div className="loading-ring"></div>
                </Fragment> :
                loading === SimulatorStatus.Error ? 
                <div style={{ marginTop: '1rem', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                    <BackArrow callback={resetMatch}/>
                    <div className="alert">
                        An error was encountered while simulating. Please try again!
                    </div>
                </div> :
                <div style={{ marginTop: "1rem" }}>
                    <BackArrow callback={resetMatch}/>
                    <div style={{ fontSize: "4rem", fontWeight: "700" }}>Match Result</div>
                    <div className="scoreboard">
                        <img src={home.logo} alt={home.name} style={{ marginRight: '1rem' }}/>
                        <strong style={{ fontSize: "3rem" }}>{goals[0]} - {goals[1]}</strong>
                        <img src={away.logo} alt={away.name} style={{ marginLeft: '1rem' }}/>
                    </div>
                    <div style={{ marginTop: '1rem' }}>
                        {
                            events.map((event, i) => (
                                <div key={i} className={event._is_home ? "home-match-event" : "away-match-event"}>
                                    <div style={{ width: "20%" }}>
                                        <img src={(event._scorer as Player)._image ?? defaultPlayer} alt="Scorer" className={event._is_home ? "home-player-icon" : "away-player-icon"}/>
                                    </div>
                                    <div><b>{event._minute}</b>: {event._commentary}</div>
                                </div>
                            ))
                        }
                    </div>
                </div>
            }
        </div>
    )
}