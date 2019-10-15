//qui utilizzereo fetch per permetterci di effettuare delle chiamate verso la nostra REST Api

import { CSRF_TOKEN } from "./csrf_token.js"

async function getJSON(response) {     //funzione per restituire il JSON del response
    if (response.status === 204) return '';
    return response.json();
}

function apiService(endpoint, method, data) {
    const config = {
      method: method || "GET",
      body: data !== undefined ? JSON.stringify(data) : null,
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN
      }
    }
    return fetch(endpoint, config)
            .then(getJSON)
            .catch(error => console.log(error))
}

export { apiService };
