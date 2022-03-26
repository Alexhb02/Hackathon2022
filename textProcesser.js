function processEntry(){
   $('#summernote').summernote('disable'); // disable editing
  var summernoteText= $(".note-editable p").prepend(" ").text(); // add spaces
   //var summernoteText = $('.note-editable').text(); // get text
    console.log(summernoteText);
};