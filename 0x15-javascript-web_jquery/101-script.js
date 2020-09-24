#!/usr/bin/node
const $ = window.$;
$(document).ready(function () {
  $('div#add_item').click(function () {
    $('<li>Item</li>').appendTo('ul.my_list');
  });
  $('div#remove_item').click(function () {
    $('li').last().remove();
  });
  $('div#clear_list').click(function () {
    $('li').remove();
  });
});
