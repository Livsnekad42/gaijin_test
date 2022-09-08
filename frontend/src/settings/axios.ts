import axios from 'axios';

export const baseURL = 'http://127.0.0.1:8000';

const _axios = axios.create({
    baseURL
});

export default _axios;