#!/usr/bin/node
const $ = window.$;
$('div#red_header').click(function () {
  $('div#red_header').css('color', 'red');
});
