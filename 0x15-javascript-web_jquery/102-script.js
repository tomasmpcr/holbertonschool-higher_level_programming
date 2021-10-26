window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.getJSON(`https://fourtonfish.com/hellosalut/?lang=${lang}`, function (data, textStatus, jqXHR) {
      $('DIV#hello').text(data.hello);
    });
  });
};
