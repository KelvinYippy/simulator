import { render, screen } from "@testing-library/react";
import { MatchPage } from "./MatchPage";

test('renders waiting message', () => {
    render(<MatchPage goals={[0, 0]} events={[]} home="Chelsea" away="Arsenal" loading/>);
    const loadingElement = screen.getByText("Waiting for Simulator to Load Results");
    expect(loadingElement).toBeInTheDocument()
})

test('show result', () => {
    render(<MatchPage goals={[0, 0]} events={[]} home="Chelsea" away="Arsenal" loading={false}/>);
    const resultElement = screen.getByText("Match Result");
    expect(resultElement).toBeInTheDocument()
})