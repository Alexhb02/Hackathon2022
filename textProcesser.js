
// only do things in jQuery when everything is loaded
$(document).ready(function(){
   $('#edit-button').addClass("hideMe");

   // define a jQuery function that is the onclick for the submit button
   $.fn.processEntry = function(){
      var summernoteText = " ";
      $('#summernote').summernote('disable'); // disable editing
      var textElements = ".note-editable p, .note-editable blockquote, .note-editable pre, .note-editable h1, .note-editable h2,.note-editable h3, .note-editable h4, .note-editable h5, .note-editable h6";
      summernoteHTML = $(".note-editable").html(); // get the html content from summernote
      summernoteText = $(summernoteHTML).prepend(" ").text(); // add spaces so the text string is formatted correctly
      $('#edit-button').removeClass("hideMe").addClass("showMe"); // show edit button
      console.log(summernoteText); // change this to a function that sends data to server
      }

      $("#edit-button").click(function(){
         $('#summernote').summernote('enable'); // enable editing
      })
});