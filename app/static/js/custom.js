document.onload = onload();

var photo;
function chooseUser() {

	$("#find_link").attr("class", "find-wait");
	$("#find_link").html("Подождите...");

	$.get( "/choose", function( data ) {
		data = data.split("'").join("\"");
		data = $.parseJSON(data);
		
		console.log(data);

		$("#found_name").html("<a href='http://vk.com/id" + data.uid + "' target='_blank'>" + data.last_name + " " + data.first_name + "</a>")
		$("#found_text").html("<a class='found_write' href='https://m.vk.com/mail?act=show&peer=" + data.uid + "'>Написать</a><br><small>uid: " + data.uid + "</small>");
		$("#try_again").html("<a onclick='chooseUser()'>Попробовать еще раз</a>");
		if (data.photo_max_orig  !== undefined) {
			$("#find_image").attr("src", data.photo_max_orig + "?timestamp=" + new Date().getTime());
		}

		$('.found_write').click(function (event) {
    		event.preventDefault();
    		window.open($(this).attr("href"), "writeWindow", "width=600,height=600,scrollbars=yes");
		});
	});
}

function onload() {
	$("#find_link").click(function (event) { chooseUser(); });	
}