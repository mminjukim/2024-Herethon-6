document.addEventListener('DOMContentLoaded', function() {
    const skills = document.querySelectorAll('.skill .checkbox');

    skills.forEach(skill => {
        skill.addEventListener('change', () => {
            const label = skill.nextElementSibling;
            if (skill.checked) {
                label.classList.add('active');
            } else {
                label.classList.remove('active');
            }
        });
    });
});
