

export interface IPlayer {
    id : number,
    username : string,
    score: number,
    avatar?: string,
    avatar_upload?: File
    game : number
    is_banned : boolean
}

export interface IGame {
    id : number
    name : string
    players_count : number
}