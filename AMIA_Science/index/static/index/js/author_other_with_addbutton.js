$( document ).ready(function() {
    'use strict';
    var authorinputcount;
    $( "#otherauthorscheckpld").on( "click", function() {
        if ($(this).prop("checked")==true){

            $(".authorinputotherlastname").each(function() {
                $(this).prop( "disabled", false);
            });

            $(".authorinputotherpatronymic").each(function() {
                $(this).prop( "disabled", false);
            });

            $(".deleteauthorbuttonother").each(function() {
                $(this).prop( "disabled", false);
            });

            $("#scienceworkaddauthorother").prop( "disabled", false);

        } else {
            $(".authorinputotherlastname").each(function() {

                $(this).prop( "disabled", true);
            });

            $(".authorinputotherpatronymic").each(function() {
                $(this).prop( "disabled", true);
            });

            $(".deleteauthorbuttonother").each(function() {
                $(this).prop( "disabled", true);
            });

            $("#scienceworkaddauthorother").prop( "disabled", true);

        }
    });

    $("#scienceworkaddauthorother").on( "click", function() {
        addrowforauthors();
    });

    function addrowforauthors(){

        authorinputcount = 0;
        $(".inputbuttonother").each(function() {
            authorinputcount = authorinputcount+1;
        });
        authorinputcount++;

        var newdiv = $('<div id="rowextraauthorsother' + authorinputcount + '" class="rowextraauthorsother"><br>\n' +
            '                                        <div class="row">\n' +
            '                                            <div class="col-sm-4 col-md-4 col-lg-4 col-xl-4">\n' +
            '                                                <label>Фамилия</label>\n' +
            '                                                <input type="text" class="form-control authorinputotherlastname" name="inputauthorsotherlastname' + authorinputcount + '" id="inputauthorsotherlastname' + authorinputcount + '" placeholder="Введите фамилию" style="width: 80%;" required>\n' +
            '                                            </div>\n' +
            '                                            <div class="col-sm-4 col-md-4 col-lg-4 col-xl-4">\n' +
            '                                                <label>Инициалы</label>\n' +
            '                                                <div class="d-flex flex-row align-items-center justify-content-between">\n' +
            '                                                    <input type="text" class="form-control authorinputotherpatronymic" name="inputauthorsotherpatronymic' + authorinputcount + '" id="inputauthorsotherpatronymic' + authorinputcount + '" placeholder="Введите инициалы" style="width: 80%;" required>\n' +
            '                                                    <button type="button" id="scienceworkdeleteauthorother" value="rowextraauthorsother' + authorinputcount + '" class="btn btn-outline-danger deleteauthorbuttonother inputbuttonother">--</button>\n' +
            '                                                </div>\n' +
            '                                            </div>\n' +
            '                                        </div>\n' +
            '                                    </div>')

        $("#extraauthorsother").append(newdiv);
        $("#authorscountother").attr('value', authorinputcount);
    }

    $("body").on("click", ".deleteauthorbuttonother", function(e) {

        var btn = e.target;
        var idval = btn.value;
        $("#" + idval).remove();

        authorinputcount = 0;
        $(".authorinputotherlastname").each(function() {
            authorinputcount++;
            $(this).attr("id", "inputauthorsotherlastname" + authorinputcount);
            $(this).attr("name", "inputauthorsotherlastname" + authorinputcount);
        });

        authorinputcount = 0;
        $(".authorinputotherpatronymic").each(function() {
            authorinputcount++;
            $(this).attr("id", "inputauthorsotherpatronymic" + authorinputcount);
            $(this).attr("name", "inputauthorsotherpatronymic" + authorinputcount);
        });

        authorinputcount = 1;
        $(".rowextraauthorsother").each(function() {
            authorinputcount++;
            $(this).attr("id", "rowextraauthorsother" + authorinputcount);
        });

        authorinputcount = 1;
        $(".deleteauthorbuttonother").each(function() {
            authorinputcount++;
            $(this).attr("value", "rowextraauthorsother" + authorinputcount);
        });

        $("#authorscountother").attr('value', authorinputcount);

    });
});