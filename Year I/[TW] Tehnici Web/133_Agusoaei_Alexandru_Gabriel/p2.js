document.addEventListener("DOMContentLoaded", function(){
    
            for (let i = 1; i <= 6; i++) {
                let button = document.createElement('button');
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

                document.body.appendChild(button);
            }
});

