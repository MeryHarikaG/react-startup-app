export default class APIService {
    static LoginUser(body) {

        return fetch('http://startupclub.onrender.com/auth/', {
            'method': 'POST',
            headers: {
                'Content-Type': 'application/json',

            },
            body: JSON.stringify(body)

        }).then(resp => resp.json())

    }


    static RegisterUser(body) {

        return fetch('http://startupclub.onrender.com/Frontend/users/', {
            'method': 'POST',
            headers: {
                'Content-Type': 'application/json',

            },
            body: JSON.stringify(body)

        }).then(resp => resp.json())

    }

}