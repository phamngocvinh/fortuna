// Get all table cells
const cellsS = document.querySelectorAll('#myTableL td')

// Loop through each cell and add click event listener
cellsS.forEach((cell) => {
  cell.addEventListener('click', () => {
    // Toggle highlight on the clicked cell
    cell.classList.toggle('table-warning')
  })
})

const cellsL = document.querySelectorAll('#myTableS td')

// Loop through each cell and add click event listener
cellsL.forEach((cell) => {
  cell.addEventListener('click', () => {
    // Toggle highlight on the clicked cell
    cell.classList.toggle('table-warning')
  })
})

window.onload = function() {
    document.getElementById("myTableS").rows[2].cells[2].classList.add("table-warning");
    document.getElementById("myTableL").rows[2].cells[2].classList.add("table-warning");
};