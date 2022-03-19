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

app.post("/searchtrips/search", function(req, res){
  const { cid, fid} = req.body
  if((cid == "") && (fid != "")){
      pool.query('SELECT * FROM trip WHERE fid = $1',
          [parseInt(fid)], (error, results) => {
              if (error) {
                  res.status(403).send(`Error: ${error}`)
                  return;
              }
              res.render('DynamicFile/TripSearch', {data: results.rows});

          })
  }
  else if((cid != "") && (fid == "")){
      pool.query("SELECT * FROM trip WHERE cid = $1", [parseInt(cid)],(error, results) => {
          if (error) {
              res.status(403).send(`Error: ${error}`)
              return;
          }
          res.render('DynamicFile/TripSearch', {data: results.rows});

      })
  }
  else{
      pool.query("SELECT * FROM trip WHERE cid = $1 AND fid = $2", [parseInt(cid), parseInt(fid)],(error, results) => {
          if (error) {
              res.status(403).send(`Error: ${error}`)
              return;
          }
          res.render('DynamicFile/TripSearch', {data: results.rows});

      })
  }
});
app.listen(port, () => {
  console.log(`Example app listening on port ${port}!`)
});