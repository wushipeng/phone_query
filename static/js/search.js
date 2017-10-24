function daochu() {
    $(".btn-success").css("border-color","#169F85") ;
}

function part() {

    $(".search").attr("hidden","hidden");
    $(".mymenu").removeAttr("hidden","hidden");
    // $(".part-hidden").attr("hidden",false);
    $(".part-appear").attr("hidden","hidden");
    $(".pagnation").attr("hidden","hidden");
}

function keyboard_c() {
    $(".search").removeAttr("hidden","hidden");
    $(".mymenu").attr("hidden","hidden");
    $(".part-hidden").attr("hidden",true);
    $(".part-appear").attr("hidden",false);
    $(".pagnation").attr("hidden",false);

}

function login() {
    if ($(".is-active").length == 0) {
        $(".login").removeAttr("hidden", "hidden");
    }
    else {
        $(".login").attr("hidden", "hidden");
    }
}
