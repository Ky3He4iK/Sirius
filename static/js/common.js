$(document).ready(function () {


    function heightDetect() {
        $(".main_head").css("height", $(window).height());
    };
    heightDetect();
    $(window).resize(function () {
        heightDetect();
    });

    $(".btn").mPageScroll2id();
    $(".mapbut").mPageScroll2id();

    $(".filterbut").click(function () {
        console.log(".filterbut");
        $('.filters').removeClass('inactive');
        $('.filterbut').addClass('inactive');
        $('.filterbutsec').removeClass('inactive');
    });
    $(".filterbutsec").click(function () {
        console.log(".filterbutsec");
        $('.filters').addClass('inactive');
        $('.filterbut').removeClass('inactive');
        $('.filterbutsec').addClass('inactive');
    });
});


$(window).load(function () {
    $(".loaderInner").fadeOut();
    $(".loader").delay(400).fadeOut("slow");
});

/* $(function () {
    $("#slider-range_3").slider({
        range: true,
        min: 0,
        max: 100,
        values: [0, 100],
        slide: function (event, ui) {
            $("#amount_3").val(ui.values[0] + " - " + ui.values[1]);
        }
    });
    $("#amount_3").val($("#slider-range_3").slider("values", 0) +
        " - " + $("#slider-range_3").slider("values", 1));
}); */