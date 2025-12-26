var n = 9;
var ans = [0, 0, 0];
var end = false;

// HTML요소
var input1, input2, input3;
var attemptsEl, resultsEl, resultImgEl, submitBtn;


function makeans() {
  var a = Math.floor(Math.random() * 10);
  var b = Math.floor(Math.random() * 10);
  var c = Math.floor(Math.random() * 10);

  while (b === a) {
    b = Math.floor(Math.random() * 10);
  }

  while (c === a || c === b) {
    c = Math.floor(Math.random() * 10);
  }

  ans[0] = a;
  ans[1] = b;
  ans[2] = c;
}

function resetinput() {
  input1.value = "";
  input2.value = "";
  input3.value = "";
  input1.focus();
}

function add(tmp1, tmp2, tmp3, strike, ball) {
  var row = document.createElement("div");
  row.className = "check-result";

  var left = document.createElement("div");
  left.className = "left";

  var s1 = document.createElement("span");
  s1.className = "num-result";
  s1.textContent = String(tmp1);

  var s2 = document.createElement("span");
  s2.className = "num-result";
  s2.textContent = String(tmp2);

  var s3 = document.createElement("span");
  s3.className = "num-result";
  s3.textContent = String(tmp3);

  left.appendChild(s1);
  left.appendChild(s2);
  left.appendChild(s3);

  var right = document.createElement("div");
  right.className = "right";

  if (strike === 0 && ball === 0) {
    var outSpan = document.createElement("span");
    outSpan.className = "num-result out";
    outSpan.textContent = "O";
    right.appendChild(outSpan);
  } else {
    var st = document.createElement("span");
    st.className = "num-result strike";
    st.textContent = String(strike) + "S";

    var bl = document.createElement("span");
    bl.className = "num-result ball";
    bl.textContent = String(ball) + "B";

    right.appendChild(st);
    right.appendChild(document.createTextNode(" "));
    right.appendChild(bl);
  }

  row.appendChild(left);
  row.appendChild(right);

  // 최신결과 위로오게
  resultsEl.prepend(row);
}

//리셋
function reset() {
  n = 9;
  end = false;

  makeans();

  resultsEl.innerHTML = "";
  resetinput();

  attemptsEl.textContent = String(n);
  resultImgEl.src = "";

  submitBtn.disabled = false;
  submitBtn.style.opacity = "1";
  submitBtn.style.cursor = "pointer";
}

function check_numbers() {
  if (end === true) {
    return;
  }

  var n1 = input1.value.trim();
  var n2 = input2.value.trim();
  var n3 = input3.value.trim();

  if (n1 === "" || n2 === "" || n3 === "") {
    resetinput();
    return;
  }

  var tmp1 = Number(n1);
  var tmp2 = Number(n2);
  var tmp3 = Number(n3);

  n -= 1;
  attemptsEl.textContent = String(n);

  var strike = 0;
  var ball = 0;
  var tmp = [tmp1, tmp2, tmp3];

  //스트라이크
  for (var i = 0; i < 3; i += 1) {
    if (tmp[i] === ans[i]) {
      strike = strike + 1;
    }
  }

  //볼
  for (var j = 0; j < 3; j += 1) {
    if (tmp[j] === ans[j]) {
      continue;
    }
    if (tmp[j] === ans[0] || tmp[j] === ans[1] || tmp[j] === ans[2]) {
      ball = ball + 1;
    }
  }

  add(tmp1, tmp2, tmp3, strike, ball);

  // 승리
  if (strike === 3) {
    resultImgEl.src = "success.png";
    end = true;

    submitBtn.disabled = true;
    submitBtn.style.opacity = "0.5";
    submitBtn.style.cursor = "not-allowed";

    resetinput();
    return;
  }

  //패배
  if (n <= 0) {
    resultImgEl.src = "fail.png";
    end = true;

    submitBtn.disabled = true;
    submitBtn.style.opacity = "0.5";
    submitBtn.style.cursor = "not-allowed";

    resetinput();
    return;
  }

  resetinput();
}

// 요소연결+게임시ㅈ작
document.addEventListener("DOMContentLoaded", function () {
  input1 = document.getElementById("number1");
  input2 = document.getElementById("number2");
  input3 = document.getElementById("number3");

  attemptsEl = document.getElementById("attempts");
  resultsEl = document.getElementById("results");
  resultImgEl = document.getElementById("game-result-img");

  submitBtn = document.querySelector(".submit-button");

  reset();
});


window.check_numbers = check_numbers;
