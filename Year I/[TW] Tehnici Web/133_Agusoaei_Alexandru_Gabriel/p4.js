var express =require("express");

var fs = require("fs");
const { parse } = require("path");

var app = express(); 

app.use(express.static("html"));


app.listen(3000, function()
{
    console.log("Serverul a pornit");
}
);




