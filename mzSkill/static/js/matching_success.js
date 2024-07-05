document.addEventListener('DOMContentLoaded', function() {
    let currentCard = 0;
    cards[1].classList.remove('active');
    cards[2].classList.remove('active');
    
    const cards = document.querySelectorAll('.card');
    const arrowContainer = document.querySelector('.arrow-container');
    const dots = document.querySelectorAll('.dot');

    arrowContainer.addEventListener('click', function() {
        cards[currentCard].classList.remove('active');
        dots[currentCard].classList.remove('active');

        currentCard = (currentCard + 1) % cards.length;

        cards[currentCard].classList.add('active');
        dots[currentCard].classList.add('active');
    });
});
