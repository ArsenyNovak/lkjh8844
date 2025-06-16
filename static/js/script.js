$(document).ready(function(){
  var i = $('input').length + 1;

  $('#add').click(function() {
    $('<input>', {type: 'text', name: 'name'+ i ,}).fadeIn('slow').appendTo('.inputs');
    i++;
  });

//  $('#myForm').submit(function(e){
//    e.preventDefault();
//    var answers = [];
//    $('.field').each(function() {
//      answers.push($(this).val());
//    });
//    alert(answers.join(', '));
//  });
});