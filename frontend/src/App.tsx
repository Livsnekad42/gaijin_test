import React from 'react';
import Auth from "./views/Auth";
import {isLogged} from "./settings/utils";

const App = () => {
    return (
        <>
            {!isLogged ? <Auth/> : <h3></h3>}
        </>
    );
};

export default App;
