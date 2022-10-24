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

const fireEventHelper = (cards: (HTMLElement | null)[]) => {
    cards.forEach((card) => {
        // eslint-disable-next-line testing-library/no-node-access
        fireEvent.click(card?.parentElement as Element)
    })
}

test("no clicking of teams should not render load button", () => {
    render(<LandingPage/>)
    checkPresence()
})

test("just home team should not render load button", () => {
    render(<LandingPage/>)
    const arsenalCard = screen.queryByText("Arsenal")
    // eslint-disable-next-line testing-library/no-node-access
    fireEvent.click(arsenalCard?.parentElement as Element)
    checkPresence()
})

test("just away team should not render load button", () => {
    render(<LandingPage/>)
    const arsenalCard = screen.queryByText("Arsenal")
    const chelseaCard = screen.queryByText("Chelsea")
    fireEventHelper([arsenalCard, chelseaCard, arsenalCard])
    checkPresence()
})

test("load should render when both teams selected", () => {
    render(<LandingPage/>)
    const arsenalCard = screen.queryByText("Arsenal")
    const chelseaCard = screen.queryByText("Chelsea")
    fireEventHelper([arsenalCard, chelseaCard])
    checkPresence(true)
})