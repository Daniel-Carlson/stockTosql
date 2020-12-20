// This is the javascript that loads the data using AJAX method, loads up some arrays and calls the arrays as chart elements.

$(document).ready(function(){
	
	$.ajax({
		url : "http://192.168.254.17/stockapp/total.php",
		type : "GET",
		success : function (final_array) {
			var obj = JSON.parse(final_array);
			console.log(obj[1]);
			
			//creating list elemnts to hold the values from the db
			var values = {total_value : []};
			var change = {total_change : []};
			var times = {day: []};
			var base_amount = {base: []};
			
			var len = obj.length;
			var sum_change = 0;
			
			//based off the length of the json object fill up the list 
			//objects
			for (var i=0; i<len; i++) {
				values.total_value.push(obj[i].total_value);
				change.total_change.push(obj[i].total_change);
				times.day.push(obj[i].day);
				base_amount.base.push(2239.47) //making a refence line for the total amount invested
			}
			//creating a total change variabel
			for (var i=0; i<change.total_change.length; i++) {
				sum_change += Number(change.total_change[i])
			}
			
			console.log(sum_change)
			// so now we have the total change as a variable sum change
			// we now need to add it to the html container
			
			document.getElementById("sum-container").innerHTML = "Total Portfolio Change: " +  sum_change
			
			
			var ctx = $("#line-chartcanvas");
			
			var data ={
				labels : times.day,
				datasets : [
					{
						label : "Portfolio value",
						data : values.total_value,
						backgroundColor : "blue",
						borderColor : "lightblue",
						fill : false,
						lineTension : 0,
						pointRadius : 5	
					},
					{
						label : "total invested",
						data : base_amount.base,
						backgroundColor : "red",
						borderColor : "red",
						fill : false,
						lineTension : 0,
						borderDash: [20, 20],
						pointRadius : 1	
					}	
				]
			};
			
			
			var chart = new Chart( ctx, {
				type : "line",
				data : data,
				options : {}
			});
			},
		error : function (data) {
			console.log("you are retard");
			
			}
			
	});
});	
