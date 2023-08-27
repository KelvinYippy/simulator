import { Stage, Team, TeamSearchType } from "../../types"
import './SetupPage.scss'

interface MatchPageProps {
    home: Team | null
    away: Team | null
    teams: Record<string, Team>
    handlePropChange: (property: "home" | "away" | "selectedState" | "teamSearchType", value: Team | Stage | TeamSearchType | null) => void,
    teamSearchType: TeamSearchType
    teamSearchLoading: boolean
}

export const SetupPage = ({home, away, teams, handlePropChange, teamSearchType, teamSearchLoading}: MatchPageProps) => {

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
            <div style={{ height: '5vh', fontWeight: 'bold', margin: '1rem', fontSize: "3rem" }}>
                Soccer Simulator
            </div>
            <div style={{ display: "flex", maxHeight: '10vh' }}>
                <div className="start-button" data-testid='trending-button' style={{ backgroundColor: teamSearchType === TeamSearchType.Trending ? "#dde4ec" : "inherit" }} onClick={() => handlePropChange("teamSearchType", TeamSearchType.Trending)}>
                    Trending
                </div>
                <div className="start-button" data-testid='club-button' style={{ backgroundColor: teamSearchType === TeamSearchType.Club ? "#dde4ec" : "inherit" }} onClick={() => handlePropChange("teamSearchType", TeamSearchType.Club)}>
                    Club   
                </div>
                <div className="start-button" data-testid='national-button' style={{ backgroundColor: teamSearchType === TeamSearchType.National ? "#dde4ec" : "inherit" }} onClick={() => handlePropChange("teamSearchType", TeamSearchType.National)}>
                    National
                </div>
            </div>
            <div className='team-grid' style={{ height: '60vh', overflow: 'scroll' }}>
                {
                    teamSearchLoading ? 
                    <div className="loading-ring"></div> :
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