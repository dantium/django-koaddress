function setup_qa(qinput,qcode,qstreet1,qstreet2,url) {
	var input = $(qinput);
	var code = $(qcode);
	var street1 = $(qstreet1);
	var street2 = $(qstreet2);
	
	input.keypress(function(e){
	    if (e.which == 13) {
	       var tagName = e.target.tagName.toLowerCase(); 
	       if (tagName !== "textarea") {
	           return false;
	       }
	   }
	});
	
	input.autocomplete({
		source: function( request, response ) {
			$.ajax({
				url: url,
				dataType: "jsonp",
				data: {
					q: request.term
				},
				success: function( data ) {
					response( $.map( data, function( item ) {
						all_data = item.fields.code + ' ' + item.fields.city + ' ' + item.fields.town + ' ' + item.fields.area + ' ' + item.fields.block;
						return {
							label: all_data,
							value: all_data,
							code: item.fields.code,
							city: item.fields.city,
							town: item.fields.town,
							area: item.fields.area,
							block: item.fields.block
						}
					}));
				}
			});
		},
		minLength: 2,
		select: function( event, ui ) {				
			code.val(ui.item.code);
			street1.val(ui.item.city +' '+ ui.item.town +' '+ ui.item.area);
			street2.val(ui.item.block);
			street2.focus();
		},
		open: function() {
			$( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
		},
		close: function() {
			$( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
		}
	});
};