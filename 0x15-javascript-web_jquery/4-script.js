$(function(){
    $('DIV#toggle_header').bind('click', function(){
      if($('header').hasClass('green')){
        $('header').addClass('red')
        $('header').removeClass('green')
      } else if($('header').hasClass('red')){
        $('header').removeClass('red')
        $('header').addClass('green')
      }
    })
});
