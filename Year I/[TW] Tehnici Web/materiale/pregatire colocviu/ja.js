<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buton Example</title>
    <style>
        .buton {
            width: 100px;
            height: 40px;
            border-radius: 10px;
            margin: 5px;
        }
        .par {
            background-color: green;
            color: white;
        }
        .impar {
            background-color: yellow;
            color: black;
        }
    </style>
</head>
<body>
    <div id="buttonContainer"></div>

    <script>
        window.onload = function() {
            const buttonContainer = document.getElementById('buttonContainer');

            for (let i = 1; i <= 6; i++) {
                const button = document.createElement('button');
                button.classList.add('buton');
                button.textContent = `Buton ${i}`;

                if (i % 2 === 0) {
                    button.classList.add('par');
                } else {
                    button.classList.add('impar');
                }

                button.addEventListener('click', function() {
                    button.style.backgroundColor = 'red';
                });

                buttonContainer.appendChild(button);
            }
        };
    </script>
</body>
</html>
