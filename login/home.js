const listItems = document.querySelectorAll(".main-menu li");

listItems.forEach((listItem) => {
  listItem.addEventListener("click", () => {
    listItems.forEach((otherItem) => {
      otherItem.classList.remove('active')
    })
    listItem.classList.add('active')
  });
});


document.addEventListener('DOMContentLoaded', function () {
  var uygulamalarMenu = document.getElementById('uygulamalar-menu');

  uygulamalarMenu.addEventListener('click', function () {
      this.classList.toggle('open');
  });
});
