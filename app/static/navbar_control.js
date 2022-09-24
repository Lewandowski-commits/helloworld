window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    el_autohide = document.querySelector('.autohide');

    if (document.body.scrollTop > 1 || document.documentElement.scrollTop > 1) {
        el_autohide.classList.remove('scrolled-down');
        el_autohide.classList.add('scrolled-up');


    } else {
        el_autohide.classList.remove('scrolled-up');
        el_autohide.classList.add('scrolled-down');
    }
}