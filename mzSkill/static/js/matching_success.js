document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.card');
    const arrowContainer = document.querySelector('.arrow-container');
    const dots = document.querySelectorAll('.dot');
    let currentCard = 0;

    arrowContainer.addEventListener('click', function() {
        cards[currentCard].classList.remove('active');
        dots[currentCard].classList.remove('active');

        currentCard = (currentCard + 1) % cards.length;

        cards[currentCard].classList.add('active');
        dots[currentCard].classList.add('active');
    });
});
