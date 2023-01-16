function toggleSearch() {
    const searchCont = document.querySelector(".search-cont");
    if (searchCont.style.display == 'none') {
        searchCont.style.display = 'flex';
    } else {
        searchCont.style.display = 'none';
    }
}

toggleSearch();
document.querySelector(".search-icon").addEventListener("click", toggleSearch);


function toggleMenu() {
    const menu = document.querySelector(".menu");
    const icon = document.querySelector("#menu-btn .bi");
    if (menu.style.display == 'none') {
        menu.style.display = 'flex';
        icon.classList.remove("bi-list");
        icon.classList.add("bi-x-square");
    } else {
        menu.style.display = 'none';
        icon.classList.remove("bi-x-square");
        icon.classList.add("bi-list");
    }
}

toggleMenu();
document.querySelector("#menu-btn").addEventListener("click", toggleMenu);


// ========== Swiper ========== //
var swiper = new Swiper(".mySwiper", {
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        type: "progressbar",
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
    },
    effect: 'fade',
    fadeEffect: {
        crossFade: true
    },
});