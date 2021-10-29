var monograf = 1; var uchebnik = 2; var uchebn_izd = 3;
var praktich_posob = 5; var metodich_razrab = 6; var spravochn_izdan = 7;
var kommentarij_zakon = 8; var nauchn_stat = 9;
var mater_konf = 10; var tezis_doklad = 11; var inaja_publ = 12;

function init_page(){
    $('.extra_divs').css('display', 'none');
    $('.extra_inputs').prop("disabled", true).prop("required", false);
}

function init_fields(id){
    if (id==monograf || id==uchebnik || id==spravochn_izdan || id==kommentarij_zakon || id==inaja_publ){
        $('#publ').css('display', 'block');
        $('#id_publisher').prop("disabled", false).prop("required", true);
    } else if (id == uchebn_izd) {
        $('#publ, #grif, #subspecies').css('display', 'block');
        $('#id_publisher, #id_subspecies').prop("disabled", false).prop("required", true);
    } else if (id == praktich_posob || id==metodich_razrab) {
        $('#publ, #interest').css('display', 'block');
        $('#id_publisher, #id_interest').prop("disabled", false).prop("required", true);
    } else if (id == nauchn_stat) {
        $('#publ, #checkmagaz, #sciencework_student_participation, #forum_result').css('display', 'block');
        $('#id_publisher, #id_magazine').prop("disabled", false).prop("required", true);
    } else if (id == mater_konf || id == tezis_doklad) {
        $('#konfer, #statusforum, #kindforum, #organizatorforum, #country, #forum_date, #kindforum, #sciencework_student_participation').css('display', 'block');
        $('#id_conference, #id_forumstatus, #id_kindforum, #id_organizatorforum, #id_forumcountry, #id_forumdate, #id_kindforum').prop("disabled", false).prop("required", true);
    } else {
        init_page();
    }
}

$( document ).ready(function() {
    'use strict';

    init_page();


    $( "#id_workisforeignauthors").on( "click", function() {
        if ($(this).prop("checked")==true){
            $("#scienceworkforeignauthorscount").prop( "disabled", false);
        } else {
            $("#scienceworkforeignauthorscount").prop( "disabled", true);
        }
    });

    $('#magazinekindradio').on('change', function () {
        $("#id_magazine").prop( "disabled", false).prop("required", true);
        $("#id_digest").prop( "disabled", true).prop("required", false);
    });

    $('#digestkindradio').on('change', function () {
        $("#id_magazine").prop( "disabled", true).prop("required", false);
        $("#id_digest").prop( "disabled", false).prop("required", true);
    });

    $('#id_kind').on('change', function () {
        var id = $(this).val();
        init_page();
        init_fields(id);
    });

    $("#id_is_forum_result").on( "click", function() {
        if ($(this).prop("checked")==true){
            $('#konfer, #forum_date, #statusforum, #kindforum').css('display', 'block');
            $('#id_conference, #id_forumdate, #id_forumstatus, #id_kindforum').prop("disabled", false).prop("required", true);
        } else {
            $('#konfer, #forum_date, #statusforum, #kindforum').css('display', 'none');
            $('#id_conference, #id_forumdate, #id_forumstatus, #id_kindforum').prop("disabled", true).prop("required", false);
        }
    });


    $("#id_grif_check").on( "click", function() {
        if ($(this).prop("checked")==true){
            $('#id_grif').prop("disabled", false).prop("required", true);
        } else {
            $('#id_grif').prop("disabled", true).prop("required", false);
        }
    });



});