document.querySelectorAll('.faq-title').forEach(title => {
    title.addEventListener('click', () => {
        const faqItem = title.parentElement;
        faqItem.classList.toggle('active');
    });
});
