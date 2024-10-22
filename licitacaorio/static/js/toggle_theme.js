function toggleTheme() {
  const html = document.documentElement;
  const currentTheme = html.getAttribute("data-theme") || "light";
  const newTheme = currentTheme === "light" ? "dark" : "light";

  html.setAttribute("data-theme", newTheme);
  localStorage.setItem("theme", newTheme);

  document
    .querySelectorAll("img[data-icon-light][data-icon-dark]")
    .forEach((img) => {
      const newSrc = img.getAttribute(`data-icon-${newTheme}`);
      console.log("Switching image:", img.alt, "to", newSrc);

      // Create a new Image object to check if the file exists
      const testImage = new Image();
      testImage.onload = function () {
        img.src = newSrc;
      };
      testImage.onerror = function () {
        console.error("Error loading image:", newSrc);
        // Optionally, set a fallback image or keep the current one
        // img.src = 'path/to/fallback/image.png';
      };
      testImage.src = newSrc;
    });
}

document.addEventListener("DOMContentLoaded", () => {
  const savedTheme = localStorage.getItem("theme") || "light";
  document.documentElement.setAttribute("data-theme", savedTheme);

  document
    .querySelectorAll("img[data-icon-light][data-icon-dark]")
    .forEach((img) => {
      const currentSrc = img.getAttribute(`data-icon-${savedTheme}`);
      console.log("Setting initial image:", img.alt, "to", currentSrc);
      img.src = currentSrc;
    });
});
