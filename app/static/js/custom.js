document.onload = onload();

function chooseUser() {

	$("#find_link").attr("class", "find-wait");
	$("#find_link").html("Подождите...");
	$("#find_image").removeAttr("src");

	$.get( "/choose", function( data ) {
		data = data.split("'").join("\"");
		data = $.parseJSON(data);
		
		console.log(data);

		$("#find_text").attr("class", "found-text");
		$("#find_text").html("<table height='180'><tr><td><div class='found-names'>" +
			"<a href='http://vk.com/id" + data.uid + "' target='_blank'>" + data.last_name + " " + data.first_name + "</a></div>" +
			"<small>uid: " + data.uid + "</small></td></tr>" +
			"<tr><td class='found_action'><a class='found_write' target='_blank' href='http://vk.com/im?sel=" + data.uid + "'>Начать диалог</a></td></tr></table>");
		$("#find_image").attr("src", data.photo_200 + "?timestamp=" + new Date().getTime());
	});
}

function onload() {
	$("#find_link").click(function (event) { chooseUser(); });	
}