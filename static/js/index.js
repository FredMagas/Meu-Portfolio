window.onscroll = function() {
  var header = document.getElementById("header");
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
      header.classList.add("scrolled");
  } else {
      header.classList.remove("scrolled");
  }
}

var btnPageUp = document.querySelector(".btn-pageup");
btnPageUp.addEventListener("click", function(event) {
  event.preventDefault();
  window.scrollTo(0, 0);
});

function menu() {
  var x = document.getElementById("sidebar-menu");
  var icon = document.getElementById("menu-icon");

  if (x.className === "") {
    x.className += "responsive";
    icon.className = "fa-solid fa-xmark fa-xl";
  } else {
    x.className = "";
    icon.className = "fa-solid fa-bars fa-xl";
  }
}

$(document).ready(function(){
  $(".owl-carousel").owlCarousel({
      loop:true,
      margin:10,
      autoPlay:true,
      autoplayTimeout:1000,
      autoplayHoverPause:true,
      responsive:{
          0:{
              items:1
          },
          600:{
              items:2
          },
          1000:{
              items:3
          }
      }
  });
});