import { render, screen } from "@testing-library/react";
import { LandingPage } from "./LandingPage";

test('renders initial setup page', () => {
    render(<LandingPage />);
    const titleElement = screen.getByText("Soccer Simulator");
    expect(titleElement).toBeInTheDocument();
});