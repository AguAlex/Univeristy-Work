const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;


app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/main.html');
});


app.post('/submit', (req, res) => {
    const nume = req.body.nume;
    res.send(`Salut, ${nume}!`);
});


app.use((req, res, next) => {
    res.status(404).send('Eroare 404: Pagina nu a fost găsită!');
});

app.listen(port, () => {
    console.log(`Serverul rulează la adresa http://localhost:${port}`);
});
