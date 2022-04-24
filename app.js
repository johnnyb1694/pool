// Load libraries
const express = require('express');
const path = require('path');
const ejs = require('ejs');

// Instantiate our application
const app = express();
const PORT = 3000;

// Assign the pure alias 'views' to the actual file path leading to the views subdirectory 
// NB: optional as express searches CWD/views anyway!
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// Make static files (e.g. CSS stylesheets) available to the express application
app.use(express.static('public'));

app.get('/', (req, res) => {
    res.render('index');
});

app.get('/submit', (req, res) => {
    res.render('submit');
});

app.listen(PORT, () => {
    console.log(`Application listening on port ${PORT}!`);
});
