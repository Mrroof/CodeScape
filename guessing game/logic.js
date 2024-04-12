// Generate a random number between 1 and 100
const randomNumber = Math.floor(Math.random() * 100) + 1;

// Get references to the input field and message area
const guessInput = document.getElementById('guessInput');
const message = document.getElementById('message');

// Function to check the user's guess
function checkGuess() {
  // Get the user's guess
  const userGuess = parseInt(guessInput.value);

  // Check if the guess is correct
  if (userGuess === randomNumber) {
    message.textContent = 'Congratulations! You guessed the correct number!';
    message.style.color = 'green';
    guessInput.disabled = true;
  } else if (userGuess < randomNumber) {
    message.textContent = 'Too low! Try a higher number.';
    message.style.color = 'red';
  } else {
    message.textContent = 'Too high! Try a lower number.';
    message.style.color = 'red';
  }
}

// Function to reset the game
function resetGame() {
  // Generate a new random number
  randomNumber = Math.floor(Math.random() * 100) + 1;

  // Reset input field and message area
  guessInput.value = '';
  message.textContent = '';
  message.style.color = 'black';
  guessInput.disabled = false;
}