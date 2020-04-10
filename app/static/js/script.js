var modal_image = document.getElementById("modal-image");
var modal_title = document.getElementById("modal-title");
var img_description = document.getElementById("img-description");

document.addEventListener('click', preview);
function preview(event) {
	if (event.target.className=="pic") {
		var pic_div = event.target.parentElement;
		modal_image.src = pic_div.childNodes[0].src;
		modal_title.innerHTML = pic_div.childNodes[1].innerHTML;
		img_description.innerHTML = "Info about " + modal_title.innerHTML;
	}
}
