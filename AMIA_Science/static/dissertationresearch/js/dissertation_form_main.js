$( document ).ready(function() {
    'use strict';

    init();

    $('#id_author, #id_leadersemployees, #id_otherauthor, #id_leadersnotemployees').select2();

    $( "#isemployee").on( "click", function() {
        if ($(this).prop("checked")==true){
            $('#div_for_employee_author').css('display', 'block');
            $('#div_for_not_employee_author').css('display', 'none');
            $('#id_author').prop('disabled', false);
            $('#id_otherauthor').prop('disabled', true);
        } else {
            $('#div_for_employee_author').css('display', 'none');
            $('#div_for_not_employee_author').css('display', 'block');
            $('#id_author').prop('disabled', true);
            $('#id_otherauthor').prop('disabled', false);
        }
    });

    $( "#leaderisemployee").on( "click", function() {
        if ($(this).prop("checked")==true){
            $('#div_for_leader_employee').css('display', 'none');
            $('#div_for_not_leader_employee').css('display', 'block');
            $('#id_leadersnotemployees').prop('disabled', false);
            $('#id_leadersemployees').prop('disabled', true);
        } else {
            $('#div_for_leader_employee').css('display', 'block');
            $('#div_for_not_leader_employee').css('display', 'none');
            $('#id_leadersnotemployees').prop('disabled', true);
            $('#id_leadersemployees').prop('disabled', false);
        }
    });

    $('#id_researchplace').on('click', function () {
        var id = $(this).val();
        if (id == 1) {
            $('#id_researchplacesubdivision').prop('disabled', false);
            $('#id_researchplacesubdivision').prop('required', true);
        }
        else {
            $('#id_researchplacesubdivision').prop('disabled', true);
            $('#id_researchplacesubdivision').prop('required', false);
        }
    });


    function init(){
        let place_id = $('#id_researchplace').val();
        if (place_id === '1') {
            $('#id_researchplacesubdivision').prop('disabled', false);
            $('#id_researchplacesubdivision').prop('required', true);
        }
    }

});




