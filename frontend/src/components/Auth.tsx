import React, {useState} from 'react';
import UserForm from './UserForm';
import {observer} from "mobx-react-lite";


const Auth = observer(() => {


    const [view, setView] = useState(true);



        return (
            <>

                <section className="d-flex align-items-center position-relative">
                    <div className="container">
                        <div className="row">
                            <div className="col-12">
                                <div className="form-signin p-4">
                                    {view ?
                                        <UserForm class="authForm" type="signIn" buttonValue={'Log In'} handlerFunction={() => setView( false)}/> :
                                        <UserForm class="authForm" type="signUp" buttonValue={'Log Up'} handlerFunction={() => setView(true)}/>}
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </>
        )
});

export default Auth;