#!/usr/bin/node
const $ = window.$;
$('div#red_header').click(function () {
  $('header').css('color', 'red');
});
