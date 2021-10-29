$(document).ready(function() {
    'use strict';

     $('.employee_select').select2();
     $('.subdivision_select').select2();

    $('#yearradio').on('change', function () {
        $("#reportingNIDyearsince").prop("disabled", true);
        $("#reportingNIDyeartill").prop("disabled", true);
        $("#reportingNIDyearsince").prop("required", false);
        $("#reportingNIDyeartill").prop("required", false);
        $("#reportingNIDyear").prop("disabled", false);
        $("#reportingNIDyear").prop("required", true);
    });

    $('#betweenyearradio').on('change', function () {
        $("#reportingNIDyearsince").prop("disabled", false);
        $("#reportingNIDyeartill").prop("disabled", false);
        $("#reportingNIDyearsince").prop("required", true);
        $("#reportingNIDyeartill").prop("required", true);
        $("#reportingNIDyear").prop("disabled", true);
        $("#reportingNIDyear").prop("required", false);
    });

    $('#reportkind').on('change', function () {

        var kind = $("#reportkind").val();

        if (kind == 0) {
            $("#inputauthors1").prop("disabled", false);
            $("#department").prop("disabled", true);
            $("#inputauthors1").prop("required", true);
            $("#department").prop("required", false);
        }
        else if (kind == 1) {
            $("#inputauthors1").prop("disabled", true);
            $("#department").prop("disabled", false);
            $("#inputauthors1").prop("required", false);
            $("#department").prop("required", true);
        }
        else if (kind == 2) {
            $("#inputauthors1").prop("disabled", true);
            $("#department").prop("disabled", true);
            $("#inputauthors1").prop("required", false);
            $("#department").prop("required", false);
        }
        else if (kind == 3) {
            $("#inputauthors1").prop("disabled", true);
            $("#department").prop("disabled", true);
            $("#inputauthors1").prop("required", false);
            $("#department").prop("required", false);
        }

        else if (kind == 4) {
            $("#inputauthors1").prop("disabled", true);
            $("#department").prop("disabled", true);
            $("#inputauthors1").prop("required", false);
            $("#department").prop("required", false);
        }

        else if (kind == 5) {
            $("#inputauthors1").prop("disabled", true);
            $("#department").prop("disabled", false);
            $("#inputauthors1").prop("required", false);
            $("#department").prop("required", true);
        }
    });
});