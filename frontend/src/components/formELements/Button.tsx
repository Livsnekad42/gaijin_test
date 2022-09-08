import React, { FunctionComponent } from 'react';
import {IButtonInterface} from "../../interfaces/IForm";



const Button = (props: IButtonInterface) => {
    return (
        <button type="submit" onClick={props.click} className={props.class} disabled={props.disabled}>{props.value}</button>
    )
};

export default Button;