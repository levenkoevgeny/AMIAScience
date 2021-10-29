$( document ).ready(function() {

    'use strict';

    $("#buttonmakeoutput").on( "click", function() {
        var kindid = $("#scienceworkkind").val();


        if (kindid == 1 || kindid == 2 || kindid == 7 || kindid == 8 || kindid == 12) {

            var s = '';
            s = s + $("#scienseworktitle").val() + '/ ';
            s = s + $("#scienceworkkind option:selected").text() + '/ ';
                $(".authorinput").each(function() {
                    s = s + $(this).val() + ', ';
                });
            s = s + '// ';
            s = s + $("#scienceworkcity option:selected").text() + '/ ';
            s = s + $("#scienceworkpublisher option:selected").text() + '/ ';
            s = s + $("#scienceworkyear").val() + 'г./ ';


        } else if (kindid == 3) {
            var s = makemaindata();

        } else if (kindid == 5 || kindid == 6) {
            var s = makemaindata();

        } else if (kindid == 9) {
            var s = makemaindata();

        } else if (kindid == 10 || kindid == 11) {
            var s = makemaindata();

            s = s + 'Дата проведения форума: ' + getdatestr($("#forumdate").val());
        }


        $("#scienseworkoutputdata").val(s);
    });

    function makemaindata() {
        var d = "";
        d = d + 'Название публикации: ' + $("#scienseworktitle").val() + '; ';
        d = d + 'Вид публикации: ' + $("#scienceworkkind option:selected").text() + '; ';
        d = d + 'Авторы: ';
        $(".authorinput").each(function() {
            d = d + $(this).val() + ' ';
        });
        d = d + '; ';
        d = d + 'Название города, где издана публикация: ' + $("#scienceworkcity option:selected").text() + '; ';
        d = d + 'Год издания: ' + $("#scienceworkyear").val() + '; ';
        d = d + 'Количество страниц: ';
        return d;
    }
    function getdatestr(datestring) {
        var arrayOfStrings = datestring.split('-');
        var months = ['Янв.','Февр.','Март.', 'Апр.', 'Мая', 'Июн.', 'Июл.', 'Авг.', 'Сент.', 'Окт.', 'Нояб.', 'Декаб.'];
        var date = '';
        var date =  date + arrayOfStrings[2] + ' ' + months[arrayOfStrings[1]-1] + ' ' + arrayOfStrings[0];

        return date;
    }

});