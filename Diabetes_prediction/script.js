document.getElementById('diabetes-form').addEventListener('submit', function(e) {
  e.preventDefault();
  
  const inputData = [
      parseFloat(document.getElementById('pregnancies').value),
      parseFloat(document.getElementById('glucose').value),
      parseFloat(document.getElementById('blood-pressure').value),
      parseFloat(document.getElementById('skin-thickness').value),
      parseFloat(document.getElementById('insulin').value),
      parseFloat(document.getElementById('bmi').value),
      parseFloat(document.getElementById('dpf').value),
      parseFloat(document.getElementById('age').value)
  ];
  
  fetch('/predict', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ input: inputData })
  })
  .then(response => response.json())
  .then(data => {
      document.getElementById('result').innerHTML = `The patient is ${data.result}`;
  })
  .catch(error => {
      console.error('Error:', error);
  });
});
