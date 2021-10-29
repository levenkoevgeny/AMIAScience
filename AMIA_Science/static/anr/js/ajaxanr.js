$( document ).ready(function() {

    'use strict';

    $("body").on("keyup", "#publinput", function() {

        var searchcur = $(this).val();
        var elemid = $(this).attr('id');
        var elem = $(this);

        setTimeout(function() {
            if (searchcur.length > 10 && searchcur == elem.val()){
                getallpublajax(elemid);
            }
        }, 800);

    });

    $("body").on("click", ".resultwork", function() {

        $("#publinput").val($(this).data("title"));
        $("#workinputhidden").val($(this).data("pk"));
        $("#workkindhidden").val($(this).data("kind"));
        $("#authorsajax").empty();
    });

    function getallpublajax(elemid, choiceid) {

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
        search["publinput"] = $("#" + elemid).val();

        $.ajax({
            url: "/anr/getallpublajax",
            type: "POST",
            dataType: 'json',
            data: search,
            timeout : 100000,
            success: function (data) {
                var dataJSON = JSON.parse(data);
                console.log("SUCCESS: ", dataJSON);
                scienceworkdisplay(dataJSON, choiceid);
            },
            error: function (e) {
                console.log("ERROR: ", e);
            },
            done: function (e) {
                console.log("DONE");
            }
        });
    }

    function scienceworkdisplay(dataJSON, choiceid) {
        $("#authorsajax").empty();
        for (var i = 0; i < dataJSON.length; i++) {
            var newdiv = $('<div/>', {
                class: 'resultwork form-control',
            });
            newdiv.html('<p class="col-12 text-truncate" title="' + dataJSON[i].fields.outputdata + '">' + dataJSON[i].fields.outputdata + '</p>');
            newdiv.data("pk", dataJSON[i].pk);
            newdiv.data("title", dataJSON[i].fields.outputdata);
            newdiv.data("kind", choiceid);
            $("#authorsajax").append(newdiv);
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