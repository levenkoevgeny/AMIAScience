$( document ).ready(function() {
    'use strict';

    var set_leader_other = $('#disserleaderlastname, #disserleaderinitials, #disserleaderjob, #academicrank, #academicdegree');
    var set_leader = $('#inputleader');

    $("#thereis").on( "click", function() {
        if ($(this).prop("checked")==true){
            $("#thereisleader").css('display', 'block');
            $("#leaderisemployee").prop("checked", false)
            leaderisemployee();
        }else {
            $("#thereisleader").css('display', 'none');
            set_leader_other.prop('disabled', true).prop('required', false);
            set_leader.prop('disabled', true).prop('required', false);
        }
    });

    $("#leaderisemployee").on( "click", function() {
        if ($(this).prop("checked")==true){
            leaderisnotemployee();
        } else {
            leaderisemployee();
        }
    });

    function leaderisemployee(){
        $('#divfornotleaderemployee').css('display', 'none');
        $('#divforleaderemployee').css('display', 'block');
        set_leader_other.prop('disabled', true).prop('required', false);
        set_leader.prop('disabled', false).prop('required', true);
    }

    function leaderisnotemployee(){
        $('#divfornotleaderemployee').css('display', 'block');
        $('#divforleaderemployee').css('display', 'none');
        set_leader_other.prop('disabled', false).prop('required', true);
        set_leader.prop('disabled', true).prop('required', false);
    }

});