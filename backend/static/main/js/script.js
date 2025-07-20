YourNamespace = {
  index: {
    init: function () {
      document.addEventListener("DOMContentLoaded", () => {
        const locOpenButton = document.querySelectorAll(".project__map__item__button");
        const locCloseButton = document.querySelectorAll(".project__map__item__button__close");
        const projectsMap = document.querySelector(".projects__map");
        const projectsList = projectsMap.querySelectorAll(".project__map__item__wrapper");

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
            console.log(item)
            item.closest(".active").classList.remove("active");
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
      const moreButton = document.querySelector(".products__button__more");
      const productsRow = document.querySelector(".products__row");
      if (moreButton)
      {let counter = 1;
      moreButton.addEventListener("click", async () => {
        let res = await getProducts();
        let newCard = "";
        console.log('Перед forEach', res);
        res.products.forEach((item) => {
          newCard += `
                <div class="card ">
                      <div class="card__prev">
                        <img src="${item.preview}" alt="card__prev-img">
                      </div>
                      <div class="card__content ">
                        <div class="card__title">${item.name}
                        </div>
                        <div class="card__desc">${item.short_description}</div>
                        <a href="${item.detail_url}" class="button button__accent card__button">
                          <span>
                            Смотреть
                          </span>
                        </a>
                      </div>
                    </div>
                `;
        });

        productsRow.innerHTML += newCard;
        if (res.checker == false) moreButton.style.display = "None";
        counter += 1;
      });

      let getProducts = async function () {
        const url = `ajax/${counter}`;
        let res = await fetch(url, {
          method: "GET",
        });

        let products = res.json();
        return products;
      };}
    },
  },
  product_detail: {
    init: function () {
      const props = document.querySelectorAll(".product__props");
      props.forEach((prop) => {
        const propsTitle = prop.querySelector(".product__props__title");
        propsTitle.addEventListener("click", (e) => {
          propsTitle.closest(".product__props").classList.toggle("active");
        });
      });
    },
  },
  projects: {
    init: function () {
      const filters = document.querySelector(".projects__filters");
      const projectsObjects = [];
      let activeFilters = {
        objects: [],
        industry: [],
        products: [],
      };
      const projects = document.querySelectorAll(".card");

      projects.forEach((project) => {
        let objects = project.getAttribute("data-object-tags").split(",");
        let industry = project.getAttribute("data-industry-tags").split(",");
        let products = project.getAttribute("data-products").split(",");
        objects.pop();
        industry.pop();
        products.pop();

        let tags = {
          project,
          objects,
          industry,
          products,
        };

        projectsObjects.push(tags);
      });

      filters.addEventListener("click", (e) => {
        if (
          !e.target.closest(".projects__filters__area") ||
          (e.target.closest(".projects__filters__dropdown") && !e.target.classList.contains("projects__filters__item__text"))
        ) {
          return;
        }

        if (e.target.classList.contains("projects__filters__item__text")) {
          const item = e.target;
          const tagName = item.innerText;
          item.previousElementSibling.checked = item.previousElementSibling.checked ? false : true;

          if (item.previousElementSibling.getAttribute("data-filter-type") == "object") {
            if (activeFilters.objects.includes(item.previousElementSibling.getAttribute("data-filter-id"))) {
              let i = activeFilters.objects.indexOf(item.previousElementSibling.getAttribute("data-filter-id"));
              activeFilters.objects.splice(i, 1);
            } else {
              activeFilters.objects.push(item.previousElementSibling.getAttribute("data-filter-id"));
            }
          } else if (item.previousElementSibling.getAttribute("data-filter-type") == "industry") {
            if (activeFilters.industry.includes(item.previousElementSibling.getAttribute("data-filter-id"))) {
              let i = activeFilters.industry.indexOf(item.previousElementSibling.getAttribute("data-filter-id"));
              activeFilters.industry.splice(i, 1);
            } else {
              activeFilters.industry.push(item.previousElementSibling.getAttribute("data-filter-id"));
            }
          } else if (item.previousElementSibling.getAttribute("data-filter-type") == "projects") {
            if (activeFilters.products.includes(item.previousElementSibling.getAttribute("data-filter-id"))) {
              let i = activeFilters.products.indexOf(item.previousElementSibling.getAttribute("data-filter-id"));
              activeFilters.products.splice(i, 1);
            } else {
              activeFilters.products.push(item.previousElementSibling.getAttribute("data-filter-id"));
            }
          } else {
            console.log("nothing");
          }

          checkFilters();
          return;
        }

        let target = e.target.closest(".projects__filters__area");

        target.classList.toggle("active");

        showDropDown();
      });

      function showDropDown(item) { }
      function checkFilters() {
        projectsObjects.forEach((item) => {
          let { project, objects, industry, products } = item;
          let boolObjects = true,
            boolIndustry = true,
            boolProducts = true;

          activeFilters.objects.forEach((tag) => {
            if (!objects.includes(tag)) {
              boolObjects = false;
            }
          });
          activeFilters.industry.forEach((tag) => {
            if (!industry.includes(tag)) {
              boolIndustry = false;
            }
          });
          activeFilters.products.forEach((tag) => {
            if (!products.includes(tag)) {
              boolProducts = false;
            }
          });

          if (boolObjects && boolIndustry && boolProducts) {
            project.style.display = "flex";
          } else {
            project.style.display = "none";
          }
        });
      }
    },
  },
  about: {
    init: function () {
      document.addEventListener("DOMContentLoaded", () => {
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
  news_detail: {
    init: function () {
      const copyButton = document.querySelector(".news-content__buttons .button");

      copyButton.addEventListener("click", () => {
        const currentUrl = window.location.href;
        navigator.clipboard.writeText(currentUrl);
      });
    },
  },
  news: {
    init: function () {
      const moreButton = document.querySelector(".news__button__more");
      const newsRow = document.querySelector(".news__row");
      if (moreButton)
      {let counter = 1;
      moreButton.addEventListener("click", async () => {
        let res = await getNews();
        let newCard = "";
        console.log('Перед forEach', res);
        res.news.forEach((item) => {
          newCard += `
                <div class="card ">
                      <div class="card__prev">
                        <img src="${item.image_url}" alt="card__prev-img">
                      </div>
                      <div class="card__content ">
                        <div class="card__timestamp">${item.pub_date}</div>
                        <div class="card__title card__title_news">${item.name}
                        </div>
                        <div class="card__desc">${item.text}</div>
                        <a href="${item.detail_url}" class="button button__accent__light card__button">
                          <span>
                            Читать дальше
                          </span>
                        </a>
                      </div>
                    </div>
                `;
        });

        newsRow.innerHTML += newCard;
        if (res.checker == false) moreButton.style.display = "None";
        counter += 1;
      });

      let getNews = async function () {
        const url = `ajax/${counter}`;
        let res = await fetch(url, {
          method: "GET",
        });

        let news = res.json();
        return news;
      };}
    },
  },
};

{
  UTIL = {
    fire: function (func, funcname, args) {
      var namespace = YourNamespace; // indicate your obj literal namespace here

      funcname = funcname === undefined ? "init" : funcname;
      if (func !== "" && namespace[func] && typeof namespace[func][funcname] == "function") {
        namespace[func][funcname](args);
      }
    },

    loadEvents: function () {
      var bodyDataPage = document.querySelector(".identificator").dataset.page;

      UTIL.fire(bodyDataPage);
    },
  };

  UTIL.loadEvents();
}

{
  const burger = document.querySelector(".burger");
  const navbar = document.querySelector(".header__navbar");
  const logo = document.querySelector(".header__logo");

  burger.addEventListener("click", (e) => {
    burger.classList.toggle("active");
    navbar.classList.toggle("active");
    logo.classList.toggle("active");
  });
}


