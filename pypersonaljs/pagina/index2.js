function load_pos_rest(){
    $.get("http://localhost:8080/autores/?format=json")
              .success( function( returned_data ){
           // Here You can display the returned information
           // In order to just see if it works you can  " console.log(returned_data) " to see it the browser's console

  } );
};

/*function load_pos_rest(){
debugger;
$.get("http://localhost:8000/catalogos/api/catalogos/?format=json", function(data){
debugger;
for(i=0; i<data.length; i++){

$("#div_rest_pos").append('<span>'+data[i].name+' - '+data[i].brand+'</span><br/>');
}
});
}*/