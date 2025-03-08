document.addEventListener("DOMContentLoaded", function () {
    // Найти все радиокнопки на странице
    const radios = document.querySelectorAll('input[type="radio"]');

    // Функция для обновления данных при смене радиокнопки
    function updateServiceDetails(event) {
        // Получаем id текущего сервиса
        const serviceId = event.target.name.split('_')[1];

        // Находим соответствующие элементы для body_parts и price
        const bodyPartsElement = document.getElementById('body_parts_' + serviceId);
        const priceElement = document.getElementById('price_' + serviceId);

        // Обновляем данные в зависимости от выбранной радиокнопки
        const selectedOption = event.target;
        bodyPartsElement.textContent = selectedOption.getAttribute('data-parts');
        priceElement.textContent = selectedOption.getAttribute('data-price') + " грн";
    }

    // Добавляем обработчик события для каждой радиокнопки
    radios.forEach(radio => {
        radio.addEventListener('change', updateServiceDetails);
    });
});