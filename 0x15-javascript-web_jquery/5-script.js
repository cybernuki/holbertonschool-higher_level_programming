$('DIV#add_item').bind('click', function(){
  const $ul = $('UL.my_list');
  const item = $("<li></li>").text("Item");
  $ul.append(item);
});