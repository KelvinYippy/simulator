import { useState } from "react"

export const useMultiState = <T, >(object: T) => {

    const [componentState, setObject] = useState(object)

    type K = keyof T

    const handleIndividualChange = (property: K, value: T[K]) => {
        setObject({
            ...componentState,
            [property]: value
        })
    }

    const handleMultipleChange = (modifiedComponentState: Partial<T>) => {
        setObject({
            ...componentState,
            ...modifiedComponentState
        })
    }

    return {
        componentState,
        handleIndividualChange,
        handleMultipleChange
    }

}