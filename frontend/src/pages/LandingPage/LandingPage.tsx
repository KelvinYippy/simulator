import { useEffect } from 'react'
import { MatchPage } from '../MatchPage/MatchPage'
import { SetupPage } from '../SetupPage/SetupPage'
import { useMultiState } from '../../hooks/useMultiState'
import { SimulatorEvent, SimulatorScore, SimulatorStatus, Stage, Team, TeamSearchType } from '../../types'
import { TeamService } from '../../services/TeamService'

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
        teams: {} as Record<string, Team>,
        teamSearchType: TeamSearchType.Trending,
        teamSearchLoading: false
    }

    const teamService = new TeamService()

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
        const fetchLookup: Record<TeamSearchType, () => Promise<Team[]>> = {
            [TeamSearchType.Trending]: teamService.fetchTrendingTeams,
            [TeamSearchType.Club]: teamService.fetchClubTeams,
            [TeamSearchType.National]: teamService.fetchNationalTeams
        }
        const result: Team[] = await fetchLookup[componentState.teamSearchType]()
        const teams: Record<string, Team> = {}
        result.forEach((team) => {
            teams[team.name] = team
        })
        handleMultipleChange({
            teams: teams,
            home: null,
            away: null
        })
    }

    useEffect(() => {
        if (componentState.selectedState === Stage.Match) {
            fetchMatch()
        } else if (componentState.selectedState === Stage.Setup) {
            handleIndividualChange("teamSearchLoading", true)
            fetchTeams()
            handleIndividualChange("teamSearchLoading", false)
        }
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [componentState.selectedState, componentState.teamSearchType])

    return (
        <div> 
            {
                componentState.selectedState === Stage.Setup && 
                <SetupPage 
                    home={componentState.home} 
                    away={componentState.away} 
                    teams={componentState.teams} 
                    handlePropChange={handleIndividualChange}
                    teamSearchType={componentState.teamSearchType}
                    teamSearchLoading={componentState.teamSearchLoading}
                />
            }
            {
                componentState.selectedState === Stage.Match && componentState.home && componentState.away &&
                <MatchPage goals={componentState.goals} events={componentState.events} loading={componentState.loading} home={componentState.home} away={componentState.away} resetMatch={resetState}/>
            }
        </div>
    )

}