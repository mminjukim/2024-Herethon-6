document.getElementById('teacher').addEventListener('click', function() {
    selectOption('teacher');
});

document.getElementById('runner').addEventListener('click', function() {
    selectOption('runner');
});

function selectOption(option) {
    document.getElementById('teacher').classList.remove('selected');
    document.getElementById('runner').classList.remove('selected');
    
    document.getElementById(option).classList.add('selected');
}

function nextPage() {
    const selectedOption = document.querySelector('.option.selected');
    if (selectedOption) {
        alert('Next page logic here for: ' + selectedOption.id);
        // Implement next page logic here
    } else {
        alert('Please select an option first.');
    }
}