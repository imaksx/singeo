<<<<<<< HEAD:frontend/js/script.js
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
=======
YourNamespace = {
  index: {
    init: function () {
      document.addEventListener("DOMContentLoaded", () => {
        const locOpenButton = document.querySelectorAll(".project__map__item__button");
        const locCloseButton = document.querySelectorAll(".project__map__item__button__close");
        const projectsMap = document.querySelector(".projects__map");
        const projectsList = projectsMap.querySelectorAll(".project__map__item__inner");

        const filters = document.querySelector(".product__filters");

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
    },
  },

  products: {
    init: function () {
      const filters = document.querySelector(".product__filters");
      const filtersItems = document.querySelectorAll(".product__filters__item__text");

      console.log(filters);

      filters.addEventListener("click", (e) => {
        console.log(!e.target.closest(".product__filters__dropdown"));
        console.log(!e.target.closest(".product__filters__area"));

        if (!e.target.closest(".product__filters__area") || e.target.closest(".product__filters__dropdown")) return;
        let target = e.target.closest(".product__filters__area");
        console.log(target);

        target.classList.toggle("active");

        showDropDown();
      });

      filtersItems.forEach((item) => {
        item.addEventListener("click", (e) => {
          item.previousElementSibling.checked = item.previousElementSibling.checked ? false : true;
        });
      });

      function showDropDown(item) {}
    },
  },
  product: {
    init: function () {
      const propsTitle = document.querySelector(".product__props__title");
      propsTitle.addEventListener("click", (e) => {
        propsTitle.closest(".product__props").classList.toggle("active");
      });
    },
  },
  projects: {
    init: function () {
      const filters = document.querySelector(".projects__filters");
      const filtersItems = document.querySelectorAll(".projects__filters__item__text");

      console.log(filters);

      filters.addEventListener("click", (e) => {
        console.log(!e.target.closest(".projects__filters__dropdown"));
        console.log(!e.target.closest(".projects__filters__area"));

        if (!e.target.closest(".projects__filters__area") || e.target.closest(".projects__filters__dropdown")) return;
        let target = e.target.closest(".projects__filters__area");
        console.log(target);

        target.classList.toggle("active");

        showDropDown();
      });

      filtersItems.forEach((item) => {
        item.addEventListener("click", (e) => {
          item.previousElementSibling.checked = item.previousElementSibling.checked ? false : true;
        });
      });

      function showDropDown(item) {}
    },
  },
};

UTIL = {
  fire: function (func, funcname, args) {
    var namespace = YourNamespace; // indicate your obj literal namespace here

    funcname = funcname === undefined ? "init" : funcname;
    if (func !== "" && namespace[func] && typeof namespace[func][funcname] == "function") {
      namespace[func][funcname](args);
    }
  },

  loadEvents: function () {
    var bodyDataPage = document.querySelector("body").dataset.page;
    console.log(bodyDataPage);

    UTIL.fire(bodyDataPage);
  },
};

UTIL.loadEvents();

// document.addEventListener("DOMContentLoaded", () => {
//   const locOpenButton = document.querySelectorAll(".project__map__item__button");
//   const locCloseButton = document.querySelectorAll(".project__map__item__button__close");
//   const projectsMap = document.querySelector(".projects__map");
//   const projectsList = projectsMap.querySelectorAll(".project__map__item__inner");

//   const filters = document.querySelector(".product__filters");

//   locOpenButton.forEach((item) => {
//     item.addEventListener("click", (e) => {
//       projectsList.forEach((project) => {
//         if (project == item.nextElementSibling) {
//           project.classList.add("active");
//         } else {
//           project.classList.remove("active");
//         }
//       });
//     });
//   });

//   locCloseButton.forEach((item) => {
//     item.addEventListener("click", (e) => {
//       item.parentElement.classList.remove("active");
//     });
//   });

//   const animateElems = document.querySelectorAll(".scroll_animate");
//   if (animateElems.length > 0) {
//     window.addEventListener("scroll", animateOnScroll);
//     function animateOnScroll() {
//       for (let index = 0; index < animateElems.length; index++) {
//         const animateElem = animateElems[index];
//         const animateElemHight = animateElem.offsetHeight;
//         const animateElemPosY = getCoords(animateElem).top;
//         const animateDelay = 10;
//         const clientHeight = window.innerHeight;

//         let animateElemPoint = clientHeight - animateElemHight / animateDelay;
//         if (animateElemHight > clientHeight) animateElemPoint = clientHeight - clientHeight / animateDelay;

//         if (scrollY > animateElemPosY - animateElemPoint) animateElem.classList.add("visible");
//       }
//     }

//     animateOnScroll();

//     function getCoords(elem) {
//       let box = elem.getBoundingClientRect();

//       return {
//         top: box.top + window.pageYOffset,
//         right: box.right + window.pageXOffset,
//         bottom: box.bottom + window.pageYOffset,
//         left: box.left + window.pageXOffset,
//       };
//     }
//   }

//   console.log(filters);

//   filters.addEventListener("click", (e) => {
//     console.log(e.target);

//     showDropDown();
//   });

//   function showDropDown(item) {}
// });
>>>>>>> ee575966cbba1c211aaaf8a40c204de226509ae9:js/script.js
