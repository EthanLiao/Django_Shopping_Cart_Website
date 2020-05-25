$("#twzipcode_ADV").twzipcode({
zipcodeIntoDistrict: true, // 郵遞區號自動顯示在地區
css: ["city form-control", "town form-control"], // 自訂 "城市"、"地區" class 名稱
countyName: "city", // 自訂城市 select 標籤的 name 值
districtName: "town" // 自訂地區 select 標籤的 name 值
});


$("#county").on("change",function(){
  district = $("#twzipcode_ADV").twzipcode('get', ['zipcode','county','district']);
  document.getElementById('address_input_id').value = district[0]+district[1]+district[2];
});

$("#district").on("change",function(){
  district = $("#twzipcode_ADV").twzipcode('get', ['zipcode','county','district']);
  document.getElementById('address_input_id').value = district[0]+district[1]+district[2];
});

function validateEmail(email) {
  var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(email);
}

$("#email_input_id").on('focus',function(){
  var email=$(this).val();
  var $result = $("#result");
  if(validateEmail(email))
  {
    $result.text(email + " is valid :)");
    $result.css("color", "green");
  }
  else
  {
    $result.text(email + " is not valid :(");
    $result.css("color", "red");
  }
});


$("#email_input_id").on("focusout",function(){
  var email=$(this).val();
  var $result = $("#result");
  if(validateEmail(email))
  {
    $result.text(email + " is valid :)");
    $result.css("color", "green");
  }
  else
  {
    $result.text(email + " is not valid :(");
    $result.css("color", "red");
  }
});


$("#email_input_id").on("change",function(){
  var email=$(this).val();
  var $result = $("#result");
  if(validateEmail(email))
  {
    $result.text(email + " is valid :)");
    $result.css("color", "green");
  }
  else
  {
    $result.text(email + " is not valid :(");
    $result.css("color", "red");
  }
});
