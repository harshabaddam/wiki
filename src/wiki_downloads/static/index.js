$(document).ready(function(){
    $("#search_button").on('click', function(){
        $.ajax({
            url: '/search',
            data: {
                'search': $("#search_id").val()
            },
            success: function(data){
                $("#list_id").html(' ');
                $("#no_result").html(' ');
                for(let i=0;i < data['data'].length;i++){
                    $("#list_id").append('<li><a href="/page?title='+data['data'][i]+'">'+data['data'][i]+'</a></li>');
                }
                if(data['data'].length==0){
                    $("#no_result").html('No Results found');
                }
            }
        });
    });
});