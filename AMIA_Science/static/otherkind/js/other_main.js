$( document ).ready(function() {
    'use strict';

    var npa = 3; var opposing = 4;
    var counsil = 5; var editoral_board = 6;
    var work_group = 7; var make_review = 8;
    var make_conclusion = 9;
    var divs = $('#opposing_div, #npa_div, #editoral_board_div, #counsil_div, #work_group_div');

    var all_inputs = $('#сouncil, #completed_work_council, #institution, #dissertation_kind, ' +
        '#defense_place, #research_theme, #aspirant,#defense_date, #work_reason, #work_kind, ' +
        '#work_subcontractors, #edition_name, #founder, #completed_work_editoral, #study_name, ' +
        '#group_establishment, #participation_result, #aspirant_lastname, #aspirant_initials, '+
        '#research_institution');
    var counsil_div_inputs = $('#сouncil, #completed_work_council, #institution');
    var opposing_div_inputs = $('#dissertation_kind, #defense_place, #research_theme, #aspirant,#defense_date, #aspirant_lastname, #aspirant_initials');
    var npa_div_inputs = $('#work_reason, #work_kind, #work_subcontractors');
    var editoral_board_div_inputs = $('#edition_name, #founder, #completed_work_editoral');
    var work_group_div_inputs = $('#study_name, #group_establishment, #participation_result');
    var make_review_div_inputs = $('#research_institution');


    $('#activity').on('change', function () {
        var id = $('#activity').val();

        switch(parseInt(id, 10)) {
            case npa:
                divs.css('display', 'none');
                $('#npa_div').css('display', 'block');
                all_inputs.prop('disabled', true).prop('required', false);
                npa_div_inputs.prop('disabled', false).prop('required', true);
                break;
            case opposing:
                divs.css('display', 'none');
                $('#opposing_div').css('display', 'block');
                $('#defense_date_div').css('display', 'block');
                $('#make_review_div').css('display', 'none');
                all_inputs.prop('disabled', true).prop('required', false);
                opposing_div_inputs.prop('disabled', false).prop('required', true);
                break;
            case make_review:
                divs.css('display', 'none');
                $('#opposing_div').css('display', 'block');
                $('#defense_date_div').css('display', 'none');
                $('#make_review_div').css('display', 'block');
                all_inputs.prop('disabled', true).prop('required', false);
                opposing_div_inputs.prop('disabled', false).prop('required', true);
                $('#defense_date').prop('disabled', true).prop('required', false);
                make_review_div_inputs.prop('disabled', false).prop('required', true);
                break;
            case make_conclusion:
                divs.css('display', 'none');
                $('#opposing_div').css('display', 'block');
                $('#defense_date_div').css('display', 'none');
                $('#make_review_div').css('display', 'block');
                all_inputs.prop('disabled', true).prop('required', false);
                opposing_div_inputs.prop('disabled', false).prop('required', true);
                $('#defense_date').prop('disabled', true).prop('required', false);
                make_review_div_inputs.prop('disabled', false).prop('required', true);
                break;
            case counsil:
                divs.css('display', 'none');
                $('#counsil_div').css('display', 'block');
                all_inputs.prop('disabled', true).prop('required', false);
                counsil_div_inputs.prop('disabled', false).prop('required', true);
                break;
            case editoral_board:
                divs.css('display', 'none');
                $('#editoral_board_div').css('display', 'block');
                all_inputs.prop('disabled', true).prop('required', false);
                editoral_board_div_inputs.prop('disabled', false).prop('required', true);
                break;
            case work_group:
                divs.css('display', 'none');
                $('#work_group_div').css('display', 'block');
                all_inputs.prop('disabled', true).prop('required', false);
                work_group_div_inputs.prop('disabled', false).prop('required', true);
                break;
        }
    });
});