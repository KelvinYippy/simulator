import { useEffect, useState } from 'react'
import './LandingPage.css'
import { MatchPage } from '../MatchPage/MatchPage'
import { SetupPage } from '../SetupPage/SetupPage'

export enum Stage {
    Setup,
    Match
}

export enum SimulatorStatus {
    Simulating,
    Error,
    Finished
}

type Player = {
    _name: string,
    _position: string,
    _rating: number,
    _age: number
}

export type SimulatorEvent = {
    _minute: number,
    _commentary: string,
    _scorer: Player | string,
    _assister: Player | string | null
}

export type SimulatorScore = [number, number]

type SimulatorResult = {
    goals: SimulatorScore,
    events: SimulatorEvent[]
}

export const LandingPage = () => {

    const initialLandingPageState = {
        home: "",
        away: "",
        selectedState: Stage.Setup,
        goals: [0, 0] as [number, number],
        events: [] as SimulatorEvent[],
        loading: SimulatorStatus.Simulating,
    }

    type T = typeof initialLandingPageState
    type K = keyof T

    const [componentState, setComponentState] = useState(initialLandingPageState)

    const handleIndividualChange = (value: T[K], property: K) => {
        setComponentState({
            ...componentState,
            [property]: value
        })
    }

    const handleMultipleChange = (object: Partial<T>) => {
        setComponentState({
            ...componentState,
            ...object
        })
    }

    const resetState = () => handleMultipleChange(initialLandingPageState)

    useEffect(() => {
        const fetchMatch = async () => {
            if (componentState.selectedState === Stage.Match) {
                try {
                    const request: SimulatorResult = await (await fetch(`http://localhost:8000/match/${componentState.home}/${componentState.away}`)).json()
                    handleMultipleChange({
                        events: request.events,
                        goals: request.goals,
                        loading: SimulatorStatus.Finished
                    })
                } catch (e) {
                    console.log(e)
                    handleIndividualChange(SimulatorStatus.Error, "loading")
                }
            }
        }
        fetchMatch()
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [componentState.selectedState])

    return (
        <div className='landing-page'> 
            {
                componentState.selectedState === Stage.Setup && 
                <SetupPage home={componentState.home} away={componentState.away} handlePropChange={handleIndividualChange}/>
            }
            {
                componentState.selectedState === Stage.Match &&
                <MatchPage goals={componentState.goals} events={componentState.events} loading={componentState.loading} home={componentState.home} away={componentState.away} resetMatch={resetState}/>
            }
        </div>
    )

}