import axios from 'axios';


export const logInRequest = async (un, pw, sa) => {
    return axios({
        method: 'post',
        url: sa + '/login',
        data: {
          user: un,
          password_plain: pw
        }
    });
}