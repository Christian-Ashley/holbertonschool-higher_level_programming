// Include the jQuery library (make sure to adjust the path to your jQuery file)
// <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

// Wait for the document to be ready
$(document).ready(function() {
  // select the correct div with jQuery
  var redHeaderDiv = $("#red_header");
  
  // attach a click event handler
  redHeaderDiv.click(function() {
    // select the header with jQuery
    var headerElement = $("header");

    // add the class 'red' to header element
    headerElement.addClass("red");
  })
})