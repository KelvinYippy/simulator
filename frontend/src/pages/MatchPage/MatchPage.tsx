import { Fragment } from "react"
import { SimulatorEvent, SimulatorScore } from "../LandingPage/LandingPage"
import { TEAMS } from '../../data'
import back_arrow from "../../assets/arrow-left.svg"
import './MatchPage.css'

interface MatchPageProps {
    goals: SimulatorScore,
    events: SimulatorEvent[],
    home: string,
    away: string,
    loading: boolean,
    resetMatch?: () => void
}

export const MatchPage = ({goals, events, home, away, loading, resetMatch}: MatchPageProps) => {

    return (
        <div>
            {
                loading ? 
                <h1>Waiting for Simulator to Load Results</h1> :
                <Fragment>
                    <img src={back_arrow} alt="Back Arrow" className="back-arrow" onClick={resetMatch}/>
                    <h3>Match Result</h3>
                    <div className="scoreboard">
                        <img src={TEAMS[home]} alt={home} style={{ marginRight: '1rem' }}/>
                        <strong>{goals[0]} - {goals[1]}</strong>
                        <img src={TEAMS[away]} alt={away} style={{ marginLeft: '1rem' }}/>
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