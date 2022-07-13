const hamburger = document.querySelector(".hambuger")
const mobileMenu = document.querySelector(".Mobile-Menu ")

hamburger.addEventListener("click", toggler)


function toggler() {
    hamburger.classList.toggle("active");
    mobileMenu.classList.toggle("hidden")
}