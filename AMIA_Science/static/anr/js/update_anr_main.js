$( document ).ready(function() {
    'use strict';

    var inputs = $('#student_lastname, #student_patronymic');

    init();

    function init() {
        var authorinputcount;

        $('.authors_multiple_update').select2();

        authorinputcount = 0;
        $(".authorinput").each(function () {
            authorinputcount++;
            $(this).attr("id", "inputauthors" + authorinputcount);
            $(this).attr("name", "inputauthors" + authorinputcount);
        });

        authorinputcount = 0;
        $(".authoridhidden").each(function () {
            authorinputcount++;
            $(this).attr("id", "authoridhidden" + authorinputcount);
            $(this).attr("name", "authoridhidden" + authorinputcount);
        });

        authorinputcount = 1;
        $(".rowextraauthors").each(function () {
            authorinputcount++;
            $(this).attr("id", "rowextraauthors" + authorinputcount);
        });

        authorinputcount = 1;
        $(".deleteauthorbutton").each(function () {
            authorinputcount++;
            $(this).attr("value", "rowextraauthors" + authorinputcount);
        });

        authorinputcount = 0;
        $(".authorinputotherlastname").each(function () {
            authorinputcount++;
            $(this).attr("id", "inputauthorsotherlastname" + authorinputcount);
            $(this).attr("name", "inputauthorsotherlastname" + authorinputcount);
        });

        authorinputcount = 0;
        $(".authorinputotherpatronymic").each(function () {
            authorinputcount++;
            $(this).attr("id", "inputauthorsotherpatronymic" + authorinputcount);
            $(this).attr("name", "inputauthorsotherpatronymic" + authorinputcount);
        });


        authorinputcount = 1;
        $(".rowextraauthorsother").each(function () {
            authorinputcount++;
            $(this).attr("id", "rowextraauthorsother" + authorinputcount);
        });

        authorinputcount = 1;
        $(".deleteauthorbuttonother").each(function () {
            authorinputcount++;
            $(this).attr("value", "rowextraauthorsother" + authorinputcount);
        });

        if ($("#otherauthorscheckpld").prop('checked') == true) {
            $(".authorinputotherlastname").each(function() {
                $(this).prop( "disabled", false);
            });

            $(".authorinputotherpatronymic").each(function() {
                $(this).prop( "disabled", false);
            });

            $(".deleteauthorbuttonother").each(function() {
                $(this).prop( "disabled", false);
            });

            $("#scienceworkaddauthorother").prop( "disabled", false);
        }
        else {
            $(".authorinputotherlastname").each(function() {

                $(this).prop( "disabled", true);
            });

            $(".authorinputotherpatronymic").each(function() {
                $(this).prop( "disabled", true);
            });

            $(".deleteauthorbuttonother").each(function() {
                $(this).prop( "disabled", true);
            });

            $("#scienceworkaddauthorother").prop( "disabled", true);
        }

        if ($("#student_participation").prop('checked') == true) {
            $("#student_block").css('display', 'block');
            inputs.prop('disabled', false).prop('required', true);
        }
        else {
            $("#student_block").css('display', 'none');
            inputs.prop('disabled', true).prop('required', false);
        }

        if ($("#has_not_work_check").prop("checked")==true){
            $('#has_work').css('display', 'none');
            $('#has_not_work').css('display', 'block');
            $('#workinputhidden, #workkindhidden, #publinput').prop('disabled', true).prop('required', false);
            $('#hasnot_publinput').prop('disabled', false).prop('required', true);
        }else {
            $('#has_work').css('display', 'block');
            $('#has_not_work').css('display', 'none');
            $('#workinputhidden, #workkindhidden, #publinput').prop('disabled', false).prop('required', true);
            $('#hasnot_publinput').prop('disabled', true).prop('required', false);
        }

        var id = $('#developmentkind').val(); var disser = 3; var divs = $('#other_authors_div, #student_participation_div');

        divs.css('display', 'block');

        if (id == disser) {
            divs.css('display', 'none');
        }

    }

});