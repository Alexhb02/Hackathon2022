const mysql = require('mysql');
require('dotenv').config();
pool = mysql.createPool({
  connectionLimit: 100,
  host: 'database-3.cwklamgalmge.us-east-2.rds.amazonaws.com',
  user: 'admin',
  password: 'Hack2022',
  database: 'sys'
});

const express = require("express")
const router = express.Router()
const app = express()

const path = require('path');
const { Server } = require('http');

var PORT = 4000

let ejs = require('ejs');
app.set("views", path.join(__dirname))
app.set("view engine", "ejs")
const bodyparser = require('body-parser')
//app.engine('html', require('ejs').renderFile)
// Body-parser middleware
app.use(bodyparser.urlencoded({ extended: false }))
app.use(bodyparser.json())
const cors = require('cors');
app.use(cors({ methods: ['GET', 'POST', 'DELETE', 'UPDATE', 'PUT', 'PATCH'] }));
app.use(express.static(__dirname + "/public"))
app.get('/', (req, res) => {
  res.send('Hello World!')
});

app.post("/login", function (req, res) {
  const { email, password } = req.body
  pool.query("SELECT user_id, user_firstname FROM users WHERE email = ? AND password = ?", [email, password], (error, results) => {
    if (error) {
      res.status(403).send(`Error: ${error}`)
      return;
    }
    res.render('index', { data: results.rows });

  })
});

app.get("/signup", function (req, res) {
  res.status(201).send(`Hello`)
  return;
});

app.post("/signup", cors(), function (req, res) {
  const { firstname, lastname, email, password } = req.body
  pool.query("INSERT INTO users (user_firstname, user_lastname, user_email, password) VALUES (?, ?, ?, ?, ?, ?);", [firstname, lastname, email, password], (error, results) => {
    if (error) {
      res.status(403).send(`Error: ${error}`)
      return;
    }
    res.status(201).send(`Success`)
    return;
    res.render('index', { data: results.rows });

  })
});

app.post("/journalEntry", function (req, res) {
  const { email, password } = req.body
  pool.query("SELECT user_id, user_firstname FROM users WHERE email = ? AND password = ?", [email, password], (error, results) => {
    if (error) {
      res.status(403).send(`Error: ${error}`)
      return;
    }
    res.render('login', { data: results.rows });
  })
});

app.post("/journal", function (req, res) {
  const { text, user_id } = req.body
  //insert spawn code
  pool.query("SELECT user_firstname FROM users WHERE user_email = $1 AND password = $2", [email, password], (error, results) => {
    if (error) {
      res.status(403).send(`Error: ${error}`)
      return;
    }
    console.log(results)
    //res.render('DynamicFile/TripSearch', {data: results.rows});

  })
});

app.listen(PORT, () => {
  console.log(`Hackathon Project listening on port ${PORT}!`)
  //res.render('DynamicFile/TripSearch', {data: results.rows});
});
