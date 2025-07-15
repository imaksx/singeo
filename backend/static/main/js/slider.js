const carousels = document.querySelectorAll(".carousel");

var initSlider = function (controls) {
  let { countWidth, carousel, autoplay, swipe } = controls;
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

  if (autoplay) {
    setInterval(() => {
      if (!isAnimate) {
        currentItem++;
        if (currentItem > carouselItemList.length - 1) currentItem = 0;
        updatePosition(currentItem);
      }
    }, 5000);
  }

  if (swipe) {
    carousel.addEventListener("touchstart", handleTouchStart, false);
    carousel.addEventListener("touchmove", handleTouchMove, false);

    let xDown = null,
      yDown = null;

    // Фиксируем изначальные координаты прикосновения
    function handleTouchStart(evt) {
      const { clientX, clientY } = evt.touches[0];
      xDown = clientX;
      yDown = clientY;
    }

    // Отслеживаем движение пальца и определяем направление свайпа
    function handleTouchMove(evt) {
      if (!xDown || !yDown) {
        return; // Если изначальные координаты не зафиксированы, прекращаем выполнение
      }

      const { clientX, clientY } = evt.touches[0];

      const xDiff = xDown - clientX;
      const yDiff = yDown - clientY;

      // Вычисляем, был ли свайп выполнен по горизонтали или вертикали
      if (Math.abs(xDiff) > Math.abs(yDiff)) {
        if (xDiff > 0) {
          currentItem++;
          if (currentItem > carouselItemList.length - 1) currentItem = 0;
          updatePosition(currentItem);
        } else {
          currentItem--;
          if (currentItem < 0) currentItem = carouselItemList.length - 1;
          updatePosition(currentItem);
        }
      }

      // Обнуляем координаты после распознавания свайпа
      xDown = yDown = null;
    }
  }
};
//var initSlider = function (countWidth, carousel, autoplay = false) {
const project = document.querySelector(".projects");
const product = document.querySelector(".products");
const news = document.querySelector(".news__banner");
const team = document.querySelector(".team");
const productProject = document.querySelector(".product-project");
if (project) {
  const projectCarousels = project.querySelectorAll(".carousel");
  projectCarousels.forEach((carousel) => {
    initSlider({
      countWidth: 1,
      carousel,
      swipe: true,
    });
  });
}
if (product) {
  const productCarousels = product.querySelectorAll(".carousel");
  productCarousels.forEach((carousel) => {
    initSlider({
      countWidth: 4,
      carousel,
    });
  });
}
if (news) {
  const newsCarousels = news.querySelectorAll(".carousel");
  newsCarousels.forEach((carousel) => {
    initSlider({
      countWidth: 1,
      carousel,
      autoplay: true,
      swipe: true,
    });
  });
}
if (team) {
  const teamCarousels = team.querySelectorAll(".carousel");
  teamCarousels.forEach((carousel) => {
    initSlider({
      countWidth: 4,
      carousel,
    });
  });
}
if (productProject) {
  const productProjectCarousels = productProject.querySelectorAll(".carousel");
  productProjectCarousels.forEach((carousel) => {
    initSlider({
      countWidth: 1,
      carousel,
      swipe: true,
    });
  });
}