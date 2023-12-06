#!/usr/bin/node
// JavaScript  that toggles the <header> element's class
$("DIV#toggle_header").click(function() {
  $("header").toggleClass("red green");
});
