import { useEffect } from 'react'
import { MatchPage } from '../MatchPage/MatchPage'
import { SetupPage } from '../SetupPage/SetupPage'
import { useMultiState } from '../../hooks/useMultiState'

export enum Stage {
    Setup,
    Match
}

export enum SimulatorStatus {
    Simulating,
    Error,
    Finished
}

export type Player = {
    _name: string,
    _position: string,
    _rating: number,
    _age: number,
    _image: string | null
}

export type Team = {
    name: string,
    link: string,
    logo: string
}

export type SimulatorEvent = {
    _minute: number,
    _commentary: string,
    _scorer: Player | string,
    _assister: Player | string | null
    _is_home: boolean
}

export type SimulatorScore = [number, number]

type SimulatorResult = {
    goals: SimulatorScore,
    events: SimulatorEvent[]
}

export const LandingPage = () => {

    const initialLandingPageState = {
        home: null as Team | null,
        away: null as Team | null,
        selectedState: Stage.Setup,
        goals: [0, 0] as SimulatorScore,
        events: [] as SimulatorEvent[],
        loading: SimulatorStatus.Simulating,
        teams: {} as Record<string, Team>
    }

    const { componentState, handleIndividualChange, handleMultipleChange } = useMultiState(initialLandingPageState)

    const resetState = () => handleMultipleChange(initialLandingPageState)

    const fetchMatch = async () => {
        try {
            const homeTeam = {
                name: componentState.home!.name,
                link: componentState.home!.link
            }
            const awayTeam = {
                name: componentState.away!.name,
                link: componentState.away!.link
            }
            const body = {
                home_team: homeTeam,
                away_team: awayTeam
            }
            const request: SimulatorResult = await (await fetch(
                "http://localhost:8000/match", {
                    method: 'POST',
                    headers: {
                        Accept: 'application.json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(body),
                    cache: 'default'
                }
            )).json()
            handleMultipleChange({
                events: request.events,
                goals: request.goals,
                loading: SimulatorStatus.Finished
            })
        } catch (_) {
            handleIndividualChange("loading", SimulatorStatus.Error)
        }
    }

    const fetchTeams = async () => {
        const result: Team[] = await ((await fetch(`http://localhost:8000/teams`)).json())
        const teams: Record<string, Team> = {}
        result.forEach((team) => {
            teams[team.name] = team
        })
        handleIndividualChange("teams", teams)
    }

    useEffect(() => {
        if (componentState.selectedState === Stage.Match) {
            fetchMatch()
        } else if (componentState.selectedState === Stage.Setup) {
            fetchTeams()
        }
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [componentState.selectedState])

    return (
        <div> 
            {
                componentState.selectedState === Stage.Setup && 
                <SetupPage home={componentState.home} away={componentState.away} teams={componentState.teams} handlePropChange={handleIndividualChange}/>
            }
            {
                componentState.selectedState === Stage.Match && componentState.home && componentState.away &&
                <MatchPage goals={componentState.goals} events={componentState.events} loading={componentState.loading} home={componentState.home} away={componentState.away} resetMatch={resetState}/>
            }
        </div>
    )

}