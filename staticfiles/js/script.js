document.addEventListener("DOMContentLoaded", () => {
    const sidebarToggle = document.getElementById("sidebarToggle");
    const sidebar = document.getElementById("sidebar");
    const closeSidebar = document.getElementById("closeSidebar");
    const mainContent = document.getElementById("mainContent");
  
    sidebarToggle.addEventListener("click", () => {
      sidebar.style.width = "250px";
      mainContent.style.marginLeft = "250px";
    });
  
    closeSidebar.addEventListener("click", () => {
      sidebar.style.width = "0";
      mainContent.style.marginLeft = "0";
    });
  });
  //
  //
  