#!/usr/bin/node
const $ = window.$;
$('div#update_header').click(function () {
  $('header').html('New Header!!!');
});
