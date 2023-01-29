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
            document.getElementById("nav-logo-active").src = bg_logo;
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
            document.getElementById("nav-logo-active").src = bg_logo_active;
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

    //Array of images to show in homepage header slide show
    // var images=new Array(mast1, mast2, mast3, mast4);
     
    // var nextimage=0;

    // doSlideshow();

    // function doSlideshow(){
    //     if(nextimage>=images.length){nextimage=0;}
    //     $('header')
    //     .css({'background':'linear-gradient(to bottom, rgba(7, 32, 79, 0.8) 0%, rgba(7, 32, 79, 0.8) 100%), url("'+images[nextimage++]+'")', 
    //     'background-position':'center',
    //     'background-repeat':'no-repeat',
    //     'background-attachment':'scroll',
    //     'background-size':'cover',
    //     'animation':'masthead-slide 10s infinite alternate'})
    //     .fadeIn(500,function(){
    //         setTimeout(doSlideshow, 5000);
    //     });
    // }

});
