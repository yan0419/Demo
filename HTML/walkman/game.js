// Game setting
var tempManPos = 0; // Left value
var tempCoinPos = 0;
var gStatus = 0;	// Game status (1 Yes/ 0 No)
var tempScore = 0;

// Timer setting
var seconds = 10;
var timer;

// Control
document.onkeydown = function(pressedKey) {
	switch (pressedKey.keyCode) {
		// Left
		case 37:
			moveManLeft(document.getElementById("walkman"));
			break;
		// Right
		case 39:
			moveManRight(document.getElementById("walkman"));
			break;
		// A
		case 65:
			moveManLeft(document.getElementById("walkman"));
			break;
		// D
		case 68:
			moveManRight(document.getElementById("walkman"));
			break;
	}
}

function counting(){
	if(seconds < 10) {
		document.getElementById("timer").innerHTML = "Timer: "  + seconds;
	} else {
		document.getElementById("timer").innerHTML = "Timer: ERROR";
	}
	
	// End game when time's up
	if (seconds > 0 ) {
		seconds--;
    } else {
		stopTimer();
		endGame();
	}
}

function startCount(){
	timer = window.setInterval(function() {
		counting();
	}, 1000);
}

function stopTimer(){
	 clearInterval(timer);
}

function moveManLeft(){
	if (gStatus == 1) {
		// ele.style.backgroundImage="url(src/img/walkman_left.gif)";
		document.getElementById("walkman").style.backgroundImage="url(src/img/walkman_left.gif)";
		tempManPos = (tempManPos - 10);
		checkManPos();
		// setManLeft(ele, tempManPos);
		setManLeft(tempManPos);
getScore();
	} else {
		// alert('game have not start');
	}
}

function moveManRight(){
	if (gStatus == 1){
		// ele.style.backgroundImage="url(src/img/walkman_right.gif)";
		document.getElementById("walkman").style.backgroundImage="url(src/img/walkman_right.gif)";
		tempManPos = (tempManPos + 10);
		checkManPos();
		// setManLeft(ele, tempManPos);
		setManLeft(tempManPos);
getScore();
	} else {
		// alert('game have not start');
	}
}

function checkManPos(){
	document.getElementById("printPos").textContent = "Position: "  + tempManPos;
	if (tempManPos > 630 || tempManPos < -10){
		endGame();
	}
}

function setManLeft(val) {
	document.getElementById("walkman").style.left = val + "px";
}

function getScore(){
	tempScore++;
	document.getElementById("score").innerHTML = "Score: "  + tempScore;
}

// open an New Broswer with fixed size
function openNewWindow(){
	window.open("walkman.html","Walk","width=720,height=420");
}

// new game && reset game
function startGame(){
	setManLeft(320);
	tempManPos = 320;
	document.getElementById("menu").style.opacity = 0;
	document.getElementById("timer").innerHTML = "Timer: "  + 10;
	document.getElementById("score").innerHTML = "Score: "  + 0;
	seconds = 9;
	tempScore = 0;
	gStatus = 1; //start game
	startCount();
}

function endGame(){
	gStatus = 0;	// end game
	stopTimer();
	document.getElementById("menu").style.opacity = 0.7;
	document.getElementById("playbtn").textContent = "Play Again";
	document.getElementById("playbtn").style.top = 260 + "px";
}
