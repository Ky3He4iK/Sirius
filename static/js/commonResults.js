$(document).ready(function () {
    $(".btn").mPageScroll2id();
    $(".mapbut").mPageScroll2id();
});

$(window).load(function () {
    $(".loaderInner").fadeOut();
    $(".loader").delay(400).fadeOut("slow");
});