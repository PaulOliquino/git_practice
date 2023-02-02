const squares = document.querySelectorAll(".square");
const board = document.getElementById("board");
const startBtn = document.getElementById("startBtn");
let turn = "X";

for (const square of squares) {
  square.addEventListener("click", handleClick);
}

startBtn.addEventListener("click", startGame);

function handleClick() {
  if (this.innerHTML !== "") return;
  this.innerHTML = turn;
  if (checkWin(turn)) {
    alert(`${turn} wins!`);
    startGame();
  } else if (checkDraw()) {
    alert("Draw!");
    startGame();
  } else {
    turn = turn === "X" ? "O" : "X";
  }
}

function checkWin(player) {
  for (let i = 0; i < 9; i += 3) {
    if (
      squares[i].innerHTML === player &&
      squares[i + 1].innerHTML === player &&
      squares[i + 2].innerHTML === player
    )
      return true;
  }
  for (let i = 0; i < 3; i++) {
    if (
      squares[i].innerHTML === player &&
      squares[i + 3].innerHTML === player &&
      squares[i + 6].innerHTML === player
    )
      return true;
  }
  if (
    squares[0].innerHTML === player &&
    squares[4].innerHTML === player &&
    squares[8].innerHTML === player
  )
    return true;
  if (
    squares[2].innerHTML === player &&
    squares[4].innerHTML === player &&
    squares[6].innerHTML === player
  )
    return true;
  return false;
}

function checkDraw() {
  for (const square of squares) {
    if (square.innerHTML === "") return false;
  }
  return true;
}

function startGame() {
  for (const square of squares) {
    square.innerHTML = "";
  }
  turn = "X";
}
