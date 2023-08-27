import { fireEvent, render, screen } from "@testing-library/react";
import { LandingPage } from "../LandingPage/LandingPage";

const checkPresence = (notDefault = false) => {
    const startElement = screen.queryByText("Simulate")
    if (notDefault) {
        expect(startElement).toBeInTheDocument()
    } else {
        expect(startElement).not.toBeInTheDocument()
    }
}

test("no clicking of teams should not render load button", () => {
    render(<LandingPage/>)
    checkPresence()
})

test("initial load should load a greyed-out trending button", () => {
    render(<LandingPage/>)
    expect(screen.getByTestId('trending-button')).toHaveStyle('background-color: #dde4ec')
    expect(screen.getByTestId('club-button')).toHaveStyle('background-color: inherit')
    expect(screen.getByTestId('national-button')).toHaveStyle('background-color: inherit')
})

test("clicking on club button should load a greyed-out club button", () => {
    render(<LandingPage/>)
    const clubButton = screen.getByTestId('club-button')
    fireEvent.click(clubButton)
    expect(screen.getByTestId('trending-button')).toHaveStyle('background-color: inherit')
    expect(screen.getByTestId('club-button')).toHaveStyle('background-color: #dde4ec')
    expect(screen.getByTestId('national-button')).toHaveStyle('background-color: inherit')
})

test("clicking on national button should load a greyed-out nation button", () => {
    render(<LandingPage/>)
    const nationButton = screen.getByTestId('national-button')
    fireEvent.click(nationButton)
    expect(screen.getByTestId('trending-button')).toHaveStyle('background-color: inherit')
    expect(screen.getByTestId('club-button')).toHaveStyle('background-color: inherit')
    expect(nationButton).toHaveStyle('background-color: #dde4ec')
})
