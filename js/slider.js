// document.addEventListener("DOMContentLoaded", () => {
//   const carousel = document.querySelector(".carousel__cards");
//   const prevButton = document.querySelector(".products__carousel__pagination-prev");
//   const nextButton = document.querySelector(".products__carousel__pagination-next");
//   const cardsList2 = document.querySelectorAll(".carousel-item.card");
//   console.log(cardsList2[1]);

//   /*const cardsList = [
//     {
//       id: 0,
//       src: "./src/img/product.png",
//       title: "Датчик нагрузки анкерный 0",
//       desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
//     },
//     {
//       id: 1,
//       src: "./src/img/product.png",
//       title: "Датчик нагрузки анкерный 1",
//       desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
//     },
//     {
//       id: 2,
//       src: "./src/img/product.png",
//       title: "Датчик нагрузки анкерный 2",
//       desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
//     },
//     {
//       id: 3,
//       src: "./src/img/product.png",
//       title: "Датчик нагрузки анкерный 3",
//       desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
//     },
//     {
//       id: 4,
//       src: "./src/img/product.png",
//       title: "Датчик нагрузки анкерный 4",
//       desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
//     },
//     {
//       id: 5,
//       src: "./src/img/product.png",
//       title: "Датчик нагрузки анкерный 5",
//       desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
//     },
//     {
//       id: 6,
//       src: "./src/img/product.png",
//       title: "Датчик нагрузки анкерный 6",
//       desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
//     },
//     {
//       id: 7,
//       src: "./src/img/product.png",
//       title: "Датчик нагрузки анкерный 7",
//       desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
//     },
//   ];
//   */

//   const cardsList = [
//     {
//       id: 0,
//       src: "./src/img/product.png",
//       title: "Датчик нагрузки анкерный 0",
//       desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
//     },
//     {
//       id: 1,
//       src: "./src/img/product.png",
//       title: "Датчик нагрузки анкерный 1",
//       desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
//     },
//     {
//       id: 2,
//       src: "./src/img/product.png",
//       title: "Датчик нагрузки анкерный 2",
//       desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
//     },
//   ];
//   let startCard = 0;
//   let endCard = startCard + cardsList2.length;
//   let isLoading = false;

//   const Card = function ({ id, src, title, desc }) {
//     const card = document.createElement("div");
//     card.classList.add("card");
//     card.innerHTML += `
//         <div class="card__preview">
//           <img src="${src}" alt="card__prev-img">
//         </div>
//         <div class="card__content">
//           <div class="card__title">${title}</div>
//           <div class="card__desc">${desc}</div>
//           <a href="./product.html" class="button button__accent card__button">
//             <span>
//               Смотреть
//             </span>
//           </a>
//         </div>
//     `;
//     return card;
//   };

//   console.log(Card(cardsList[1]));

//   const initSlider = () => {
//     for (let i = startCard; i < endCard; i++) {
//       const card = Card(cardsList[i]);
//       //carousel.append(card);
//     }

//     console.log(1);

//     if (cardsList2.length <= 4) {
//       carousel.style.left = "0";
//       carousel.style.justifyContent = "start";
//       prevButton.style.display = nextButton.style.display = "none";
//       return;
//     }

//     carousel.prepend(loadPrevCard());
//     carousel.append(loadNextCard());
//   };

//   const loadPrevCard = () => {
//     let prevCard = startCard - 1;
//     if (prevCard < 0) prevCard = cardsList.length - 1;
//     return cardsList2[prevCard];
//   };

//   const loadNextCard = () => {
//     let nextCard = endCard;
//     if (nextCard >= cardsList2.length) nextCard = 0;
//     return cardsList2[nextCard];
//   };

//   const nextSlide = () => {
//     if (isLoading) return;
//     isLoading = !isLoading;
//     startCard += 1;
//     endCard += 1;
//     if (endCard >= cardsList2.length) {
//       endCard = 0;
//     }
//     if (startCard >= cardsList2.length) {
//       startCard = 0;
//     }

//     animate({
//       timing: function (timeFraction) {
//         return timeFraction;
//       },
//       draw: function (progress) {
//         carousel.children[0].style.marginLeft = -34.8 * progress + "rem";
//       },
//       duration: 600,
//       removeElement: carousel.children[0],
//       direction: "next",
//     });
//   };

//   const prevSlide = () => {
//     if (isLoading) return;
//     isLoading = !isLoading;
//     startCard -= 1;
//     endCard -= 1;
//     if (endCard < 0) {
//       endCard = cardsList.length - 1;
//     }
//     if (startCard < 0) {
//       startCard = cardsList.length - 1;
//     }

//     animate({
//       timing: function (timeFraction) {
//         return timeFraction;
//       },
//       draw: function (progress) {
//         carousel.children[0].style.marginLeft = 34.8 * progress + "rem";
//         if (progress == 1) carousel.children[0].style.marginLeft = 0;
//       },
//       duration: 600,
//       removeElement: carousel.children[carousel.children.length - 1],
//       direction: "prev",
//     });
//   };

//   const animate = ({ timing, draw, duration, removeElement, direction }) => {
//     const start = performance.now();

//     requestAnimationFrame(function animate(time) {
//       let timeFraction = (time - start) / duration;
//       if (timeFraction > 1) timeFraction = 1;

//       let progress = timing(timeFraction);

//       draw(progress);

