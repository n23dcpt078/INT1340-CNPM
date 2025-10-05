document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault(); // Ngăn reload trang khi submit

  let username = document.getElementById("username").value.trim();
  let password = document.getElementById("password").value.trim();

  if (username === "" || password === "") {
    alert("Vui lòng nhập đầy đủ Username và Password!");
  } else if (password.length < 6) {
    alert("Password phải có ít nhất 6 ký tự!");
  } else {
    alert("Đăng nhập thành công!");
  }
});

function cancelForm() {
  document.getElementById("loginForm").reset();
}
