import {toast} from "react-toastify";

export function isLogged() : boolean {
    return localStorage.getItem('isAuthorized') === 'true';
}

export function setToastError(toaster : string) {
    try {
        const error = () => toast.error(toaster, {
            hideProgressBar: true
        });
        error();
    } catch (e) {
        console.log(e)
    }
}

export function setToastInfo(toaster : string) {
    const info = () => toast.info(toaster,{
        hideProgressBar: true
    });
    info();
}

export function setToastWarn(toaster : string) {
    const warn = () => toast.warn(toaster,{
        hideProgressBar: true
    });
    warn();
}

export function setToastSuccess(toaster : string) {
    const success = () => toast.success(toaster,{
        hideProgressBar: true
    });
    success();
}
