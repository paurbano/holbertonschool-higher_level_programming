// Jquery
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.getJSON(url, function (response) {
  $('DIV#hello').text(response.hello);
});
