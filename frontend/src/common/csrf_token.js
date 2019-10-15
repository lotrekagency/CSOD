// qui scriveremo il codice necessario a permetterci di estrarre questo token
// necessario per le richieste che non sono considerate sicure, quindi quelle richieste
// che comportano la scrittura nel database

// con questa funzione otteniamo questo CSRF_TOKEN che esporteremo e lo integreremo nel codice
// che utilizzeremo per comunicare con la REST Api

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var CSRF_TOKEN = getCookie('csrftoken');

export { CSRF_TOKEN };
