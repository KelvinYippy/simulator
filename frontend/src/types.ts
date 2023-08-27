export enum Stage {
    Setup,
    Match
}

export enum SimulatorStatus {
    Simulating,
    Error,
    Finished
}

export enum TeamSearchType {
    Trending,
    Club,
    National
}

export type Player = {
    _name: string,
    _position: string,
    _rating: number,
    _age: number,
    _image: string | null
}

export type Team = {
    name: string,
    link: string,
    logo: string
}

export type SimulatorEvent = {
    _minute: number,
    _commentary: string,
    _scorer: Player | string,
    _assister: Player | string | null
    _is_home: boolean
}

export type SimulatorScore = [number, number]