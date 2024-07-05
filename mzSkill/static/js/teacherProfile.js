document.addEventListener("DOMContentLoaded", function () {
  showContent("teachingPlan");
});

function showContent(contentType) {
  const contentBox = document.getElementById("contentBox");
  const teachingPlanTab = document.getElementById("teachingPlan");
  const runnerReviewTab = document.getElementById("runnerReview");

  // Remove underline and reset color for both tabs
  teachingPlanTab.classList.remove("underline");
  teachingPlanTab.classList.add("no-underline");
  runnerReviewTab.classList.remove("underline");
  runnerReviewTab.classList.add("no-underline");

  if (contentType === "teachingPlan") {
    contentBox.innerHTML = `
    <a href="">
    <div class="middleContainerMessage">
        <div class="dot">●</div>
        <div class="middleMessage">
          초보자분들도 쉽게 배울 수 있는 기초 드로잉
        </div>
      </div>
      <div class="middleContainerBox">
        전공자입니다!
        시간 날 때마다 드로잉 피드백 봐 드려요.
        학원에서 어린 학생들 봐 주고 있어서 아마 쉽게 설명해 드릴 수 있을 것 같습니다~!
      </div>
      <div class="teachingPlanKeyword">무료 티칭</div></a>
      
    `;
    // Add underline to the teaching plan tab
    teachingPlanTab.classList.add("underline");
    teachingPlanTab.classList.remove("no-underline");
  } else if (contentType === "runnerReview") {
    contentBox.innerHTML = `
    <a href="">
    <div class="middleContainerMessage">
        <div class="dot"></div>
        <div class="middleMessage">
        <div class="review">
  <div class="reviewHeader">
    <span class="stars">★★★★★</span>
    <span class="divider">|</span>
    <span class="reviewer">한***** 러너</span>
  </div>
  <div class="reviewContent">
    피드백을 꼼꼼하게 해주셔서 너무 좋았어요. 그림을 너무 배우고 싶었는데 덕분에 주변에서도 진짜 많이 늘었다고 칭찬을 많이 받았습니다!
  </div>
</div>
          
        </div>
      </div></a>
      
    `;
    // Add underline to the runner review tab
    runnerReviewTab.classList.add("underline");
    runnerReviewTab.classList.remove("no-underline");
  }
}
