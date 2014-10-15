function callback(){

}

$.ajax ({
	type: 'GET',
	url: 'http://192.168.0.12:8080/catalogos/api/catalogos/', 
	data: {},
	//data: {format: "json"},
    contentType: "application/json",
//	 dataType:'json',
	success: function (data) {
                alert("funciona");
            },
    error: function (result) {
                alert("no funciona");
            }
}).done(callback);
