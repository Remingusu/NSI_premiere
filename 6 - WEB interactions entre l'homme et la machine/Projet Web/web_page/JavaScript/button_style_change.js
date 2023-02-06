function enterButtonStyle() {
    submitButton.classList.replace("submitButtonOver", "submitButton");
}

function leaveButtonStyle() {
    submitButton.classList.replace("submitButton", "submitButtonOver");
}

var submitButton = document.getElementById('submitButton');

submitButton.addEventListener("mouseenter", enterButtonStyle);
submitButton.addEventListener("mouseleave", leaveButtonStyle);
