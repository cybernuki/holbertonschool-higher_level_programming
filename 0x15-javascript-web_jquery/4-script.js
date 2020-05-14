$('DIV#toggle_header').bind('click', function() {
  const $header = $('header');
  console.log($header);
  
  if ($header.hasClass('red')) {
    $header.removeClass('red');
    $header.addClass('green');
  } else {
    $header.removeClass('green');
    $header.addClass('red');
  }
});