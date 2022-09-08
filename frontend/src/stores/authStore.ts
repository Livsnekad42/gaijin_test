import {
    signUp,
    signIn,
    setHeaderAuthorization,
    removeHeaderAuthorization,
} from '../requests/axiosRequests';
import {runInAction, makeAutoObservable} from 'mobx';
import {isLogged, setToastError} from "../settings/utils";



class AuthStore {

    constructor() {
        this.logIn = this.logIn.bind(this);
        this.logUp = this.logUp.bind(this);
        this.getTimeLogOut = this.getTimeLogOut.bind(this);
        makeAutoObservable(this);
        this.data.isLoggedIn = isLogged();
        this.logOut = this.logOut.bind(this);
    }

    data = {
        isLoggedIn: false,
        username: "",
        creds : {
            "email": "",
            "username": "",
            "password": ""
        },
        logOutTime : 600,
        token : ""
    }

    setLoginStatus(val: boolean) {
        let value = val.toString();
        localStorage.setItem('isAuthorized', value);
    }

    getLoginStatus() {
        return localStorage.getItem('isAuthorized');
    }

    setToken(val: string) {
        runInAction(() => {
            this.data.token = val;
        })
    }


    getTimeLogOut(tokenData: any) {
        let data = JSON.parse(tokenData)
        console.log('par', data)
        let diff = data.exp - data.iat;
        runInAction(() => {
            this.data.logOutTime = diff
        })
    }


    async logIn(cred: any) {
        try {
            const resp = await signIn(cred);
            const token = resp.data.token;
            let data = window.atob(token.split('.')[1])
            this.getTimeLogOut(data);
            setHeaderAuthorization(token);
            localStorage.setItem('isAuthorized', 'true');
            runInAction(() => {
                this.setLoginStatus(true)
            })
        } catch (error) {
            setToastError(error)
        }
    }

    async logUp(cred: any) {
        try {
           const resp = await signIn(cred);
            const token = resp.data.token;
            let data = window.atob(token.split('.')[1])
            this.getTimeLogOut(data);
            setHeaderAuthorization(token);
            localStorage.setItem('isAuthorized', 'true');
            runInAction(() => {
                this.setLoginStatus(true)
                this.data.creds.username = resp.data.username
                this.data.creds.email = resp.data.email
            })
        }
        catch (error) {
            setToastError(error)
        }
    }

   async logOut() {
        await localStorage.setItem('isAuthorized', 'false');
        runInAction(() => {
            this.setLoginStatus(false);
        })
        removeHeaderAuthorization();
        await localStorage.removeItem('jsw');
        window.location.href = "/";

    }
}


export default new AuthStore();
