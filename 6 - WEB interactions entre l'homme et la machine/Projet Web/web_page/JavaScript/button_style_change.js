function enterButtonStyle() {
    submitButton.classList.replace("submitButton", "submitButtonOver");
}

function leaveButtonStyle() {
    submitButton.classList.replace("submitButtonOver", "submitButton");
}

var submitButton = document.getElementById('submitButton');

submitButton.addEventListener("mouseenter", enterButtonStyle);
submitButton.addEventListener("mouseleave", leaveButtonStyle);
