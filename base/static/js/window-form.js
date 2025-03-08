document.addEventListener('DOMContentLoaded', () => {
    const windowForm = document.getElementById('window-form');
    const openButtons = document.querySelectorAll('.site-but, .signup-btn-header, .order-button, .subscription-button');
    const closeButton = document.querySelector('#window-form .close-button');

    // Открытие формы
    openButtons.forEach(button => {
        button.addEventListener('click', () => {
            windowForm.style.display = 'flex';
        });
    });

    if (closeButton) {
        closeButton.addEventListener('click', () => {
            const windowForm = document.getElementById('window-form');
            windowForm.style.display = 'none';
        });
    } else {
        console.error('Close button not found');
    }

    // Закрытие формы при клике вне контента
    windowForm.addEventListener('click', (event) => {
        if (event.target === windowForm) {
            windowForm.style.display = 'none';
        }
    });
});
