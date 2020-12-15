const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

window.setTimeout(function() {
    $(".alert").fadeTo(500, 0)
}, 3000);

window.setTimeout(function() {
    $(".alert-success").fadeTo(500, 0)
}, 3000);


