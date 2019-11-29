const textarea = document.getElementById('project_description'),
      allButtons = Array.from(document.querySelectorAll('.plus_str_button'));

allButtons.forEach(item => {
    item.addEventListener('click',() => {
        textarea.value += (String(item.textContent) + " ");
    })
})

