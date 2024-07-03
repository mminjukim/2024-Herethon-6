document.addEventListener('DOMContentLoaded', function() {
    const skills = document.querySelectorAll('.skill');
    const options = document.querySelectorAll('.option .checkbox');

    skills.forEach(skill => {
        skill.addEventListener('click', () => {
            const subSkills = skill.querySelector('.sub-skills');
            subSkills.style.display = subSkills.style.display === 'flex' ? 'none' : 'flex';
            skill.classList.toggle('active');
        });
    });

    options.forEach(option => {
        option.addEventListener('change', () => {
            const section = option.closest('.section');
            if (section.querySelector('.checkbox:checked')) {
                section.classList.add('active');
            } else {
                section.classList.remove('active');
            }
        });
    });
});
