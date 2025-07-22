const carousels = document.querySelectorAll(".carousel");

var initSlider = function (countWidth, carousel) {
  console.log(carousel);
  const carouselInner = carousel.querySelector(".carousel__cards");
  const carouselItemList = carousel.querySelectorAll(".carousel-item");
  const carouselPagPoint = carousel.querySelector(".carousel__pagination_point");
  const carouselPagArrow = carousel.querySelector(".carousel__pagination_arrow");

  let currentItem = 0;
  let isAnimate = false;

  console.log(carousel, carouselInner, carouselItemList);
  console.dir(carouselInner.children);

  if (carouselItemList.length <= 0) {
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
      if (!e.target.closest(".carousel__pagination_point") || isAnimate) return;
      let target = e.target.closest(".carousel__pagination_point__item");
      console.dir(target);

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
      if (currentItem >= carouselItemList.length - countWidth + 1) {
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
      if (currentItem < 0) {
        prevBtn.disabled = true;
        currentItem++;
        return;
      }
      updatePosition(currentItem);
    });
  }

  var updatePosition = function (currentItem) {
    let width = carouselItemList[1].offsetLeft;

    console.log(`translateX(${(-currentItem * width) / 10}rem)`);

    carouselInner.style.transform = `translateX(${(-currentItem * width) / 10}rem)`;
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

  updatePosition(currentItem);
};

initSlider(4, carousels[0]);
initSlider(1, carousels[1]);
initSlider(1, carousels[2]);
