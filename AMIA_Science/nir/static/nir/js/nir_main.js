$( document ).ready(function() {

    'use strict';

    $("#organization_check").on( "click", function() {
        if ($(this).prop("checked")==true){
            $("#organization_div").css('display', 'block');
            $("#organisation").prop('disabled', false).prop('required', true);
        }else {
            $("#organization_div").css('display', 'none');
            $("#organisation").prop('disabled', true).prop('required', false);
        }
    });

});