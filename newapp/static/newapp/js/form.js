$(document).ready(function() {

  $("#ChooseDaydiv").hide();
  //function to display required date selectors on selection of a particular time scale
  $("#ChooseScale").change(function() {
    if( $(this).val() == "H"){
      $("#ChooseDaydiv").show();
    }
    else if( $(this).val() == "D"){
      $("#ChooseDaydiv").hide();
    }
  });

  $.Acadselect = function(){
    $("#Acad").change(function(){
      var selectedvalue = $('#Acad option:selected').text();
      /*if (selectedvalue == "Ground Floor"){
          $(".wing").hide();
          $("#Classrooms").show();              
      }
      else*/ if ((selectedvalue == "First Floor")||(selectedvalue == "Second Floor")){
          $(".wing").hide();
          $("#AcadandHostelWings").show();
          //$.Acadwingselect1();
        }
      else if ((selectedvalue == "Third Floor")||(selectedvalue == "Fourth Floor")||(selectedvalue == "Fifth Floor")){
          $(".wing").hide();
          $("#AcadWings").show();
          //$.Acadwingselect2();
        }
      else {
        $(".wing").hide();
      }          
    });
  };

  $.Libselect = function(){
    $("#Lib").change(function(){
      var selectedvalue = $('#Lib option:selected').text();
      if ((selectedvalue == "Third Floor")||(selectedvalue == "Second Floor")){
          $(".wing").hide();
          $("#LibLabs").show();
        }
      else {
        $(".wing").hide();
      }          
    });
  };

  $.Hostelselect = function(){
    $("#GH").change(function(){
      var selectedvalue = $('#GH option:selected').text();
      if (selectedvalue == ""){
          $(".wing").hide();
          }
      else {
        $(".wing").hide();
        $("#AcadandHostelWings").show();
      }          
    });
  };

  $.Hostelselect = function(){
    $("#BH").change(function(){
      var selectedvalue = $('#BH option:selected').text();
      if (selectedvalue == ""){
          $(".wing").hide();
          }
      else {
        $(".wing").hide();
        $("#AcadandHostelWings").show();
      }          
    });
  };

  $.hideAll = function(){
    $("#location > select").hide();          
    $("#Building").show();
  };
  
  $.Buildingselect = function(){     
    $('#Building').change(function () {
    if ($('#Building option:selected').text() == "Academic Block"){
        $.hideAll();
        $('#Acad').show();
        $.Acadselect();                               
    }
    else if ($('#Building option:selected').text() == "Library and Information Centre"){
        $.hideAll();
        $('#Lib').show();
        $.Libselect();
    }
    else if ($('#Building option:selected').text() == "Students Activity Centre"){
        $.hideAll();
        $('#SAC').show();
    }
    else if ($('#Building option:selected').text() == "Girls Hostel"){
        $.hideAll();
        $('#GH').show();
        $.Hostelselect();
    }
    else if ($('#Building option:selected').text() == "Boys Hostel"){
        $.hideAll();
        $('#BH').show();
        $.Hostelselect();
    }
    else if ($('#Building option:selected').text() == "Faculty Housing"){
        $.hideAll();
        $('#FH').show();
    }
    else {
        $.hideAll();
    }
    });
  };

  $.hideAll();
  $.Buildingselect();

});