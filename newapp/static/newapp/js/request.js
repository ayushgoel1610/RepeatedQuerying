function compute_url() {
  var str = "http://127.0.0.1:8000/";
  var temp = $("#ChooseScale").val();
  if(temp == "H"){
    str+= "halfhour/";
    str+= $("#ChooseDay option:selected").text() + "/";
  }
  else if( temp == "D"){
    str = "day/";
  }
  else{
    alert("Please choose a scale!");
    return;
  }    

  var date1 = $('input[name=date1]');
  var date2 = $('input[name=date2]');
  if (date1.val() != "" && date2.val() != ""){
    str+= date1.val() + "/" +  date2.val();
  }
  else{
    alert("Please choose a duration!");
    return;
  }
  charts(str,temp);
  //alert(str);
  //obj.format = temp;
  //return str;
  /*
  //computing AP label
  var APlabel;
  var temp2 = $("#Building").val();
  switch (temp2){
    case "": APlabel = "";
      break;
    case "Acad": APlabel = "ACB";
      break;
    case "Lib": APlabel = "LB";
      break;
    case "SAC": APlabel = "DB";
      break;
    case "GH": APlabel = "GH";
      break;
    case "BH": APlabel = "BH";
      break;
    default: APlabel = "";
  }
  var temp3 = $(".floor").val();
  //alert(temp3);
  switch (temp3){
    case "": APlabel += "";
      break;
    case "F0": APlabel += "0F";
      break;
    case "F1": APlabel += "1F";
      break;
    case "F2": APlabel += "2F";
      break;
    case "F3": APlabel += "3F";
      break;
    case "F4": APlabel += "4F";
      break;
    case "F5": APlabel += "5F";
      break;
    default: APlabel += "";
  }
  */
}

/*function loadXMLDoc(){
  var xmlhttp;    
  var urlstr = compute_url();
  alert(urlstr);
  if (urlstr){              
    if (window.XMLHttpRequest)
      {// code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
      }
    else
      {// code for IE6, IE5
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
      }
    xmlhttp.onreadystatechange=function()
      {
      if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
        data=xmlhttp.responseText;
        console.log(data);
        }
      }
    xmlhttp.open("GET",urlstr,true);
    xmlhttp.send();       
  }
  else
    alert ("no url");
}*/

// Create the XHR object.
function createCORSRequest(method, url) {
  var xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {
    // XHR for Chrome/Firefox/Opera/Safari.
    xhr.open(method, url, true);
  } else if (typeof XDomainRequest != "undefined") {
    // XDomainRequest for IE.
    xhr = new XDomainRequest();
    xhr.open(method, url);
  } else {
    // CORS not supported.
    xhr = null;
  }
  return xhr;
}

// Helper method to parse the title tag from the response.
function getTitle(text) {
  return text.match('<title>(.*)?</title>')[1];
}

// Make the actual CORS request.
function makeCorsRequest() {
  var obj = { format: "H" };
  var url = compute_url(obj);
  //var url = "http://192.168.1.40:9128/halfhour/any/2014-07-01/2014-07-02";
  var xhr = createCORSRequest('GET', url);
  if (!xhr) {
    alert('CORS not supported');
    return;
  }

  // Response handlers.
  xhr.onload = function() {
    var text = xhr.responseText;
    var title = getTitle(text);
    alert('Response from CORS request to ' + url + ': ' + title);
    console.log(text);
    var timeformat = obj.format;
    charts(text, timeformat);
  };

  xhr.onerror = function() {
    alert('Woops, there was an error making the request.');
  };

  xhr.send();
}
