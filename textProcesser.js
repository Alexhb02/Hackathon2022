const express = require("express");
const { spawn } = require('child_process');
const app = express();
const port = 8812;

(function processEntry($){
    var summernoteText = $('.note-editable').text(); //get just the text
    console.log(summernoteText);
})(jQuery);

app.get('/semantics.py', (req, res) => {
    var data1;
   // spawn new child process to call the python script
   const python = spawn('python3', ['semantics.py', ]);
   // collect data from script
   python.stdout.on('data', function (data) {
      console.log('Pipe data from python script ...');
      data1 = data.toString();
   });
   // in close event we are sure that stream from child process is closed
   python.on('close', (code) => {
      console.log(`child process close all stdio with code ${code}`);
      // send data to browser
      res.send(data1)
   });
})

app.get('/script2/:fname/:lname', (req, res) => {
    var data2;
    // spawn new child process to call the python script
    const python = spawn('python3', ['script2.py', req.params.fname, req.params.lname]);
    // collect data from script
    python.stdout.on('data', function (data) {
       console.log('Pipe data from python script ...');
       data2 = data.toString();
    });
   // in close event we are sure that stream from child process is closed
   python.on('close', (code) => {
      console.log(`child process close all stdio with code ${code}`);
      // send data to browser
      res.send(data2)
   });
})
app.listen(port, () => console.log(`node python script app listening on port ${port}!`))