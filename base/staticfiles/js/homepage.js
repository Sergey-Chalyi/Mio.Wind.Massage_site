document.querySelectorAll('.go-to-profile').forEach(button => {
    button.addEventListener('click', (event) => {
        // Останавливаем всплытие, чтобы клик обрабатывался только на go-to-profile
        event.stopPropagation();

        // Находим родительский элемент с классом .card
        const card = button.closest('.card');

        // Переключаем класс flipped
        if (card) {
            card.classList.toggle('flipped');
        }
    });
});
