let count = 0;

function changeImage(src) {
    document.querySelector("img").src = "./images/" + src + ".png";
}

document.body.onmousedown = function () {
    count += 1;
    document.querySelector("#pop").textContent = count;
    changeImage("unko_gorilla");
}
document.body.onmouseup = function () {
    changeImage("gorilla_banana");
}
