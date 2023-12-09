// Get all table cells
const cells = document.querySelectorAll('#myTable td')

// Loop through each cell and add click event listener
cells.forEach((cell) => {
  cell.addEventListener('click', () => {
    // Toggle highlight on the clicked cell
    cell.classList.toggle('table-warning')
  })
})