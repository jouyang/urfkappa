orange_active = false;
blue_active = false;
orange_champ = "";
blue_champ = "";
orange_champ_id = 0;
blue_champ_id = 0;

function resetGraph(){
    var bargraph = $("#graphHolder1stats-graph");
    if (bargraph){
        bargraph.replaceWith("<div id=\"stats-graph\"></div>");
    }
    var error = $("#error");
    if (error){
    	error.remove();
    }
}

$(window).load(function() {
	$(document).foundation();
	$("img[src='../static/icons/Square.png']").remove();

	$(".champion").click(function(){

	    if($(this).hasClass("orange-border"))
	    {
	        $(this).removeClass("orange-border");
	        orange_active = false;
	        orange_champ = "";
	        orange_champ_id = 0;
		}
	    else if(orange_active === false && !$(this).hasClass("blue-border")) 
	    {
	        $(this).addClass("orange-border");
	        orange_active = true;
	        orange_champ = $(this).attr('id');
	        orange_champ_id = $(this).attr('data-id');
	    }
	    else if($(this).hasClass("blue-border")) 
	    {
	        $(this).removeClass("blue-border");
	        blue_active = false;
	        blue_champ = "";
	        blue_champ_id = 0;
	    }
	    else if(blue_active === false && !$(this).hasClass("orange-border")) {
	        $(this).addClass("blue-border");
	        blue_active = true;
	        blue_champ = $(this).attr('id');
	        blue_champ_id = $(this).attr('data-id');
	    }
			
	    if(orange_active && blue_active) {
	        $.ajax({
	            type : 'GET',
	            url : "/stats/" + orange_champ_id + "/" + blue_champ_id,
	            beforeSend: function() {
	                $("#champ-grid").hide();
	            },
	            success: function(data) {
	                $("#orange-champ-pic").attr('src' , '../static/icons/' + orange_champ + 'Square.png');
	                $("#blue-champ-pic").attr('src' , '../static/icons/' + blue_champ + 'Square.png');

	                if("error" in data){
	                    $('#stats-graph').html("<h2 id=\"error\">Sorry... Not enough data for this match up</h2>")
	                    $("#stats").animate( { "opacity" : "show"}, 1000);
	                    return;
	                }
	                champ1_win_rate = Math.round(data['champ1_win_rate'] *100);
	                champ2_win_rate = Math.round(data['champ2_win_rate'] *100);
	                
	                var arrayOfData = new Array(
	                    [champ1_win_rate, data['champ1_name'], '#e67e22'],
	                    [champ2_win_rate, data['champ2_name'], '#3498db']
	                    ); 
	                $('#stats-graph').jqBarGraph({ data: arrayOfData,
	                                             title : "UrfKappa - Winrate: " + data['champ1_name'] + " vs " + data['champ2_name'],
	                                             barSpace: 15,
	                                             height: 400,
	                                             postfix : '%'});
	                $("#graphHolder1stats-graph").addClass("center");
	                $("#stats").animate( { "opacity" : "show"}, 800);
	            }
	        });
		}

	});

	$("#reset").click(function(){
	    $("#stats").hide();
	    resetGraph();
	    $("#champ-grid").animate( { "opacity" : "show"}, 800);
		var a = orange_champ.replace("'", "\\'");
		var b = a.replace(" ", "\\ ");
		var c = blue_champ.replace("'", "\\'");
		var d = c.replace(" ", "\\ ");
		$('#' + b).removeClass("orange-border");
		$('#' + d).removeClass("blue-border");
		orange_champ = ""; orange_active = false;
		blue_champ = ""; blue_active = false;
	});
});