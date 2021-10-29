$( document ).ready(function() {
    'use strict';

    var id = $('#id_kind').val();
    init_fields(id);

    var authorinputcount;

    authorinputcount = 0;
    $(".authorinput").each(function() {
        authorinputcount++;
        $(this).attr("id", "inputauthors" + authorinputcount);
        $(this).attr("name", "inputauthors" + authorinputcount);
    });

    authorinputcount = 0;
    $(".authoridhidden").each(function() {
        authorinputcount++;
        $(this).attr("id", "authoridhidden" + authorinputcount);
        $(this).attr("name", "authoridhidden" + authorinputcount);
    });

    authorinputcount = 0;
    $(".checkboxextraauthors").each(function() {
        authorinputcount++;
        $(this).attr("id", "checkboxextraauthors" + authorinputcount);
        $(this).attr("name", "checkboxextraauthors" + authorinputcount);
    });

    authorinputcount = 1;
    $(".rowextraauthors").each(function() {
        authorinputcount++;
        $(this).attr("id", "rowextraauthors" + authorinputcount);
    });

    authorinputcount = 1;
    $(".deleteauthorbutton").each(function() {
        authorinputcount++;
        $(this).attr("value", "rowextraauthors" + authorinputcount);
    });

    var selected_option_magazine = $('#id_magazine option:selected').val();
    var selected_option_digest = $('#id_digest option:selected').val();

    if (selected_option_magazine !='') {
        $('#magazinekindradio').click();
    }

    if (selected_option_digest !='' ) {
        $('#digestkindradio').click();
    }

    var selected_option_international_base = $('#id_ininternational option:selected').val();

    if (selected_option_international_base > 0 ) {
        $('#id_ininternational').prop("disabled", false).prop("required", true);
        $('#ininternational_check').prop("checked", true);
    }

    if($("#id_is_forum_result").attr("checked") == 'checked') {
        $('#konfer').css('display', 'block');
        $('#id_conference').prop("disabled", false).prop("required", true);
    }

    var select_option_grif = $('#id_grif').val();

    if (select_option_grif !=''){
        $('#id_grif_check').click();
    }
});