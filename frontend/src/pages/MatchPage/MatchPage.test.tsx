import { render, screen } from "@testing-library/react";
import { SimulatorStatus } from "../LandingPage/LandingPage";
import { MatchPage } from "./MatchPage";

test('renders waiting message', () => {
    render(<MatchPage goals={[0, 0]} events={[]} home="Chelsea" away="Arsenal" loading={SimulatorStatus.Simulating}/>);
    const loadingElement = screen.getByText("Waiting for Simulator to Load Results");
    expect(loadingElement).toBeInTheDocument()
})

test('show result', () => {
    render(<MatchPage goals={[0, 0]} events={[]} home="Chelsea" away="Arsenal" loading={SimulatorStatus.Finished}/>);
    const resultElement = screen.getByText("Match Result");
    expect(resultElement).toBeInTheDocument()
})