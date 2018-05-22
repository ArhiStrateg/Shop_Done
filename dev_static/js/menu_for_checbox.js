var options = [];

$( '.dropdown-menu a' ).on( 'click', function( event ) {

    var $target = $( event.currentTarget ),
        val = $target.attr( 'data-value' ),
        name = $target.attr( 'name' ),
        $inp = $target.find( 'input' ),
        bloc_input = $target.attr( 'input' ),
        href_way = $target.attr( 'href' ),
        idx;
        console.log( name );

    if ( ( name == "normal" ) ) {
        window.location.href = href_way;
    }

    if ( ( name == "search_mini_menu" ) ) {

    }





    if ( ( name == "menu_low" ) ) {
        block.on('click', 'a:not([href^="#"])', function(evt) {
        evt.preventDefault();
        window.open(evt.target.href, '_blank');
        })
   }

    if ( ( name == 'search_hight' ) ) {
        if ( ( idx = options.indexOf( val ) ) > -1 ) {
            options.splice( idx, 1 );
            setTimeout( function() { $inp.prop( 'checked', false ) }, 0);
        } else {
            options.push( val );
            setTimeout( function() { $inp.prop( 'checked', true ) }, 0);
       }
    }

   $( event.target ).blur();
    console.log( options.indexOf( val ) );
    console.log( name );



   console.log( options );
   return false;
});

