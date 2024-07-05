document.querySelectorAll(".catagory").forEach((div) => {
  const checkbox = div.querySelector(".checkbox");
  checkbox.addEventListener("change", function () {
    div.classList.toggle("checked", this.checked);
  });

  div.addEventListener("click", function (event) {
    if (event.target.tagName !== "INPUT" && event.target.tagName !== "LABEL") {
      checkbox.checked = !checkbox.checked;
      checkbox.dispatchEvent(new Event("change"));
    }
  });
});
