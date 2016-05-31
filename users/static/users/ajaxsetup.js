/**
 * need this everytime you do post ajax
 */

function getCookie(name){
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        // if cookie is an attribute of document
        // and if the document.cookie is not a empty string
        // (it can be a number, dict, string etc)
        var cookies = document.cookie.split(';');
        // outputs a list of strings
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?

            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
     beforeSend: function(xhr, settings) {
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
});