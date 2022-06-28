let partBtn = document.getElementById('part_btn');
let autoBtn = document.getElementById('auto_btn');
let labelOwnName = document.getElementById('own_name_label');
let fieldOwnNumber = document.getElementById('number_field');
let ownNameErr = document.getElementById('ownNameErr');
let ownNumberErr = document.getElementById('ownNumberErr');
let ownCommentErr = document.getElementById('ownCommentErr');


if (partBtn.checked === true) {
    labelOwnName.innerHTML = 'Название запчасти: <span class="text-danger">*</span>'
    fieldOwnNumber.classList.add('d-none');
}
else {
    labelOwnName.innerHTML = 'Модель автомобиля: <span class="text-danger">*</span>'
    fieldOwnNumber.classList.remove('d-none');
}


partBtn.addEventListener('click', (e) => {
    partBtn.checked = true;
    autoBtn.checked = false;

    labelOwnName.innerHTML = 'Название запчасти: <span class="text-danger">*</span>'
    fieldOwnNumber.classList.add('d-none');

    ownNameErr.innerText = "";
    ownNumberErr.innerText = "";
    ownCommentErr.innerText = "";
})


autoBtn.addEventListener('click', (e) => {
    autoBtn.checked = true;
    partBtn.checked = false;

    labelOwnName.innerHTML = 'Модель автомобиля: <span class="text-danger">*</span>'
    fieldOwnNumber.classList.remove('d-none');

    ownNameErr.innerText = "";
    ownNumberErr.innerText = "";
    ownCommentErr.innerText = "";
})
