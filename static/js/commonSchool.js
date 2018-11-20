
$(document).ready(function(){
	
	
	

	$(".btn").mPageScroll2id();
	$(".mapbut").mPageScroll2id();
	

	
	
});



$(window).load(function() { 
	$(".loaderInner").fadeOut(); 
	$(".loader").delay(400).fadeOut("slow"); 
});

var marksCanvas = document.getElementById("EGE");

var chartOptions = {
  scale: {
    ticks: {
		beginAtZero: true,
      min: 0,
      max: 100,
      stepSize: 10
    },
    pointLabels: {
		fontFamily: "Raleway",
      fontSize: 15
    }},
	  legend: {
    display: false
  }
  
};
var radarChart = new Chart(marksCanvas, {
type: 'radar',
data: ege_data,
options: chartOptions
});


var Canvas = document.getElementById("OGE");

var Options = {
  scale: {
    ticks: {
		beginAtZero: true,
      min: 0,
      max: 100,
      stepSize: 10
    },
    pointLabels: {
		fontFamily: "Raleway",
      fontSize: 15
    }},
	  legend: {
    display: false
  }
  
};
var Chart = new Chart(Canvas, {
type: 'radar',
data: oge_data,
options: Options
});
