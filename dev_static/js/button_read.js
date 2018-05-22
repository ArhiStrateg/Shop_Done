function facechange (objName) {
    if ( $(objName).css('display') == 'none' ) {
    $(objName).animate({height: 'hide'}, 400);
    } else {
    $(objName).animate({height: 'show'}, 200);
    }
};

