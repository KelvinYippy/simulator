import { fireEvent, render, screen } from "@testing-library/react";
import { LandingPage } from "../LandingPage/LandingPage";

const checkIfPresent = (notDefault = false) => {
    const startElement = screen.queryByText("Simulate")
    if (notDefault) {
        expect(startElement).toBeInTheDocument()
    } else {
        expect(startElement).not.toBeInTheDocument()
    }
}

test("no clicking of teams should not render load button", () => {
    render(<LandingPage/>)
    checkIfPresent()
})

test("just home team should not render load button", () => {
    render(<LandingPage/>)
    const arsenalCard = screen.queryByText("Arsenal")
    // eslint-disable-next-line testing-library/no-node-access
    fireEvent.click(arsenalCard?.parentElement as Element)
    checkIfPresent()
})

test("just away team should not render load button", () => {
    render(<LandingPage/>)
    const arsenalCard = screen.queryByText("Arsenal")
    const chelseaCard = screen.queryByText("Chelsea")
    // eslint-disable-next-line testing-library/no-node-access
    fireEvent.click(arsenalCard?.parentElement as Element)
    // eslint-disable-next-line testing-library/no-node-access
    fireEvent.click(chelseaCard?.parentElement as Element)
    // eslint-disable-next-line testing-library/no-node-access
    fireEvent.click(arsenalCard?.parentElement as Element)
    checkIfPresent()
})

test("load should render when both teams selected", () => {
    render(<LandingPage/>)
    const arsenalCard = screen.queryByText("Arsenal")
    const chelseaCard = screen.queryByText("Chelsea")
    // eslint-disable-next-line testing-library/no-node-access
    fireEvent.click(arsenalCard?.parentElement as Element)
    // eslint-disable-next-line testing-library/no-node-access
    fireEvent.click(chelseaCard?.parentElement as Element)
    checkIfPresent(true)
})