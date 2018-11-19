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
        $('.filters').toggleClass('active');
        $('.filterbut').toggleClass('active');
        $('.filterbutsec').toggleClass('active');
    });
    $(".filterbutsec").click(function () {
        $('.filters').toggleClass('active');
        $('.filterbut').toggleClass('active');
        $('.filterbutsec').toggleClass('active');
    });


});


$(window).load(function () {
    $(".loaderInner").fadeOut();
    $(".loader").delay(400).fadeOut("slow");
});


$('.nstSlider').nstSlider({
    "crossable_handles": false,
    "left_grip_selector": ".leftGrip",
    "right_grip_selector": ".rightGrip",
    "value_bar_selector": ".bar",
    "value_changed_callback": function (cause, leftValue, rightValue) {
        $(this).parent().find('.leftLabel').text(leftValue);
        $(this).parent().find('.rightLabel').text(rightValue);
    }
});

$("#slider").slider({
    min: 0,
    max: 1000,
    values: [0, 1000],
    range: true
});

