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
    {% load static %}
    <!DOCTYPE html>
    <html>
    <div class="middleContainerMessage">
        <div class="dot">●</div>
        <div class="middleMessage">
          {{ teacher.bio }}
        </div>
    </div>
    <div class="middleContainerBox">
        {{ teacher.teaching_plan|linebreaksbr }}
    </div>
    <div class="teachingPlanKeyword">
      {% if teacher.is_paid == False %}
        무료 티칭
      {% else %}
        유료 티칭
      {% endif %}
    </div>
      </html>
    `;
    // Add underline to the teaching plan tab
    teachingPlanTab.classList.add("underline");
    teachingPlanTab.classList.remove("no-underline");
  } else if (contentType === "runnerReview") {
    contentBox.innerHTML = `
    <div class="middleContainerMessage">
        <div class="dot"></div>
        <div class="middleMessage">
          {% for review in reviews %}
          <div class="review">
            <div class="reviewHeader">
              <span class="stars">
                {% for i in range(review.rating - 1) %}★{% endfor %}
              </span>
              <span class="divider">|</span>
              <span class="reviewer">{{review.learner.nickname|truncatechars:1}} 러너</span>
            </div>
            <div class="reviewContent">
              {{ review.comment }}
            </div>
          </div>
          {% endfor %}
        </div>
    </div>
      
    `;
    // Add underline to the runner review tab
    runnerReviewTab.classList.add("underline");
    runnerReviewTab.classList.remove("no-underline");
  }
}