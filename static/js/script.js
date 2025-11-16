'use strict';

/**
 * element toggle function
 */

const elemToggleFunc = function (elem) { elem.classList.toggle("active"); }



/**
 * navbar variables
 */

const navToggleBtn = document.querySelector("[data-nav-toggle-btn]");
const navbar = document.querySelector("[data-navbar]");
const overlay = document.querySelector("[data-overlay]");
const header = document.querySelector("[data-header]");
const icon = navToggleBtn.querySelector("ion-icon");

// EVENT: Toggle Navbar
navToggleBtn.addEventListener("click", function () {

    navbar.classList.toggle("active");
    overlay.classList.toggle("active");

    // Ubah ikon menu → close
    if (navbar.classList.contains("active")) {
        icon.setAttribute("name", "close-outline"); // ikon silang
    } else {
        icon.setAttribute("name", "menu-outline"); // ikon menu
    }
});

// EVENT: Klik overlay → tutup menu
overlay.addEventListener("click", function () {
    navbar.classList.remove("active");
    overlay.classList.remove("active");
    icon.setAttribute("name", "menu-outline");
});
