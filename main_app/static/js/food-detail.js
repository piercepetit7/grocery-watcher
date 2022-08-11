const dateInput = document.getElementById('initial-id_expiration')

const picker = MCDatepicker.create({
  el: '#initial-id_expiration',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date()
})

dateInput.addEventListener("clicks", (evt) => {
  picker.open()
})