$(function () {
  'use strict';
  //Adjust slider height

  var winH = $(window).height(),
    navH = $('#lari-header').innerHeight();
  $('#lari-carousel, .carousel-item').height(winH - navH);
});

// Add background to navbar when scrolled
$(document).ready(function () {
  var scrollTop = 0;
  $(window).scroll(function () {
    scrollTop = $(window).scrollTop();

    if (scrollTop >= 100) {
      $('#lari-header').addClass('scrolled-nav');
    } else if (scrollTop < 100) {
      $('#lari-header').removeClass('scrolled-nav');
    }
  });

  /*Overlay Menu*/
  $('#toggle').click(function () {
    $(this).toggleClass('active');
    $('#overlay').toggleClass('open');
    $('#lari-header').toggleClass('overlay-opened');
    $('body').toggleClass('overlay-opened');
  });

  /*Hover sub menu*/
  $(".hoverzone").hover(function () {
    $(this).children(".sub-menu").addClass("submenu-opened");
  }, function () {
    $(this).children(".sub-menu").removeClass("submenu-opened");
  });
});