$( document ).ready(function() {
    'use strict';

    var set_author_other = $('#disserauthorlastname, #inputauthorsotherpatronymic1');
    var set_author = $('#inputauthors1');

    $( "#isemployee").on( "click", function() {
        if ($(this).prop("checked")==true){
            authorisemployee();
        } else {
            authorisnotemployee();
        }
    });

    $('#disserplace').on('change', function () {

        var id = $('#disserplace').val();

        if (id == 1) {
            $('#disserplacesubdivision').prop('disabled', false);
            $('#disserplacesubdivision').prop('required', true);
        }
        else {
            $('#disserplacesubdivision').prop('disabled', true);
            $('#disserplacesubdivision').prop('required', false);
        }

    });

    function authorisemployee() {
        $('#divfornotemployeeauthor').css('display', 'none');
        $('#divforemployeeauthor').css('display', 'block');
        set_author_other.prop('disabled', true).prop('required', false);
        set_author.prop('disabled', false).prop('required', true);
    }

    function authorisnotemployee() {
        $('#divfornotemployeeauthor').css('display', 'block');
        $('#divforemployeeauthor').css('display', 'none');
        set_author_other.prop('disabled', false).prop('required', true);
        set_author.prop('disabled', true).prop('required', false);
    }

});