//       if (timeFraction < 1) {
//         requestAnimationFrame(animate);
//       } else {
//         removeElement.style.display = "none";
//         isLoading = false;
//         if (direction == "prev") {
//           carousel.prepend(loadPrevCard());
//         }
//         if (direction == "next") {
//           carousel.append(loadNextCard());
//         }
//       }
//     });
//   };

//   nextButton.addEventListener("click", nextSlide);

//   prevButton.addEventListener("click", prevSlide);

//   initSlider();
// });

const carousels = document.querySelectorAll(".carousel");

var initSlider = function (countWidth, carousel) {
  const carouselInner = carousel.querySelector(".carousel__cards");
  const carouselItemList = carousel.querySelectorAll(".carousel-item");
  const carouselPagPoint = carousel.querySelector(".carousel__pagination_point");
  const carouselPagArrow = carousel.querySelector(".carousel__pagination_arrow");

  let currentItem = 0;
  let isAnimate = false;

  if (carouselItemList.length <= countWidth || carouselItemList.length <= 0) {
    if (carouselPagArrow) carouselPagArrow.style.display = "none";
    return;
  }

  if (carouselPagPoint) {
    carouselItemList.forEach((item, index) => {
      carouselPagPoint.innerHTML += `
      <div class="carousel__pagination_point__item" data-id = ${index}>
        <span>${index + 1}</span>
      </div>
      `;
    });

    carouselPagPoint.addEventListener("click", (e) => {
      if (!e.target.closest(".carousel__pagination_point") || isAnimate || !e.target.closest(".carousel__pagination_point__item")) return;
      let target = e.target.closest(".carousel__pagination_point__item");

      target.style.opacity = ".6";

      if (Number(target.dataset.id) || Number(target.dataset.id) == 0) {
        currentItem = target.dataset.id;
      }
      updatePosition(currentItem);
    });
  }

  if (carouselPagArrow) {
    const prevBtn = carouselPagArrow.querySelector(".carousel__pagination-prev");
    const nextBtn = carouselPagArrow.querySelector(".carousel__pagination-next");
    nextBtn.addEventListener("click", (e) => {
      if (isAnimate) return;
      currentItem++;

      prevBtn.disabled = false;
      if (Visible(carouselItemList[carouselItemList.length - 1])) {
        nextBtn.disabled = true;
        currentItem--;
        return;
      }
      updatePosition(currentItem);
    });
    prevBtn.addEventListener("click", (e) => {
      if (isAnimate) return;
      currentItem--;
      nextBtn.disabled = false;
      if (Visible(carouselItemList[0])) {
        prevBtn.disabled = true;
        currentItem++;
        return;
      }
      updatePosition(currentItem);
    });
  }

  var updatePosition = function (currentItem) {
    let width = carouselItemList[1].offsetLeft;
    let width2 = carouselItemList[0].offsetWidth;

    carouselInner.style.transform = `translateX(${-currentItem * width}px)`;

    isAnimate = true;
    setTimeout(() => {
      isAnimate = false;
    }, 600);

    if (carouselPagPoint) {
      Points = carouselPagPoint.querySelectorAll(".carousel__pagination_point__item");
      Points.forEach((point, index) => {
        if (currentItem == index) {
          point.style.opacity = "1";

          point.style.transform = "scale(1, 1)";
        } else {
          point.style.opacity = ".6";
          point.style.transform = "scale(.8, .8)";
        }
      });
    }
  };

  var Visible = function (target) {
    const container = document.querySelector(".container");

    // Все позиции элемента
    var targetPosition = {
        top: window.scrollY + target.getBoundingClientRect().top,
        left: window.scrollX + target.getBoundingClientRect().left,
        right: window.scrollX + target.getBoundingClientRect().right,
        bottom: window.scrollY + target.getBoundingClientRect().bottom,
      },
      // Получаем позиции окна
      windowPosition = {
        top: window.scrollY,
        left: window.scrollX + container.offsetLeft,
        right: window.scrollX + container.offsetLeft + container.clientWidth,
        bottom: window.scrollY + document.documentElement.clientHeight,
      };

    if (
      // Если позиция верхней части элемента меньше позиции нижней чайти окна, то элемент виден снизу
      targetPosition.right - 50 < windowPosition.right && // Если позиция правой стороны элемента больше позиции левой части окна, то элемент виден слева
      targetPosition.left + 50 > windowPosition.left
    ) {
      // Если позиция левой стороны элемента меньше позиции правой чайти окна, то элемент виден справа
      // Если элемент полностью видно, то запускаем следующий код
      return true;
    } else {
      // Если элемент не видно, то запускаем этот код
      return false;
    }
  };

  updatePosition(currentItem);
};

const project = document.querySelector(".projects");
const product = document.querySelector(".products");
const news = document.querySelector(".news__banner");
const team = document.querySelector(".team");
if (project) {
  const projectCarousels = project.querySelectorAll(".carousel");
  projectCarousels.forEach((carousel) => {
    initSlider(1, carousel);
  });
}
if (product) {
  const productCarousels = product.querySelectorAll(".carousel");
  productCarousels.forEach((carousel) => {
    initSlider(4, carousel);
  });
}
if (news) {
  const newsCarousels = news.querySelectorAll(".carousel");
  newsCarousels.forEach((carousel) => {
    initSlider(1, carousel);
  });
}
if (team) {
  const teamCarousels = team.querySelectorAll(".carousel");
  teamCarousels.forEach((carousel) => {
    initSlider(4, carousel);
  });
}
