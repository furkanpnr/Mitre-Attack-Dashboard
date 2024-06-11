document.querySelector(".jsFilter").addEventListener("click", function () {
    document.querySelector(".filter-menu").classList.toggle("active");
});
  
document.querySelector(".grid").addEventListener("click", function () {
    document.querySelector(".list").classList.remove("active");
    document.querySelector(".grid").classList.add("active");
    document.querySelector(".products-area-wrapper").classList.add("gridView");
    document.querySelector(".products-area-wrapper").classList.remove("tableView");
});
  
document.querySelector(".list").addEventListener("click", function () {
    document.querySelector(".list").classList.add("active");
    document.querySelector(".grid").classList.remove("active");
    document.querySelector(".products-area-wrapper").classList.remove("gridView");
    document.querySelector(".products-area-wrapper").classList.add("tableView");
});


// Get the filter elements
const filterMenu = document.querySelector(".filter-menu");
const filterCategory = filterMenu.querySelector("select:nth-of-type(1)");
const filterStatus = filterMenu.querySelector("select:nth-of-type(2)");
const applyButton = document.getElementById("apply-btn");
const resetButton = document.getElementById("reset-btn");

// Apply filter
applyButton.addEventListener("click", function () {
    console.log("apply click")
    applyFilters();
});

// Reset filter
resetButton.addEventListener("click", function () {
    console.log("reset click")
    resetFilters();
});


// Apply filter logic
function applyFilters() {
    const selectedCategory = filterCategory.value.trim();
    const selectedStatus = filterStatus.value.trim();
    const productArea = document.querySelector('.products-area-wrapper');
    const products = productArea.querySelectorAll('.products-row');


    products.forEach(product => {
        const productCategory = product.querySelector(".product-cell.category").textContent.trim();
        const productStatus = product.querySelector(".product-cell.status-cell").textContent.trim();
        
        const categoryValue = productCategory.split(":")[1].trim();
        const statusValue = productStatus.split(":")[1].trim();
        
        let categoryMatch = selectedCategory === "All Types" || categoryValue === selectedCategory;
        let statusMatch = selectedStatus === "All Status" || statusValue === selectedStatus;

        if (categoryMatch && statusMatch) {
            product.style.display = "";
        } else {
            product.style.display = "none";
        }
    });
}

// Reset filter logic
function resetFilters() {
    filterCategory.value = "All Types";
    filterStatus.value = "All Status";
    applyFilters();
}