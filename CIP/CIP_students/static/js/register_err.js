const alert = document.querySelectorAll('.alert-danger'),
      inputs = document.querySelectorAll('.form-control');

inputs.forEach(item => {
    item.addEventListener('input',() =>{
        alert.forEach(item =>{
          item.style.display = 'none';
        })
    });
});