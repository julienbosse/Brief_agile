$(document).ready(function() {


$(window).scroll(function() {
    var scroll = $(window).scrollTop();

     //>=, not <=
    if (scroll >= 60) {
        //clearHeader, not clearheader - caps H
        //$(".navbar").addClass("bg-light");
        $(".navbar").addClass("scrolled");
        $(".nav-link").addClass("white-scroll");
        $("a.navbar-brand").addClass("white-scroll");
    } else {
      $(".navbar").removeClass("scrolled");
      $(".nav-link").removeClass("white-scroll");
      $("a.navbar-brand").removeClass("white-scroll");
    }
}); //missing );

// document ready
});