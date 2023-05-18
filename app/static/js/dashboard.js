function fetchdata(){
 $.ajax({
  url: '/dashboard',
  type: 'get',
  contentType: 'application/json',
  success: function(response){
   document.getElementById("temperature").innerHTML = response.temperature;
   document.getElementById("humidity").innerHTML = response.humidity;
   document.getElementById("carbon_monoxide").innerHTML = response.carbon_monoxide;
   document.getElementById("atmosphere_pressure").innerHTML = response.atmosphere_pressure;
  }
 });
}

$(document).ready(function(){
 setInterval(fetchdata,2000);
});