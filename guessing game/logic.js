


JavaScript
const guessInput = document.getElementById('guess');
const submitButton = document.getElementById('submit-guess');
const message = document.getElementById('message');

// Generate a random number between 1 and 100
let randomNumber = Math.floor(Math.random() * 100) + 1;

submitButton.addEventListener('click', function() {
  const guess = parseInt(guessInput.value);

  // Check if input is valid (number between 1 and 100)
  if (isNaN(guess) || guess < 1 || guess > 100) {
    message.textContent = "Please enter a valid number between 1 and 100.";
    return; // Exit the function if input is invalid
  }

  // Check guess
  if (guess === randomNumber) {
    message.textContent = "Congrats! You guessed the number!";
    submitButton.disabled = true; // Disable button after correct guess
  } else if (guess > randomNumber) {
    message.textContent = "Too high! Try again.";
  } else {
    message.textContent = "Too low! Try again.";
  }
});