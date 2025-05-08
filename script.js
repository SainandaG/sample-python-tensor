document.getElementById("tensorForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form reload
  
    // Get user input and split into numbers
    const inputStr = document.getElementById("numbers").value;
    const numArray = inputStr.split(',').map(Number).filter(n => !isNaN(n));
  
    if (numArray.length === 0) {
      document.getElementById("output").textContent = "Please enter valid numbers.";
      return;
    }
  
    // Create tensor from array
    const inputTensor = tf.tensor(numArray);
    const squaredTensor = inputTensor.square();
  
    // Show output
    squaredTensor.array().then(result => {
      document.getElementById("output").textContent = "Squared values: " + result.join(', ');
    });
  });
  