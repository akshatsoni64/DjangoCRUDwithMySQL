function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function(){
    // console.log("Jquery Working Fine Sir!");

    // $("#editStudent").on('submit','form',function(e){
    $("#editStudent").click(function(){
        alert("Updating"+this.id);
        var cookies = document.cookie.split(";");
        var cookie = cookies[0].split("=")
        // console.log("Cookie"+cookie[1]);

        var formdata = new FormData($("#addStudent")[0]);

        $.ajax({
            url:'insert/'+cookie[1],
            type:'POST',
            processData: false,
            cache: false,
            contentType: false,
            data:formdata,
            success:function(data){
                // console.log(data);
                alert("Updated");
                $("#addStudent").trigger("reset");
                window.location.href="http://localhost:8000/index";
                $("#submitStudent").css("display","block");
                $("#editStudent").css("display","none");
            }
        });
    });

    $("#addStudent").submit(function(e){
         e.preventDefault();
        var formdata = new FormData(this);
        // for(var pair of formData.entries()) {
        //    console.log(pair[0]+ ', '+ pair[1]);
        // }
        $.ajax({
            url:'insert/',
            type:'POST',
            processData: false,
            cache: false,
            contentType: false,
            data:formdata,
            success:function(data){
                // console.log(data);
                // alert("Inserted");
                $("#addStudent").trigger("reset");
                window.location.href="http://localhost:8000/index";
            }
        });
    });

    $(".editStudent").on('click',function(){
        console.log("Edit Request");
        var sid = this.id.substr(8,9);
        document.cookie="sid="+sid;
        // console.log(sid);
        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie('csrftoken') }
        });
        $.ajax({
            url: 'insert/'+sid,
            type: 'PUT',
            success: function(data){
                // console.log("Editing");
                // console.log(data)
                $("#nameStudent").val(data['name']);
                $("#branchStudent").val(data['branch']);
                $("#enoStudent").val(data['eno']);
                $("#submitStudent").css("display","none");
                $("#editStudent").css("display","block");
            }
        });

    });

    $(".deleteStudent").on('click',function(){
        // console.log("Delete Request");
        var formdata = new FormData($("#addStudent")[0]);
        var sid = this.id.substr(8,9);
        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie('csrftoken') }
        });
        $.ajax({
            url: 'delete/'+sid,
            type: 'DELETE',
            processData: false,
            cache: false,
            contentType: false,
            data:formdata,
            success: function(data){
                // console.log("Deleted");
                window.location.href="http://localhost:8000/index";
            }
        });
    });
});