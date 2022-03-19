const { Pool} = require('pg')
require('dotenv').config();
const connectionString = process.env.CONNECTION_STRING
const pool = new Pool({
    connectionString,
})
let ejs = require('ejs');
const bodyparser = require('body-parser')
const express = require("express")
const path = require('path')
const router = express.Router()
const app = express()
app.use(express.static(__dirname + "/public"))
var PORT = process.env.PORT || 3306

app.get('/', (req, res) => {
  res.send('Hello World!')
});

app.post("/login", function(req, res){
  const { email, password} = req.body
  pool.query("SELECT user_firstname FROM users WHERE email = $1 AND password = $2", [email, password],(error, results) => {
      if (error) {
          res.status(403).send(`Error: ${error}`)
          return;
      }
      res.send('This worked ${results.rows}')
      //res.render('DynamicFile/TripSearch', {data: results.rows});

  })
});

app.post("/journal", function(req, res){
  const { text, user_id} = req.body
  //insert spawn code
  pool.query("SELECT user_firstname FROM users WHERE email = $1 AND password = $2", [email, password],(error, results) => {
      if (error) {
          res.status(403).send(`Error: ${error}`)
          return;
      }
      res.send('This worked ${results.rows}')
      //res.render('DynamicFile/TripSearch', {data: results.rows});

  })
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}!`)
});


(function($){
  var summernoteText = $('.note-editable').text(); //get just the text
  console.log(summernoteText);
})(jQuery);