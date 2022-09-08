import _axios from '../settings/axios';








export const signIn = async (data: object) => await _axios.post('/auth/login/', data);

export const signUp = async (data: object) => await _axios.post('/auth/registration/', data);


export const getPlayers = async (data: object) => await _axios.get('/players/players/', data);
export const getPlayer = async (id: number) => await _axios.get(`/players/players/${id}/`);
export const createPlayer = async (data: object) => await _axios.post('/players/players/', data);
export const editPlayer = async (id: number, data: object) => await _axios.put(`/players/players/${id}/`, data);
export const deletePlayer = async (id: number) => await _axios.delete(`/players/players/${id}/`);

export const getGames = async (data: object) => await _axios.get('/players/games/', data);
export const getGame = async (id: number) => await _axios.get(`/players/games/${id}/`);
export const createGame = async (data: object) => await _axios.post('/players/games/', data);
export const editGame = async (id: number, data: object) => await _axios.put(`/players/games/${id}/`, data);
export const deleteGame = async (id: number) => await _axios.delete(`/players/games/${id}/`);


export function setHeaderAuthorization(token: string) {
    _axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
}

export function removeHeaderAuthorization() {
    delete _axios.defaults.headers.common["Authorization"];
}

