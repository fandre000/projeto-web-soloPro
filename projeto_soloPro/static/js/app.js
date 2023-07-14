$(".menu-bar").on("click", function () {
    $(".barra-lateral").addClass("active");
});

$(".close-barra-lateral").on("click", function(){
    $(".barra-lateral").removeClass("active");
}


)


const candidatos = document.querySelector('.candidatos');
let startY;
let startScrollTop;

candidatos.addEventListener('mousedown', (event) => {
  startY = event.pageY;
  startScrollTop = candidatos.scrollTop;

  candidatos.addEventListener('mousemove', moveHandler);
  candidatos.addEventListener('mouseup', removeMoveHandler);
});

function moveHandler(event) {
  const deltaY = event.pageY - startY;
  candidatos.scrollTop = startScrollTop - deltaY;
}

function removeMoveHandler() {
    candidatos.removeEventListener('mousemove', moveHandler);
    candidatos.removeEventListener('mouseup', removeMoveHandler);
}










