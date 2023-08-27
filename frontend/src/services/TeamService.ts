import { Team } from "../types"

export class TeamService {

    private fetchTeamHelper = async (team_type: string) => {
        const teams: Team[] = await (await fetch(`http://localhost:8000/${team_type}`)).json()
        return teams
    }

    fetchTrendingTeams = async () => await this.fetchTeamHelper("teams")

    fetchClubTeams = async () => await this.fetchTeamHelper("clubs")

    fetchNationalTeams = async () => await this.fetchTeamHelper("national_teams")

}