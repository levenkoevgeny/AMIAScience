$( document ).ready(function() {
    'use strict';

    var set_leader_other = $('#disserleaderlastname, #disserleaderinitials, #disserleaderjob, #disserleaderposition, #academicrank, #academicdegree');
    var set_leader = $('#inputleader');

    init();

    function init() {
        if ($("#thereis").prop('checked') == true){
            $("#thereisleader").css('display', 'block');
            if ($("#leaderisemployee").prop('checked') == true) {
                leaderisnotemployee();
            } else {
                leaderisemployee();
            }
        } else {
            $("#thereisleader").css('display', 'none');
            set_leader_other.prop('disabled', true).prop('required', false);
            set_leader.prop('disabled', true).prop('required', false);
        }

    }

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