document.addEventListener("DOMContentLoaded", function () {
  const images = document.querySelectorAll(".starImage");
  let currentIndex = 0;

  images.forEach((img, index) => {
    img.addEventListener("click", function () {
      if (index === currentIndex) {
        const originalSrc = "../images/review/Star 5.png";
        const alternateSrc = "../images/review/Star 5 (1).png";

        this.src = this.src.includes("(1)") ? originalSrc : alternateSrc;

        currentIndex = (currentIndex + 1) % images.length;
      }
    });
  });
});
