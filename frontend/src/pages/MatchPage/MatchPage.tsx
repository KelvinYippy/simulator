import { Fragment } from "react"
import { SimulatorEvent, SimulatorScore, SimulatorStatus, Team } from "../LandingPage/LandingPage"
import './MatchPage.scss'
import { BackArrow } from "../../components/BackArrow/BackArrow"

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
                <Fragment>
                    <BackArrow callback={resetMatch}/>
                    <h3>Match Result</h3>
                    <div className="scoreboard">
                        <img src={home.logo} alt={home.name} style={{ marginRight: '1rem' }}/>
                        <strong>{goals[0]} - {goals[1]}</strong>
                        <img src={away.logo} alt={away.name} style={{ marginLeft: '1rem' }}/>
                    </div>
                    <div style={{ marginTop: '1rem' }}>
                        {
                            events.map((event, i) => (
                                <div key={i}>
                                    {
                                        <p><b>{event._minute}</b>: {event._commentary}</p>
                                    }
                                </div>
                            ))
                        }
                    </div>
                </Fragment>
            }
        </div>
    )
}