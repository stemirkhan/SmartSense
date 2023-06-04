function fetchdata(){
    $.ajax({
     url: '/dashboard',
     type: 'get',
     contentType: 'application/json',
     success: function(response){
     for (var key in response) {
       if (response.hasOwnProperty(key)) {
           document.getElementById(key).innerHTML = response[key];
       }
       }
     }
    });
   }
   
   $(document).ready(function(){
    setInterval(fetchdata,2000);
   });