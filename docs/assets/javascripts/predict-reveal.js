// Widget "Dự đoán trước, chạy sau" (quy tắc ①). Ô .predict-result ẩn tới khi gõ dự đoán >= 25 ký tự.
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".predict").forEach(function (box, i) {
    var input = box.querySelector(".predict-input");
    var btn = box.querySelector(".predict-btn");
    var result = box.querySelector(".predict-result");
    if (!input || !btn || !result) return;
    var key = "predict:" + window.location.pathname + ":" + i;
    var MIN = 25;
    function reveal() {
      input.setAttribute("disabled", "disabled");
      btn.setAttribute("disabled", "disabled");
      btn.textContent = "Đã khoá — đối chiếu bên dưới";
      result.hidden = false;
      box.classList.add("revealed");
    }
    var saved = null;
    try { saved = window.localStorage.getItem(key); } catch (e) {}
    if (saved) { input.value = saved; reveal(); }
    input.addEventListener("input", function () {
      btn.disabled = input.value.trim().length < MIN;
    });
    btn.disabled = true;
    btn.addEventListener("click", function () {
      if (input.value.trim().length < MIN) return;
      try { window.localStorage.setItem(key, input.value.trim()); } catch (e) {}
      reveal();
    });
  });
});
