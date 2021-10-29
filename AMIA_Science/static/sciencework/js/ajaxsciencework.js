$( document ).ready(function() {

    'use strict';

    var authorinputcount;

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


        authorinputcount = 0;
        $(".checkboxextraauthors").each(function() {
            authorinputcount++;
            $(this).attr("id", "checkboxextraauthors" + authorinputcount);
            $(this).attr("name", "checkboxextraauthors" + authorinputcount);
        });

        authorinputcount = 1;
        $(".rowextraauthors").each(function() {
            authorinputcount++;
            $(this).attr("id", "rowextraauthors" + authorinputcount);
         });

        authorinputcount = 1;
        $(".deleteauthorbutton").each(function() {
            authorinputcount++;
            $(this).attr("value", "rowextraauthors" + authorinputcount);
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

    $("body").on("click", ".ajaxrow", function() {

        $(this).parent().siblings(".authorinput").val($(this).data("fio"));
        $(this).parent().siblings(".authoridhidden").val($(this).data("pk" ));
        $(this).parent().parent().parent().parent().siblings(".two").children().children(".disabledextrainput").val($(this).data("subdivision" ));
        $(this).parent().empty();

    });

    function addrowforauthors(){

        authorinputcount = 0;
        $(".inputbutton").each(function() {
            authorinputcount = authorinputcount+1;
       });
        authorinputcount++;

        var newdiv = $('<div id="rowextraauthors' + authorinputcount + '" class="rowextraauthors"><br>\n' +
            '    <div class="row">\n' +
            '        <div class="col-sm-6 col-md-6 col-lg-6 col-xl-6">\n' +
            '            <div class="row">\n' +
            '                <div class="col-sm-2 col-md-2 col-lg-2 col-xl-2 d-flex align-items-center">\n' +
            '                    <div class="d-flex align-items-center">\n' +
            '                        <label>Автор</label>&emsp;\n' +
            '                        <input type="checkbox" name="checkboxextraauthors' + authorinputcount + '" id="checkboxextraauthors' + authorinputcount + '" class="checkboxextraauthors">\n' +
            '                    </div>\n' +
            '                </div>\n' +
            '                <div class="col-sm-10 col-md-10 col-lg-10 col-xl-10">\n' +
            '                    <input type="text" class="form-control authorinput" name="inputauthors' + authorinputcount + '" id="inputauthors' + authorinputcount + '" placeholder="Начните вводить фамилию..." required>\n' +
            '                <input type="hidden" id="authoridhidden' + authorinputcount + '" name="authoridhidden' + authorinputcount + '" class="authoridhidden">\n' +
            '                    <div class="invalid-feedback">\n' +
            '                        Заполните поле!\n' +
            '                    </div>\n' +
            '                    <div class="divforajax"></div>\n' +
            '                </div>\n' +
            '            </div>\n' +
            '        </div>\n' +
            '        <div class="col-sm-6 col-md-6 col-lg-6 col-xl-6 two">\n' +
            '            <div class="d-flex align-items-center flex-row justify-content-between">\n' +
            '                <input type="text" disabled class="form-control disabledextrainput" style="width: 90%;">\n' +
            '                <button type="button" id="scienceworkdeleteauthor" value="rowextraauthors' + authorinputcount + '" class="btn btn-outline-danger deleteauthorbutton inputbutton">--</button>\n' +
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
        search["idarray"] = [];

        $(".authoridhidden").each(function() {
            var attr = $(this).attr('value');

            if (typeof attr !== typeof undefined && attr !== false) {
                search["idarray"].push($(this).val());
            }
        });

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

        $("#"+elemid).siblings(".divforajax").empty();

        for (var i = 0; i < dataJSON.length; i++) {
            var newdiv = $('<div/>', {
                class: 'ajaxrow form-control',
            });
            newdiv.html(dataJSON[i].fields.lastname + ' ' + dataJSON[i].fields.firstname + ' ' + dataJSON[i].fields.patronymic);
            newdiv.data("pk", dataJSON[i].pk);
            var fio = dataJSON[i].fields.lastname + ' ' + (dataJSON[i].fields.firstname).charAt(0) + '.' + (dataJSON[i].fields.patronymic).charAt(0)+ '.';
            newdiv.data("fio", fio);
            newdiv.data("subdivision", dataJSON[i].fields.subdivision);
            $("#"+elemid).siblings(".divforajax").append(newdiv);
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