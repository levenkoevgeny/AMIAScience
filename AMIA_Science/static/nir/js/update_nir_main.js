$( document ).ready(function() {
    'use strict';

    init();

    function init() {

        if ($("#organization_check").prop('checked') == true) {
            $("#organization_div").css('display', 'block');
            $("#organisation").prop('disabled', false).prop('required', true);
        } else {
            $("#organisation").prop('disabled', true).prop('required', false);
        }



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

        authorinputcount = 0;
        $(".authorinputotherlastname").each(function() {
            authorinputcount++;
            $(this).attr("id", "inputauthorsotherlastname" + authorinputcount);
            $(this).attr("name", "inputauthorsotherlastname" + authorinputcount);
        });

        authorinputcount = 0;
        $(".authorinputotherpatronymic").each(function() {
            authorinputcount++;
            $(this).attr("id", "inputauthorsotherpatronymic" + authorinputcount);
            $(this).attr("name", "inputauthorsotherpatronymic" + authorinputcount);
        });


        authorinputcount = 1;
        $(".rowextraauthorsother").each(function() {
            authorinputcount++;
            $(this).attr("id", "rowextraauthorsother" + authorinputcount);
        });

        authorinputcount = 1;
        $(".deleteauthorbuttonother").each(function() {
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

    }


});