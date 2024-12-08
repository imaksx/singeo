document.addEventListener("DOMContentLoaded", () => {
  const carousel = document.querySelector(".carousel__cards");
  const prevButton = document.querySelector(".products__carousel__pagination-prev");
  const nextButton = document.querySelector(".products__carousel__pagination-next");
  const cardsList = [
    {
      id: 0,
      src: "./src/img/product.png",
      title: "Датчик нагрузки анкерный 0",
      desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
    },
    {
      id: 1,
      src: "./src/img/product.png",
      title: "Датчик нагрузки анкерный 1",
      desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
    },
    {
      id: 2,
      src: "./src/img/product.png",
      title: "Датчик нагрузки анкерный 2",
      desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
    },
    {
      id: 3,
      src: "./src/img/product.png",
      title: "Датчик нагрузки анкерный 3",
      desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
    },
    {
      id: 4,
      src: "./src/img/product.png",
      title: "Датчик нагрузки анкерный 4",
      desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
    },
    {
      id: 5,
      src: "./src/img/product.png",
      title: "Датчик нагрузки анкерный 5",
      desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
    },
    {
      id: 6,
      src: "./src/img/product.png",
      title: "Датчик нагрузки анкерный 6",
      desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
    },
    {
      id: 7,
      src: "./src/img/product.png",
      title: "Датчик нагрузки анкерный 7",
      desc: "Yorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate liberoetvelit interdum, ac aliquet odio mattis.",
    },
  ];
  let startCard = 0;
  let endCard = startCard + 4;
  let isLoading = false;

  const Card = function ({ id, src, title, desc }) {
    const card = document.createElement("div");
    card.classList.add("card");
    card.innerHTML += `
        <div class="card__preview">
          <img src="${src}" alt="card__prev-img">
        </div>
        <div class="card__content">
          <div class="card__title">${title}</div>
          <div class="card__desc">${desc}</div>
          <a href="/" class="button card__button">
            <span>
              Смотреть
            </span>
          </a>
        </div>
    `;
    return card;
  };

  const initSlider = () => {
    for (let i = startCard; i < endCard; i++) {
      const card = Card(cardsList[i]);
      carousel.append(card);
    }

    carousel.prepend(loadPrevCard());
    carousel.append(loadNextCard());
  };

  const loadPrevCard = () => {
    let prevCard = startCard - 1;
    if (prevCard < 0) prevCard = cardsList.length - 1;
    return Card(cardsList[prevCard]);
  };

  const loadNextCard = () => {
    let nextCard = endCard;
    if (nextCard >= cardsList.length) nextCard = 0;
    return Card(cardsList[nextCard]);
  };

  const nextSlide = () => {
    if (isLoading) return;
    isLoading = !isLoading;
    startCard += 1;
    endCard += 1;
    if (endCard >= cardsList.length) {
      endCard = 0;
    }
    if (startCard >= cardsList.length) {
      startCard = 0;
    }

    animate({
      timing: function (timeFraction) {
        return timeFraction;
      },
      draw: function (progress) {
        carousel.children[0].style.marginLeft = -34.8 * progress + "rem";
      },
      duration: 600,
      removeElement: carousel.children[0],
      direction: "next",
    });
  };

  const prevSlide = () => {
    if (isLoading) return;
    isLoading = !isLoading;
    startCard -= 1;
    endCard -= 1;
    if (endCard < 0) {
      endCard = cardsList.length - 1;
    }
    if (startCard < 0) {
      startCard = cardsList.length - 1;
    }

    animate({
      timing: function (timeFraction) {
        return timeFraction;
      },
      draw: function (progress) {
        carousel.children[0].style.marginLeft = 34.8 * progress + "rem";
        if (progress == 1) carousel.children[0].style.marginLeft = 0;
      },
      duration: 600,
      removeElement: carousel.children[carousel.children.length - 1],
      direction: "prev",
    });
  };

  const animate = ({ timing, draw, duration, removeElement, direction }) => {
    const start = performance.now();

    requestAnimationFrame(function animate(time) {
      let timeFraction = (time - start) / duration;
      if (timeFraction > 1) timeFraction = 1;

      let progress = timing(timeFraction);

      draw(progress);

      if (timeFraction < 1) {
        requestAnimationFrame(animate);
      } else {
        removeElement.remove();
        isLoading = false;
        if (direction == "prev") {
          carousel.prepend(loadPrevCard());
        }
        if (direction == "next") {
          carousel.append(loadNextCard());
        }
      }
    });
  };

  nextButton.addEventListener("click", nextSlide);

  prevButton.addEventListener("click", prevSlide);

  initSlider();
});
