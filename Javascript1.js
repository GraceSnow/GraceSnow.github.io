function changeImage() {
	var image = document.getElementById("butterfly1");
	//image.src="image3.jpg";
	if (image.src.match("butterfly1.jpg")) {
		image.src = "smallpig_game.png";
		image.alt = "pig";
	}
	else {
		image.src = "butterfly1.jpg";
		image.alt = "butterfly1";
	}
}
function myFunction() {
    document.getElementById("frm1").submit();
}