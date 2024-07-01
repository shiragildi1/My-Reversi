document.addEventListener("DOMContentLoaded", (event) => {
  console.log("DOM fully loaded and parsed");
  document.getElementById("start-game").addEventListener("click", startGame);
});

function startGame() {
  console.log("Start game button clicked");
  fetch("/start_game")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("board").style.display = "block";
      renderBoard(data.board, data.player);
    })
    .catch((error) => console.error("Error:", error));
}

function renderBoard(board, player) {
  const gameBoard = document.getElementById("game-board");
  gameBoard.innerHTML = "";

  for (let row = 0; row < board.length; row++) {
    const tr = document.createElement("tr");
    for (let col = 0; col < board[row].length; col++) {
      const td = document.createElement("td");
      td.dataset.row = row;
      td.dataset.col = col;
      td.textContent =
        board[row][col] === 1 ? "R" : board[row][col] === 2 ? "B" : "";
      td.style.backgroundColor =
        board[row][col] === 1
          ? "red"
          : board[row][col] === 2
          ? "black"
          : "green";
      td.addEventListener("click", () => makeMove(row, col, player));
      tr.appendChild(td);
    }
    gameBoard.appendChild(tr);
  }
}

function makeMove(row, col, player) {
  fetch("/make_move", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      board: Array.from(document.querySelectorAll("#game-board tr")).map((tr) =>
        Array.from(tr.children).map((td) =>
          td.textContent === "R" ? 1 : td.textContent === "B" ? 2 : 0
        )
      ),
      row: row,
      col: col,
      player: player,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.valid) {
        renderBoard(data.board, data.player);
      } else {
        alert("Invalid move!");
      }
    })
    .catch((error) => console.error("Error:", error));
}
