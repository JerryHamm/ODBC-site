/*!
* Start Bootstrap - Creative v7.0.6 (https://startbootstrap.com/theme/creative)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-creative/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');

        if (!navbarCollapsible && navbarDropdownItemColourChange) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
            document.getElementById("nav-dropdown-item-1").style.color = "#6c757d";
            document.getElementById("nav-dropdown-item-2").style.color = "#6c757d";
            document.getElementById("nav-dropdown-item-3").style.color = "#6c757d";
            document.getElementById("nav-dropdown-item-4").style.color = "#6c757d";
            document.getElementById("nav-dropdown-item-5").style.color = "#6c757d";
            document.getElementById("nav-dropdown-item-6").style.color = "#6c757d";
            document.getElementById("nav-dropdown-item-7").style.color = "#6c757d";
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
            document.getElementById("nav-dropdown-item-1").style.color = "#000";
            document.getElementById("nav-dropdown-item-2").style.color = "#000";
            document.getElementById("nav-dropdown-item-3").style.color = "#000";
            document.getElementById("nav-dropdown-item-4").style.color = "#000";
            document.getElementById("nav-dropdown-item-5").style.color = "#000";
            document.getElementById("nav-dropdown-item-6").style.color = "#000";
            document.getElementById("nav-dropdown-item-7").style.color = "#000";
        }

    };


    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    // Activate SimpleLightbox plugin for portfolio items
    new SimpleLightbox({
        elements: '#portfolio a.portfolio-box'
    });

});
