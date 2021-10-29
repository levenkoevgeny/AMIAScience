$( document ).ready(function() {

    'use strict'

    $( "#employeedocentcheck").on( "click", function() {
        if ($(this).prop("checked")==true){
            $("#employeedocentdate").prop( "disabled", false);
        } else {
            $("#employeedocentdate").prop( "disabled", true);
        }
    });

    $( "#employeeprofessorcheck").on( "click", function() {
        if ($(this).prop("checked")==true){
            $("#employeeprofessordate").prop( "disabled", false);
        } else {
            $("#employeeprofessordate").prop( "disabled", true);
        }
    });

    $( "#employeecandidatecheck").on( "click", function() {
        if ($(this).prop("checked")==true){
            $("#employeecandidatedate").prop( "disabled", false);
            $("#employeecandidatetitle").prop( "disabled", false);
            $("#employeecandidatespecialty").prop( "disabled", false);
        } else {
            $("#employeecandidatedate").prop( "disabled", true);
            $("#employeecandidatetitle").prop( "disabled", true);
            $("#employeecandidatespecialty").prop( "disabled", true);
        }
    });

    $( "#employeedoctorcheck").on( "click", function() {
        if ($(this).prop("checked")==true){
            $("#employeedoctordate").prop( "disabled", false);
            $("#employeedoctortitle").prop( "disabled", false);
            $("#employeedoctorspecialty").prop( "disabled", false);
        } else {
            $("#employeedoctordate").prop( "disabled", true);
            $("#employeedoctortitle").prop( "disabled", true);
            $("#employeedoctorspecialty").prop( "disabled", true);
        }
    });

    $( "#scienceworkforeignauthors").on( "click", function() {
        if ($(this).prop("checked")==true){
            $("#scienceworkforeignauthorscount").prop( "disabled", false);
        } else {
            $("#scienceworkforeignauthorscount").prop( "disabled", true);
        }
    });

    $( "#dateofbirth").on( "blur", function() {


        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });


        var search = {};
        search["authorlastname"] = $("#lastname").val();
        search["dateofbirth"] = $("#dateofbirth").val();

        $.ajax({
            url: "getallauthorsajaxforcheck",
            type: "POST",
            dataType: 'json',
            data: search,
            timeout : 100000,
            success: function (data) {
                var dataJSON = JSON.parse(data);
                console.log("SUCCESS: ", dataJSON);
                if (dataJSON.length>0){
                    alert('В базе имеется совпадение!')
                }

            },
            error: function (e) {
                console.log("ERROR: ", e);
            },
            done: function (e) {
                console.log("DONE");
            }
        });
    });


    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


});




















