let keyPreseed = false;
let intervalId;

        document.addEventListener('keydown', function(event) {
            if (event.key === 'a' && !keyPreseed) {
                keyPreseed = true;
                
                
                const infoParagraph = document.getElementById('info');
                const currentDate = new Date();
                infoParagraph.textContent += ` Data și ora curentă: ${currentDate.toLocaleString()}`;

                
                intervalId = setInterval(() => {
                    const randomFontSize = Math.floor(Math.random() * 21) + 10; 
                    infoParagraph.style.fontSize = `${randomFontSize}px`;
                }, 3000);
            }
        });