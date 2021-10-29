$( document ).ready(function() {
    'use strict';

    $('#id_conference').on('change', function () {
        var konference_id = $('#id_conference').val();

        // $("#scienceworkstatusforum, #scienceworkorganizatorforum, #scienceworkcityforforum").val($("#scienceworkstatusforum option:first").val());

        switch(parseInt(konference_id, 10)) {
            case 1:
                $("#id_forumstatus").val("2");
                $("#id_organizatorforum").val("1");
                $("#id_forumcountry").val("7");
                $("#id_kindforum").val("1");
                break;
            case 8:
                $("#id_forumstatus").val("2");
                $("#id_organizatorforum").val("1");
                $("#id_forumcountry").val("7");
                $("#id_kindforum").val("2");
                break;
        }

    });

});