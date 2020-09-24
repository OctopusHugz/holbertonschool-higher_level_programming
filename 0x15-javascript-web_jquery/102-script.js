#!/usr/bin/node
const $ = window.$;
$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const language = $('input#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + language;
    $.get(url, function (data) {
      $('div#hello').html(data.hello);
    });
  });
});
