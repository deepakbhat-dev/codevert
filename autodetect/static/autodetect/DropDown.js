$(document).ready(function() {
	$('#dbutton').on('click', function() {
		document.getElementById("sel_choice").disabled=false;
		document.getElementById("cbutton").disabled=false;
	});
	$('#change_convert').on('click', function() {
		$("#cbutton").attr("disabled", false);
		$("#sel_choice").attr("disabled", false);
		$('#answer').empty();
		$('#change_convert').hide();
	})
});
