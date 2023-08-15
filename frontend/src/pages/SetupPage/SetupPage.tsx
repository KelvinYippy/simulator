import { Stage, Team } from "../LandingPage/LandingPage"
import './SetupPage.scss'

interface MatchPageProps {
    home: Team | null
    away: Team | null
    teams: Record<string, Team>
    handlePropChange: (property: "home" | "away" | "selectedState", value: Team | Stage | null) => void
}

export const SetupPage = ({home, away, teams, handlePropChange}: MatchPageProps) => {

    const handleClassName = (name: string) => {
        let className = "team-card"
        if (home && name === home.name) {
            className = `home-${className}`
        } else if (away && name === away.name) {
            className = `away-${className}`
        }
        return className
    }
    
    const handleChange = (e: React.MouseEvent<HTMLDivElement, MouseEvent>) => {
        const chosenTeam = e.currentTarget.textContent as string
        if (!home && (!away || away.name !== chosenTeam)) {
            handlePropChange("home", teams[chosenTeam])
        } else if (home && home.name === chosenTeam) {
            handlePropChange("home", null)
        } else if (!away) {
            handlePropChange("away", teams[chosenTeam])
        } else if (away && away.name === chosenTeam) {
            handlePropChange("away", null)
        }
    }

    const simulateMatch = () => handlePropChange("selectedState", Stage.Match)

    return (
        <div> 
            <div style={{ height: '5vh', fontWeight: 'bold', margin: '1rem' }}>
                Soccer Simulator
            </div>
            <div className='team-grid' style={{ height: '70vh', overflow: 'scroll' }}>
                {
                    Object.keys(teams).map((team, index) => (
                        <div key={index} className={handleClassName(teams[team].name)} onClick={handleChange}>
                            <img src={teams[team].logo} alt={teams[team].name} className="team-image"/>
                            <b>{teams[team].name}</b>
                        </div>
                    ))
                }
            </div>
            <div style={{ height: '25vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                {
                    home && away &&
                    <div className='start-card'>
                        <b className='start-text'>{home.name} Versus {away.name}</b>
                        <button className='start-button' onClick={simulateMatch}>Simulate</button>
                    </div>
                }
            </div>
        </div>
    )

}