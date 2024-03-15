<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Client</title>
</head>
<body>
    <label for="number">Enter a number:</label>
    <input type="number" id="number">
    <button onclick="sendNumber()">Send</button>
    <p id="result"></p>

    <script>
        function sendNumber() {
            var number = document.getElementById('number').value;
            // Replace 'htt/sum' with the actual URL of your server endpoint
            fetch('https://flwebapp11.azurewebsites.net/sum', { // Replace with the actual URL
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ numbers: [parseInt(number)] })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('result').innerText = 'Sum: ' + data.sum;
            });
        }
    </script>
</body>
</html>
