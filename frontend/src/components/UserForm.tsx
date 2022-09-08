import React, {useState} from 'react';
import Input from './formElements/Input';
import authStore from '../stores/authStore';
import { Link } from 'react-router-dom';
import {observer} from "mobx-react-lite";
import {runInAction} from "mobx";
import {IFormInterface} from "../interfaces/IForm";
import Button from "./formELements/Button";

const UserForm = observer( (props: IFormInterface) => {

    const [data, setData] = useState({
        'email': '',
        'username': '',
        'password': '',
    });


    const handleEmail = (event: React.ChangeEvent<HTMLInputElement>) => {
        runInAction(()=> {
            authStore.data.creds.email = event.target.value;
        })
        return setData({'email': event.target.value, 'password': data.password, username: data.username});
    }

    const handleUsername = (event: React.ChangeEvent<HTMLInputElement>) => {
        runInAction(()=> {
            authStore.data.username = event.target.value;
        })
        setData({'email': data.email, 'password': data.password, "username": event.target.value });
    }

    const handlePass = (event: React.ChangeEvent<HTMLInputElement>) => {
        runInAction(()=> {
            authStore.data.creds.password = event.target.value;
        })
        setData({'email': data.email, 'password': event.target.value, username: data.username});
    }



    return (
        <>
            <div id="auth-form">

                <div className="mb-2">
                    <Input type="email" placeholder="Enter your e-mail" change={handleEmail} class="form-control" id="floatingEmail" />

                </div>

                {props.type === 'signUp' && <div className="mb-3">
                    <Input type="text" placeholder="Enter your nickname" change={handleUsername} class="form-control" id="floatingPassword"/>
                </div>}

                <div className="mb-3">
                    <Input type="password" placeholder="Enter your пароль" change={handlePass} class="form-control" id="floatingPassword"/>
                </div>


                <Button
                    click={props.type === 'signIn' ? authStore.logIn.bind(this, {
                        "email": data.email,
                        "password": data.password
                    }) : authStore.logUp.bind(this, data)}
                    value={props.buttonValue} class="btn btn-primary w-100 mb-4 red-btn red-btn-auth"/>


                <div className="col-12 text-center mt-3">
                    <p>
                        <p className="text-muted me-2" style={{fontSize:20}}>{props.type === 'signIn' ? 'Want to create new account?' : 'Already registered?'} </p>
                        <p style={{cursor: 'pointer', fontSize:20}} className="text-dark fw-medium" onClick={() => props.handlerFunction()}>{props.buttonValue === "Log Up" ? 'Log Up' : 'Log In'}</p>
                    </p>
                </div>
            </div>
        </>
    )
});

export default UserForm;