function enterButtonStyle() {
    champion_div.classList.replace("champion_div", "champion_divOver");
}

function leaveButtonStyle() {
    champion_div.classList.replace("champion_divOver", "champion_div");
}

var champion_card = document.getElementById('champion_div');

champion_card.addEventListener("mouseenter", enterButtonStyle);
champion_card.addEventListener("mouseleave", leaveButtonStyle);
