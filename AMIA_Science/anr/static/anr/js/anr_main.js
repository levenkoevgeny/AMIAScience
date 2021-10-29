$( document ).ready(function() {
    'use strict';


    $('#publication_id').select2({
        ajax: {
            url: "getallpublajax_select2",
            type: "GET",
            dataType: 'json',
            minimumInputLength: 20,
            data: function (params) {
                var query = {
                    search: params.term,
                }
                return query;
            },
            success: function (data) {
                var dataJSON = JSON.parse(data);
                console.log("SUCCESS: ", dataJSON);
            },
            processResults: function (data) {
                return {
                    results: $.map(JSON.parse(data), function (item) {
                        return {
                            text: item.fields.outputdata,
                            id: item.pk
                        }
                    })
                };
            }
        }
    });

    $('#id_dissertation, #id_nir, #anr_authors, #id_authors').select2();

    inputs_group_make_hidden();
    developmentkind_change();

    if ($("#id_is_student_participation").prop("checked")==true){
        $("#student_block").css('display', 'block');
        $("#id_student").prop('disabled', false).prop('required', true);
    }else {
        $("#student_block").css('display', 'none');
        $("#id_student").prop('disabled', true).prop('required', false);
    }


    if ($("#id_development_has_not_base").prop("checked")==true){
        $('#has_work').css('display', 'none');
        $('#has_not_work').css('display', 'block');
        $('#id_development_without_base').prop('disabled', false).prop('required', true);
        $('#publinput, #id_dissertation, #id_nir').prop('disabled', true).prop('required', false);
    }else {
        $('#has_work').css('display', 'block');
        $('#has_not_work').css('display', 'none');
        $('#id_development_without_base').prop('disabled', true).prop('required', false);
        developmentkind_change();
    }


    $("#id_is_student_participation").on( "click", function() {
        if ($(this).prop("checked")==true){
            $("#student_block").css('display', 'block');
            $("#id_student").prop('disabled', false).prop('required', true);
        }else {
            $("#student_block").css('display', 'none');
            $("#id_student").prop('disabled', true).prop('required', false);
        }

    });

    $("#id_development_has_not_base").on( "click", function() {
        if ($(this).prop("checked")==true){
            $('#has_work').css('display', 'none');
            $('#has_not_work').css('display', 'block');
            $('#id_development_without_base').prop('disabled', false).prop('required', true);
            $('#publinput, #id_dissertation, #id_nir').prop('disabled', true).prop('required', false);
        }else {
            $('#has_work').css('display', 'block');
            $('#has_not_work').css('display', 'none');
            $('#id_development_without_base').prop('disabled', true).prop('required', false);
            developmentkind_change();
        }
    });

    $('#id_developmentkind').on('change', function () {
        developmentkind_change();
    });


    function developmentkind_change() {
        var nir = 1; var sciencework = 2; var disser = 3;
        var divs = $('#other_authors_div, #student_participation_div, #adjunct_div');
        var id = $('#id_developmentkind').val();

        divs.css('display', 'block');
        inputs_group_make_hidden();

        if (id == nir) {
            $('#adjunct_div').css('display', 'none');
            $('#nir_div').css('display', 'block');
            $('#id_nir').prop('disabled', false).prop('required', true);
            $('#id_authors').prop('required', true);
        } else

        if (id == sciencework) {
            $('#adjunct_div').css('display', 'none');
            $('#publication_div').css('display', 'block');
            $('#publinput').prop('disabled', false).prop('required', true);
            $('#id_authors').prop('required', true);
        } else

        if (id == disser) {
            divs.css('display', 'none');
            $('#adjunct_div').css('display', 'none');
            $('#adjunct_div').css('display', 'block');
            $('#dissertations_div').css('display', 'block');
            $('#id_dissertation').prop('disabled', false).prop('required', true);
            $('#id_authors').prop('required', false);
        } else {
            inputs_group_make_hidden();
            divs.css('display', 'none');
        }
    }

    function inputs_group_make_hidden() {
        var inputs_divs = $('#publication_div, #dissertations_div, #nir_div');
        var inputs = $('#publinput, #id_dissertation, #id_nir');
        inputs_divs.css('display', 'none');
        inputs.prop('disabled', true).prop('required', false);
    }

});