import { TEAMS } from "../../data"
import { Stage } from "../LandingPage/LandingPage"
import './SetupPage.scss'

interface MatchPageProps {
    home: string
    away: string
    handlePropChange: (value: string | Stage, property: "home" | "away" | "selectedState") => void
}

export const SetupPage = ({home, away, handlePropChange}: MatchPageProps) => {

    const handleClassName = (name: string) => {
        let className = "team-card"
        if (name === home) {
            className = `home-${className}`
        } else if (name === away) {
            className = `away-${className}`
        }
        return className
    }
    
    const handleChange = (e: React.MouseEvent<HTMLDivElement, MouseEvent>) => {
        if (home === "" && away !== e.currentTarget.textContent) {
            handlePropChange(e.currentTarget.textContent as string, "home")
        } else if (home === e.currentTarget.textContent) {
            handlePropChange("", "home")
        } else if (away === "") {
            handlePropChange(e.currentTarget.textContent as string, "away")
        } else if (away === e.currentTarget.textContent) {
            handlePropChange("", "away")
        }
    }

    return (
        <div> 
            <h3>Soccer Simulator</h3>
            <div className='team-grid'>
                {
                    Object.keys(TEAMS).map((team, index) => (
                        <div key={index} className={handleClassName(team)} onClick={handleChange}>
                            <img src={TEAMS[team]} alt={team} className="team-image"/>
                            <b>{team}</b>
                        </div>
                    ))
                }
            </div>
            {
                home !== "" && away !== "" &&
                <div className='start-card'>
                    <b className='start-text'>{home} Versus {away}</b>
                    <button className='start-button' onClick={() => handlePropChange(Stage.Match, "selectedState")}>Simulate</button>
                </div>
            }
        </div>
    )

}