
function validateForm() {
	var x = document.forms["fileUploadForm"]["data"].value;
	if (x == "") {
		alert("Choose a file to apply the classifer.");
		return false;
	} else if (x.endsWith(".csv") == false) {
		alert("Choose a CSV file as a dataset.");
		return false;
	}
}
