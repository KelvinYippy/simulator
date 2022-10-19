import { render, screen } from "@testing-library/react";
import { TEAMS } from "../../data";
import { LandingPage } from "./LandingPage";

test('renders initial setup page', () => {
    render(<LandingPage />);
    const titleElement = screen.getByText("Soccer Simulator");
    expect(titleElement).toBeInTheDocument();
});
  
test('renders team cards', () => {
    render(<LandingPage />)
    for (const team in TEAMS) {
      const teamCard = screen.getByText(team)
      expect(teamCard).toBeInTheDocument()
    }
})