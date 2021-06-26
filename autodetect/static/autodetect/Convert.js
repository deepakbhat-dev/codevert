function convertFunction(sel_format) {
	document.getElementById("sel_choice").disabled=true;
	$.ajax(
		 {
			 type:"GET",
			 url: "/autodetect/convert",
			 data: {
				 "to_format" : sel_format,
			 },
			 success: function(response) {
				 $("#answer").append(
					$("<h3></h3>").html(response));
			},
		});
	document.getElementById("cbutton").disabled=true;
	$("#change_convert").show();
}
