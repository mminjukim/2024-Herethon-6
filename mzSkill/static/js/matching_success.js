document.querySelector('.match-button').addEventListener('click', function() {
    alert('1:1 매칭 신청이 완료되었습니다!');
    // Implement additional logic here if necessary
});

document.querySelectorAll('.nav-btn').forEach(button => {
    button.addEventListener('click', function() {
        alert(button.textContent + ' 클릭됨');
        // Implement navigation logic here
    });
});
