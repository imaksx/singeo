document.addEventListener('DOMContentLoaded', function() {
    const loadMoreButton = document.getElementById('load-more');
    
    if (loadMoreButton) {
        loadMoreButton.addEventListener('click', function() {
            const nextPage = this.getAttribute('data-page');
            const container = document.getElementById('news-container');
            
            // Показываем индикатор загрузки
            this.innerHTML = '<span>Загрузка...</span>';
            
            // Делаем AJAX-запрос
            fetch(`?page=${nextPage}`, {
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                // Добавляем новые новости
                data.news.forEach(article => {
                    const card = document.createElement('div');
                    card.className = 'card';
                    
                    let imageHTML = '<p>Нет изображений</p>';
                    if (article.image_url) {
                        imageHTML = `<img src="${article.image_url}" alt="card__prev-img" class="news-image">`;
                    }
                    
                    card.innerHTML = `
                        <div class="card__prev">
                            ${imageHTML}
                        </div>
                        <div class="card__content">
                            <div class="card__timestamp">${article.pub_date}</div>
                            <div class="card__title card__title_news">${article.name}</div>
                            <div class="card__desc">${article.text.substring(0, 150)}...</div>
                            <a href="${article.detail_url}" class="button button__accent__light card__button">
                                <span>Читать дальше</span>
                            </a>
                        </div>
                    `;
                    container.appendChild(card);
                });
                
                // Обновляем кнопку
                if (data.has_next) {
                    this.setAttribute('data-page', parseInt(nextPage) + 1);
                    this.innerHTML = '<span>Показать больше</span>';
                } else {
                    // Скрываем кнопку, если больше нет новостей
                    this.parentElement.style.display = 'none';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                this.innerHTML = '<span>Ошибка загрузки</span>';
            });
        });
    }
});