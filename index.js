const mysql = require('mysql');
require('dotenv').config();
pool = mysql.createPool({
  connectionLimit: 100,
  host: 'database-3.cwklamgalmge.us-east-2.rds.amazonaws.com',
  user: 'admin',
  password: 'Hack2022',
  database: 'sys'
});
let ejs = require('ejs');
const bodyparser = require('body-parser')
const express = require("express")
const path = require('path')
const router = express.Router()
const app = express()
app.use(express.static(__dirname + "/public"))
var PORT = 3306

app.get('/', (req, res) => {
  res.send('Hello World!')
});

app.post("/login", function(req, res){
  const { email, password} = req.body
  pool.query("SELECT user_id, user_firstname FROM users WHERE email = ? AND password = ?", [email, password],(error, results) => {
      if (error) {
          res.status(403).send(`Error: ${error}`)
          return;
      }
      res.render('index', {data: results.rows});

  })
});

app.post("/signup", function(req, res){
  const { firstname, lastname, email, password} = req.body
  pool.query("INSERT INTO users (user_firstname, user_lastname, user_email, password) VALUES (?, ?, ?, ?, ?, ?);", [firstname, lastname, email, password],(error, results) => {
      if (error) {
          res.status(403).send(`Error: ${error}`)
          return;
      }
      res.render('index', {data: results.rows});

  })
});

app.post("/journalEntry", function(req, res){
  const { email, password} = req.body
  pool.query("SELECT user_id, user_firstname FROM users WHERE email = ? AND password = ?", [email, password],(error, results) => {
      if (error) {
          res.status(403).send(`Error: ${error}`)
          return;
      }
      res.render('login', {data: results.rows});
  })
});

app.post("/journal", function(req, res){
  const { text, user_id} = req.body
  //insert spawn code
  pool.query("SELECT user_firstname FROM users WHERE user_email = $1 AND password = $2", [email, password],(error, results) => {
      if (error) {
          res.status(403).send(`Error: ${error}`)
          return;
      }
      console.log(results)
      //res.render('DynamicFile/TripSearch', {data: results.rows});

  })
});

app.listen(PORT, () => {
  console.log(`Example app listening on port ${PORT}!`)
    //res.render('DynamicFile/TripSearch', {data: results.rows});
});
