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


// Slider code
const next_btn = document.querySelector(".next-btn");
const prev_btn = document.querySelector(".prev-btn");

