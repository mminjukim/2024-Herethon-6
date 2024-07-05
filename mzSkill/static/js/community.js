            // 닫기 버튼 클릭 이벤트
            document.querySelector('.close-popup').addEventListener('click', function() {
                console.log('Close button clicked');
                document.getElementById('category-popup').classList.remove('show');
                setTimeout(function() {
                    document.getElementById('category-popup').style.display = 'none';
}, 300); // 애니메이션 완료 후
});

function handleSortChange(selectElement) {
    var selectedValue = selectElement.value;
    if (selectedValue === "인기순") {
        window.location.href = "popular_posts.html"; // 인기순 링크
    } else if (selectedValue === "추천순") {
        window.location.href = "recommended_posts.html"; // 추천순 링크
    }
}

document.querySelector('.category-button').addEventListener('click', function() {
    document.getElementById('category-popup').style.display = 'flex';
    setTimeout(function() {
        document.getElementById('category-popup').classList.add('show');
    }, 10); //CSS animation
});

document.querySelectorAll('.category-option').forEach(function(button) {
    button.addEventListener('click', function() {
        var selectedCategory = this.getAttribute('data-category');
        document.getElementById('category').value = selectedCategory;
        document.querySelector('.category-button').textContent = selectedCategory;
        document.getElementById('category-popup').classList.remove('show');
        setTimeout(function() {
            document.getElementById('category-popup').style.display = 'none';
        }, 300); // Wait for the animation to finish
    });
});