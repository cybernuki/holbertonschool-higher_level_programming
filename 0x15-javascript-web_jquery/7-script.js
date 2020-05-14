const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'
const character = $.get(url , function(data, textStatus) {

	if (textStatus == 'success') {
		$('DIV#character').text(data.name);
	}
});
