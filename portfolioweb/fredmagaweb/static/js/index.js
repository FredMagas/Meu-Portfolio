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

/* Alterne entre adicionar e remover a classe "responsive" para topnav quando o usuário clicar no ícone */
function myFunction() {
    var x = document.getElementById("sidebar-menu");
    if (x.className === "") {
      x.className += "responsive";
    } else {
      x.className = "";
    }
  }