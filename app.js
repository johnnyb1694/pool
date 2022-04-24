const express = require("express");

const app = express();
const PORT = 3000;

app.get("/", (req, res) => {
    res.send("<h1>Received!</h1>");
});

app.listen(PORT, () => {
    console.log(`Application listening on port ${PORT}!`);
});
