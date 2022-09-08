import {makeAutoObservable} from "mobx";
import {IPlayer, IGame} from '../interfaces/IPlayer';

interface IPlayerData {
    players : Array<IPlayer>,
    games:  Array<IGame>
}


class PlayerStore {

    constructor() {
        makeAutoObservable(this);
    }

    data: IPlayerData = {
        players : [{
            id : 0,
            username : "",
            score: 0,
            avatar: "",
            avatar_upload: null,
            game: 0,
            is_banned : false
        }],
        games : [{
                id : 0,
                name : "",
                players_count : 0
            }]
    }
}