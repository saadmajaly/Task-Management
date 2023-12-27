document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form');
  const usernameInput = document.querySelector('input[name="username"]');
  const emailInput = document.querySelector('input[name="email"]');
  const passwordInput = document.querySelector('input[name="password"]');
  const confirmPasswordInput = document.querySelector('input[name="password_confirmation"]');
  const errorBox = document.getElementById('error-box');

  form.addEventListener('submit', function (event) {
    errorBox.style.display = 'none';
    errorBox.innerHTML = '';

    if (!validateUsername(usernameInput.value)) {
      displayError('Invalid username. Please enter a valid username. (valid username must contain more than 4 characters)');
      event.preventDefault();
    }

    if (!validateEmail(emailInput.value)) {
      displayError('Invalid email address. Please enter a valid email.');
      event.preventDefault();
    }

    if (!validatePassword(passwordInput.value)) {
      displayError('Invalid password. Please enter a password with at least 6 characters.');
      event.preventDefault();
    }

    if (passwordInput.value !== confirmPasswordInput.value) {
      displayError('Password confirmation does not match the password.');
      event.preventDefault();
    }
    if (ermsg.length > 0)
    {
      displayError(ermsg);
      console.log(ermsg);
      event.preventDefault();
      }
  });

  usernameInput.addEventListener('input', function () {
    validateUsername(usernameInput.value);
  });

  emailInput.addEventListener('input', function () {
    validateEmail(emailInput.value);
  });

  passwordInput.addEventListener('input', function () {
    validatePassword(passwordInput.value);
  });

  confirmPasswordInput.addEventListener('input', function () {
    if (passwordInput.value !== confirmPasswordInput.value) {
      displayError('Password confirmation does not match the password.');
    } else {
      clearError();
    }
  });

  function validateUsername(username) {
    const isValid = username.length >= 4;
    if (!isValid) {
      displayError('Invalid username. Please enter a valid username. (valid username must contain more than 4 characters)');
    } else {
      clearError();
    }
    return isValid;
  }

  function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const isValid = emailRegex.test(email);
    if (!isValid) {
      displayError('Invalid email address. Please enter a valid email.');
    } else {
      clearError();
    }
    return isValid;
  }

  function validatePassword(password) {
    const isValid = password.length >= 6;
    if (!isValid) {
      displayError('Invalid password. Please enter a password with at least 6 characters.');
    } else {
      clearError();
    }
    return isValid;
  }

  function displayError(message) {
    errorBox.style.display = 'block';
    errorBox.innerHTML = message;
  }

  function clearError() {
    errorBox.style.display = 'none';
    errorBox.innerHTML = '';
  }
});
