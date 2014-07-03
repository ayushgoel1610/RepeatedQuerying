$(document).ready(function() {

	$("select").hide();
	$("#People").show();

	$.Studentselect = function() {
		 $("#Students").change(function() {
		 	var selvalue = $("#Students option:selected").text();
		 	if (selvalue == "B.Tech"){
		 		$(".year").hide();
		 		$("#BTech").show();
		 	}
		 	else if (selvalue == "M.Tech"){
		 		$(".year").hide();
		 		$("#MTech").show();
		 	}
		 	else if (selvalue == "PhD"){
		 		$(".year").hide();
		 		//$("#PhD").show();
		 	}
		 	else{
		 		$(".year").hide();
		 	}
		 });
	};

	$("#People").change(function() {
		var selvalue = $("#People option:selected").text();
		if (selvalue == "Students"){
			$("#Students").show();
			$.Studentselect();
		}
		else {
			$("#Students").hide();
		}
	});
});
