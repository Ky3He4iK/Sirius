
$(document).ready(function(){



	function heightDetect() {
		$(".main_head").css("height", $(window).height());
	};
	heightDetect();
	$(window).resize(function() {
		heightDetect();
	});

	$(".btn").mPageScroll2id();
	$(".mapbut").mPageScroll2id();

  	$(".filterbut").click(function(){
		$('.filters').toggleClass('active');
		$('.filterbut').toggleClass('active');
		$('.filterbutsec').toggleClass('active');
	});
	$(".filterbutsec").click(function(){
		$('.filters').toggleClass('active');
		$('.filterbut').toggleClass('active');
		$('.filterbutsec').toggleClass('active');
	});


});


$(window).load(function() {
	$(".loaderInner").fadeOut();
	$(".loader").delay(400).fadeOut("slow");
});


$( function() {
    $( "#slider-range_1" ).slider({
      range: true,
      min: 0,
      max: 100,
      values: [ 0, 100 ],
      slide: function( event, ui ) {
        $( "#amount_1" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_1" ).val($( "#slider-range_1" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_1" ).slider( "values", 1 ) );
  } );


$( function() {
    $( "#slider-range_2" ).slider({
      range: true,
      min: 0,
      max: 100,
      values: [ 0, 100 ],
      slide: function( event, ui ) {
        $( "#amount_2" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_2" ).val($( "#slider-range_2" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_2" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_3" ).slider({
      range: true,
      min: 0,
      max: 100,
      values: [ 0, 100 ],
      slide: function( event, ui ) {
        $( "#amount_3" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_3" ).val($( "#slider-range_3" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_3" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_4" ).slider({
      range: true,
      min: 0,
      max: 100,
      values: [ 0, 100 ],
      slide: function( event, ui ) {
        $( "#amount_4" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_4" ).val($( "#slider-range_4" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_4" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_5" ).slider({
      range: true,
      min: 0,
      max: 100,
      values: [ 0, 100 ],
      slide: function( event, ui ) {
        $( "#amount_5" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_5" ).val($( "#slider-range_5" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_5" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_6" ).slider({
      range: true,
      min: 0,
      max: 100,
      values: [ 0, 100 ],
      slide: function( event, ui ) {
        $( "#amount_6" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_6" ).val($( "#slider-range_6" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_6" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_7" ).slider({
      range: true,
      min: 0,
      max: 100,
      values: [ 0, 100 ],
      slide: function( event, ui ) {
        $( "#amount_7" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_7" ).val($( "#slider-range_7" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_7" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_8" ).slider({
      range: true,
      min: 0,
      max: 100,
      values: [ 0, 100 ],
      slide: function( event, ui ) {
        $( "#amount_8" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_8" ).val($( "#slider-range_8" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_8" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_9" ).slider({
      range: true,
      min: 0,
      max: 100,
      values: [ 0, 100 ],
      slide: function( event, ui ) {
        $( "#amount_9" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_9" ).val($( "#slider-range_9" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_9" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_10" ).slider({
      range: true,
      min: 0,
      max: 100,
      values: [ 0, 100 ],
      slide: function( event, ui ) {
        $( "#amount_10" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_10" ).val($( "#slider-range_10" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_10" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_11" ).slider({
      range: true,
      min: 0,
      max: 100,
      values: [ 0, 100 ],
      slide: function( event, ui ) {
        $( "#amount_11" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_11" ).val($( "#slider-range_11" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_11" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_12" ).slider({
      range: true,
      min: 0,
      max: 100,
      values: [ 0, 100 ],
      slide: function( event, ui ) {
        $( "#amount_12" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_12" ).val($( "#slider-range_12" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_12" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_13" ).slider({
      range: true,
      min: 0,
      max: 100,
      values: [ 0, 100 ],
      slide: function( event, ui ) {
        $( "#amount_13" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_13" ).val($( "#slider-range_13" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_13" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_14" ).slider({
      range: true,
      min: 0,
      max: 100,
      values: [ 0, 100 ],
      slide: function( event, ui ) {
        $( "#amount_14" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_14" ).val($( "#slider-range_14" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_14" ).slider( "values", 1 ) );
  } );













$( function() {
    $( "#slider-range_01" ).slider({
      range: true,
      min: 2,
      max: 5,
      values: [ 2, 5 ],
      slide: function( event, ui ) {
        $( "#amount_01" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_01" ).val($( "#slider-range_01" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_01" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_02" ).slider({
      range: true,
      min: 2,
      max: 5,
      values: [ 2, 5 ],
      slide: function( event, ui ) {
        $( "#amount_02" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_02" ).val($( "#slider-range_02" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_02" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_03" ).slider({
      range: true,
      min: 2,
      max: 5,
      values: [ 2, 5 ],
      slide: function( event, ui ) {
        $( "#amount_03" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_03" ).val($( "#slider-range_03" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_03" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_04" ).slider({
      range: true,
      min: 2,
      max: 5,
      values: [ 2, 5 ],
      slide: function( event, ui ) {
        $( "#amount_04" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_04" ).val($( "#slider-range_04" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_04" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_05" ).slider({
      range: true,
      min: 2,
      max: 5,
      values: [ 2, 5 ],
      slide: function( event, ui ) {
        $( "#amount_05" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_05" ).val($( "#slider-range_05" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_05" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_06" ).slider({
      range: true,
      min: 2,
      max: 5,
      values: [ 2, 5 ],
      slide: function( event, ui ) {
        $( "#amount_06" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_06" ).val($( "#slider-range_06" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_06" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_07" ).slider({
      range: true,
      min: 2,
      max: 5,
      values: [ 2, 5 ],
      slide: function( event, ui ) {
        $( "#amount_07" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_07" ).val($( "#slider-range_07" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_07" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_08" ).slider({
      range: true,
      min: 2,
      max: 5,
      values: [ 2, 5 ],
      slide: function( event, ui ) {
        $( "#amount_08" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_08" ).val($( "#slider-range_08" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_08" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_09" ).slider({
      range: true,
      min: 2,
      max: 5,
      values: [ 2, 5 ],
      slide: function( event, ui ) {
        $( "#amount_09" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_09" ).val($( "#slider-range_09" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_09" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_010" ).slider({
      range: true,
      min: 2,
      max: 5,
      values: [ 2, 5 ],
      slide: function( event, ui ) {
        $( "#amount_010" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_010" ).val($( "#slider-range_010" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_010" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_011" ).slider({
      range: true,
      min: 2,
      max: 5,
      values: [ 2, 5 ],
      slide: function( event, ui ) {
        $( "#amount_011" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_011" ).val($( "#slider-range_011" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_011" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_012" ).slider({
      range: true,
      min: 2,
      max: 5,
      values: [ 2, 5 ],
      slide: function( event, ui ) {
        $( "#amount_012" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_012" ).val($( "#slider-range_012" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_012" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_013" ).slider({
      range: true,
      min: 2,
      max: 5,
      values: [ 2, 5 ],
      slide: function( event, ui ) {
        $( "#amount_013" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_013" ).val($( "#slider-range_013" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_013" ).slider( "values", 1 ) );
  } );

$( function() {
    $( "#slider-range_014" ).slider({
      range: true,
      min: 2,
      max: 5,
      values: [ 2, 5 ],
      slide: function( event, ui ) {
        $( "#amount_014" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount_014" ).val($( "#slider-range_014" ).slider( "values", 0 ) +
      " - " + $( "#slider-range_014" ).slider( "values", 1 ) );
  } );



/*
var slider_1 = document.getElementById('step_1');

noUiSlider.create(slider_1, {
	start: [0,100],
	connect: true,
    range: {
        'min': 0,
        'max': 100
	}
});

var slider_2 = document.getElementById('step_2');

noUiSlider.create(slider_2, {
	start: [0,100],
	connect: true,
    range: {
        'min': 0,
        'max': 100
	}
});*/


