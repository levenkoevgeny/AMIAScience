$( document ).ready(function() {

    'use strict';
    var authorinputcount = 1;

    $("#scienceworkaddauthor").on( "click", function() {
        addrowforauthors();
    });


    $("body").on("click", ".deleteauthorbutton", function(e) {

        var btn = e.target;
        var idval = btn.value;
        $("#" + idval).remove();


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

        $("#authorscount").attr('value', authorinputcount);

    });

    $("body").on("keyup", ".authorinput", function() {

        var searchcur = $(this).val();
        var elemid = $(this).attr('id');
        var elem = $(this);

        setTimeout(function() {
            if (searchcur == elem.val()){
                getallauthorsajax(elemid);
            }
        }, 800);

    });

    $("body").on("click", ".resultauthors", function() {

        $(this).parent().siblings(".authorinput").val($(this).data("lastname" ));
        $(this).parent().siblings(".authoridhidden").val($(this).data("pk" ));
        $(this).parent().parent().siblings(".two").children().children(".disabledextrainput").val($(this).data("subdivision" ));
        $(this).parent().empty();

    });

    function addrowforauthors(){

        authorinputcount++;
        var newdiv = $('<div id="rowextraauthors' + authorinputcount + '" class="rowextraauthors"><br>\n' +
            '    <div class="row">\n' +
            '        <div class="col-sm-6 col-md-6 col-lg-6 col-xl-6">\n' +
            '                <input type="text" class="form-control authorinput" name="inputauthors' + authorinputcount + '" id="inputauthors' + authorinputcount + '" placeholder="Начните вводить фамилию..." required>\n' +
            '                <input type="hidden" id="authoridhidden' + authorinputcount + '" name="authoridhidden' + authorinputcount + '" class="authoridhidden">\n' +
            '                <div class="authorsajax"></div>\n' +
            '                <div class="invalid-feedback">\n' +
            '                    Это поле является обязательным для заполнения!\n' +
            '                </div>\n' +
            '        </div>\n' +
            '        <div class="col-sm-6 col-md-6 col-lg-6 col-xl-6 two">\n' +
            '            <div class="d-flex align-items-center flex-row justify-content-between">\n' +
            '                <input type="text" disabled class="form-control disabledextrainput" style="width: 90%;">\n' +
            '                <button type="button" id="scienceworkdeleteauthor" value="rowextraauthors' + authorinputcount + '" class="btn btn-outline-danger deleteauthorbutton">--</button>\n' +
            '            </div>\n' +
            '        </div>\n' +
            '    </div>\n' +
            '</div>');

        $("#extraauthors").append(newdiv);
        $("#authorscount").attr('value', authorinputcount);
    }

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
            url: "getallauthorsajax",
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

        $("#"+elemid).siblings(".authorsajax").empty();

        for (var i = 0; i < dataJSON.length; i++) {
            var newdiv = $('<div/>', {
                class: 'resultauthors form-control',
            });
            newdiv.html(dataJSON[i].fields.lastname + ' ' + dataJSON[i].fields.firstname + ' ' + dataJSON[i].fields.patronymic);
            newdiv.data("pk", dataJSON[i].pk);
            newdiv.data("lastname", dataJSON[i].fields.lastname);
            newdiv.data("subdivision", dataJSON[i].fields.subdivision);
            $("#"+elemid).siblings(".authorsajax").append(newdiv);
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

