function processEntry(){
   $('#summernote').summernote('disable'); // disable editing
  var summernoteText= $(".note-editable p").prepend(" ").text(); // add spaces
    console.log(summernoteText);
};