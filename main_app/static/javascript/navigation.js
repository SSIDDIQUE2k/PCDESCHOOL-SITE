const bar = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');
let menuOpen = false;

bar.addEventListener('click', () => {
    if (menuOpen == false) {
        navLinks.style.display = 'block';
        menuOpen = true;
    } else if (menuOpen == true){ 
        navLinks.style.display = 'none';
        menuOpen = false;
    }
});