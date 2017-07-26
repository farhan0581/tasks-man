// var counter = 1;
// var limit = 10;
// function addInput(divName){
//      // if (counter == limit)  {
//      //      alert("You have reached the limit of adding " + counter + " inputs");
//      // }
//      // else {
//      //      var newdiv = document.createElement('div');
//      //      newdiv.innerHTML = "Entry " + (counter + 1) + " <br><input type='text' name='myInputs[]'>";
//      //      document.getElementById(divName).appendChild(newdiv);
//      //      counter++;
//      // }
//      var div = document.getElementById(divName),
//      clone = div.cloneNode(true);
//      clone.id = divName + ""
//      document.getElementById(divName).appendChild(clone);
// }

$('#clone').click(function() {
     var div_html = '<div id="dynamicInput" class="regional">\
                    <h4>Regional dish data</h4>\
                    Start time (defaut is current date time)\
                    <br>\
                    <br>\
                    <input type="date" name="start_datetime" class="form-control">\
                    <br>\
                    <br>\
                    <b>End time (default is 2020 date time)</b>\
                    <br>\
                    <br>\
                    <input type="date" name="end_datetime" class="form-control">\
                    <br>\
                    <b>Dish ids (comma separated)</b>\
                    <br>\
                    <textarea name="dish_id" cols="30" rows="20" class="form-control"></textarea>\
                    <br>\
                    <br>\
                    <b>Show dishes in corousel ?</b>\
                    <br>\
                    <br>\
                    <select name="show_dishes_in_carousel">\
                     <option value="0">No</option>\
                         <option value="1">Yes</option>\
                    </select>\
                    <br>\
                    <br>\
                    <b>City</b>\
                    <br>\
                    <br>\
                    <select name="city_names_id">\
                         <option value="999">SELECT</option>\
                         <option value="101">Gurgaon</option>\
                         <option value="102">Delhi</option>\
                         <option value="103">Noida</option>\
                         <option value="104">Hyderabad</option>\
                         <option value="106">Mumbai</option>\
                         <option value="105">Bangalore</option>\
                         <option value="108">Pune</option>\
                         <option value="107">Chennai</option>\
                         <option value="109">Kolkata</option>\
                    </select>\
                    <br><br>\
               </div>'
     // $('.regional').clone().insertAfter(".regional");
     $("#clone").before(div_html);

});


$("#savemydish").click(function() {

     var sf_name = $('#tag_sf_name').val();
    $.ajax({
     url:"/curated_data/check_sf_name/",
     dataType:'json',
     type: 'post',
     data: {"sf_name":sf_name},
     success:function(response){
          
          if (response.name == 'no')
          {
               alert('This sf name already exists, please change it..!!');
               return false;
          }
          else if (response.name == 'yes')
          {    
               $('#save').click()
          }
     }
     });

});

// $('#specials_form').submit(function(){
$('#publish').click(function(){
     var city_dict = {
                    '101':'gurgaon',
                    '102':'delhi',
                    '103':'noida',
                    '104':'hyderabad',
                    '105':'bangalore',
                    '106':'mumbai',
                    '107': 'chennai',
                    '108': 'pune',
                    '109': 'kolkata',
               };
     var tag_name = $('[name="tag_name"]').val();
     var tag_sf_name = $('[name="tag_sf_name"]').val();
     var fb_share_title = $('[name="fb_share_title"]').val();
     var fb_share_desc = $('[name="fb_share_desc"]').val();
     var image_url = $('[name="image_url"]').val();
     var mode = $('[name="mode"]').val();
     var cat_name = $('[name="cat_name"]').val();
     var city_names = $('[name="city_names"]').val();
     var flag = 0;
     var count = 0;
     var city_array = [];
     $(".regional").each(function() {
          var cur_city_id = $(this).find('[name="city_names_id"]').val().toLowerCase();
          city_name = city_dict[cur_city_id]
          if(cur_city_id != 'select')
          {
               city_array.push(city_name);
          };
          var dish_ids = $(this).find('[name="dish_id"]').val().split(",");
          for(j=0; j<dish_ids.length; j++)
          {
               trim_id = dish_ids[j].replace(/^\s+|\s+$/g, '');
               if(trim_id.length != 8)
               {    
                    // console.log(trim_id);
                    alert('Problem in dish ids of ' + city_name);
                    flag = 1;
               };
          };
          
     });
     if(city_array.length != city_names.length)
     {
          alert('There is some city mismatch in the dropdowns please check,length');
          flag = 1;
     }
     else{

          for (i = 0; i < city_names.length; i++) { 
               
               if($.inArray(city_names[i], city_array) == -1)
               {
                    alert('There is some city mismatch in the dropdowns please check,repated');
                    flag = 1
               };
          };

     };
     if(tag_name.length == 0)
     {
          alert('Please enter the tag name.');
          flag = 1;
     };
     if(tag_sf_name.length == 0)
     {
          alert('Please enter the tag sf name.');
          flag = 1;
     };
     if(fb_share_title.length == 0)
     {
          alert('Please enter the fb share title');
          flag = 1;
     };
     if(fb_share_desc.length == 0)
     {
          alert('Please enter the fb share description');
          flag = 1;
     };
     if(image_url.length == 0)
     {
          alert('Please enter the Image url');
          flag = 1;
     };
     if(cat_name.length == 0)
     {
          alert('Please enter the category name');
          flag = 1;
     };

     if(flag == 1)
     {
          return false;
     }
     else{
          return true;
     };

    });




