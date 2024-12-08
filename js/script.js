document.addEventListener("DOMContentLoaded", () => {
  const locOpenButton = document.querySelectorAll(".project__map__item__button");
  const locCloseButton = document.querySelectorAll(".project__map__item__button__close");
  const projectsMap = document.querySelector(".projects__map");
  const projectsList = projectsMap.querySelectorAll(".project__map__item__inner");

  locOpenButton.forEach((item) => {
    item.addEventListener("click", (e) => {
      projectsList.forEach((project) => {
        if (project == item.nextElementSibling) {
          project.classList.add("active");
        } else {
          project.classList.remove("active");
        }
      });
    });
  });

  locCloseButton.forEach((item) => {
    item.addEventListener("click", (e) => {
      item.parentElement.classList.remove("active");
    });
  });

  const animateElems = document.querySelectorAll(".scroll_animate");
  if (animateElems.length > 0) {
    window.addEventListener("scroll", animateOnScroll);
    function animateOnScroll() {
      for (let index = 0; index < animateElems.length; index++) {
        const animateElem = animateElems[index];
        const animateElemHight = animateElem.offsetHeight;
        const animateElemPosY = getCoords(animateElem).top;
        const animateDelay = 10;
        const clientHeight = window.innerHeight;

        let animateElemPoint = clientHeight - animateElemHight / animateDelay;
        if (animateElemHight > clientHeight) animateElemPoint = clientHeight - clientHeight / animateDelay;
        console.log(scrollY + clientHeight);
        console.log(animateElemHight);

        if (scrollY > animateElemPosY - animateElemPoint) animateElem.classList.add("visible");
      }
    }

    animateOnScroll();

    function getCoords(elem) {
      let box = elem.getBoundingClientRect();

      return {
        top: box.top + window.pageYOffset,
        right: box.right + window.pageXOffset,
        bottom: box.bottom + window.pageYOffset,
        left: box.left + window.pageXOffset,
      };
    }
  }
});
