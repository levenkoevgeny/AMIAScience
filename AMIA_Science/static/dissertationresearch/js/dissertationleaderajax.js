$( document ).ready(function() {

    'use strict';

    $("body").on("keyup", ".leaderinput", function() {
        var searchcur = $(this).val();
        var elemid = $(this).attr('id');
        var elem = $(this);

        setTimeout(function() {
            if (searchcur == elem.val()){
                getallauthorsajax(elemid);
            }
        }, 800);
    });

    $("body").on("click", ".leaderrow", function() {
        $("#inputleader").val($(this).data("fio"));
        $("#leaderhidden").val($(this).data("pk" ));
        $("#disabledextrainputleader").val($(this).data("subdivision"));
        $(this).parent().empty();
    });


    function getallauthorsajax(elemid) {

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

        var search = {}
        search["authorlastname"] = $("#" + elemid).val();

        $.ajax({
            url: "/getallauthorsajax",
            type: "POST",
            dataType: 'json',
            data: search,
            timeout : 100000,
            success: function (data) {
                var dataJSON = JSON.parse(data);
                console.log("SUCCESS: ", dataJSON);
                displayauthorsextrarows(dataJSON, elemid);
            },
            error: function (e) {
                console.log("ERROR: ", e);
            },
            done: function (e) {
                console.log("DONE");
            }
        });
    }


    function displayauthorsextrarows(dataJSON, elemid) {
        $("#leaderajax").empty();
        for (var i = 0; i < dataJSON.length; i++) {
            var newdiv = $('<div/>', {
                class: 'leaderrow form-control',
            });
            newdiv.html(dataJSON[i].fields.lastname + ' ' + dataJSON[i].fields.firstname + ' ' + dataJSON[i].fields.patronymic);
            newdiv.data("pk", dataJSON[i].pk);
            var fio = dataJSON[i].fields.lastname + ' ' + (dataJSON[i].fields.firstname).charAt(0) + '.' + (dataJSON[i].fields.patronymic).charAt(0)+ '.';
            newdiv.data("fio", fio);
            newdiv.data("subdivision", dataJSON[i].fields.subdivision);
            $("#leaderajax").append(newdiv);
        }
    }

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