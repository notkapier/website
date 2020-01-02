$(document).on('click', '.library', function(e){
	var token = '{{csrf_token}}';
   var library_id = $(this).attr('name');
   console.log(library_id)
   $.ajax({
   	url: '/digitallibrary',
   	type: 'POST',
   	dataType: 'html',
   	headers:{
        "X-CSRFToken": token
    },
   	data:{'library_id':library_id},
   	success: function(data){
   		$('#content_container').empty();
   		$('#content_container').html(data);
   	},
   	error: function(jqXHR, textstatus, errorThrown){
   		console.log('error')
   	}
   });
})
$(".dropdown-item").on("click", (function(e){
 	e.preventDefault();
 	var slideIndex = $(this).attr('name');
 console.log(slideIndex); 
 	$( '.slider-for' ).slick('slickGoTo', slideIndex, false); 
}));