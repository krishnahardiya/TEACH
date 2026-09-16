// Menu button ko HTML se select kar rahe hain
const menuButton = document.getElementById("menuButton");

// Navigation menu ko HTML se select kar rahe hain
const menu = document.getElementById("menu");

// Button par click hone par menu show ya hide hoga
menuButton.addEventListener("click", function () {
    menu.classList.toggle("show");
});

// Menu ke kisi link par click karne ke baad mobile menu band ho jayega
const menuLinks = document.querySelectorAll("#menu a");

menuLinks.forEach(function (link) {
    link.addEventListener("click", function () {
        menu.classList.remove("show");
    });
});
