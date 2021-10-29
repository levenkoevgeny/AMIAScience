$( document ).ready(function() {

    'use strict';

    function init_page(){
        let id = $('#radio_value_id').val();
        console.log(id);
        if (id === '1') {
            $('#yearradio').click();
            $('#reportingNIDyear').prop( "disabled", false).prop("required", true);
            $('#reportingNIDyearsince').prop( "disabled", true).prop("required", false);
            $('#reportingNIDyeartill').prop( "disabled", true).prop("required", false);

        } else {
            $('#betweenyearradio').click();
            $('#reportingNIDyear').prop( "disabled", true).prop("required", false);
            $('#reportingNIDyearsince').prop( "disabled", false).prop("required", true);
            $('#reportingNIDyeartill').prop( "disabled", false).prop("required", true);
        }
    }
    init_page();

    $('#yearradio').on('change', function () {
        $('#reportingNIDyear').prop( "disabled", false).prop("required", true);
        $('#reportingNIDyearsince').prop( "disabled", true).prop("required", false);
        $('#reportingNIDyeartill').prop( "disabled", true).prop("required", false);
    });

    $('#betweenyearradio').on('change', function () {
        $('#reportingNIDyear').prop( "disabled", true).prop("required", false);
        $('#reportingNIDyearsince').prop( "disabled", false).prop("required", true);
        $('#reportingNIDyeartill').prop( "disabled", false).prop("required", true);
    });



});