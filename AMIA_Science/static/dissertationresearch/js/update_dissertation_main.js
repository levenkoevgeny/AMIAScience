$( document ).ready(function() {
    'use strict';

    var set_author_other = $('#disserauthorlastname, #inputauthorsotherpatronymic1');
    var set_author = $('#inputauthors1');

    init();

    function init() {

        if ($("#isemployee").prop('checked') == true) {
            authorisemployee();
        } else {
            authorisnotemployee();
        }


        var id = $('#disserplace').val();

        if (id == 1) {
            $('#disserplacesubdivision').prop('disabled', false).prop('required', true);
        } else {
            $('#disserplacesubdivision').prop('disabled', true).prop('required', false);
        }
    }

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