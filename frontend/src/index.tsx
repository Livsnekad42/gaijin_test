import React from 'react';
import ReactDOM from 'react-dom';
import {Router} from "react-router-dom";
import App from './App';
import history from "./settings/history";

ReactDOM.render(
    <>
        <Router history={history} key={Math.random()}>
     <App/>
        </Router>
    </>,
  document.getElementById('root')
);
