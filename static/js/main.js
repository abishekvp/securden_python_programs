
document.getElementById("clear_db").addEventListener("click", function(e){
    if(confirm("Are you sure you want to clear the DB?")){
        e.preventDefault();
        $.ajax({
            type:'POST',
            url:'/clear-db',
            data:{
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function(response){
                location.href = "/";
            }
        });
    }
});

document.getElementById("initiate").addEventListener("click", function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:'/total-taxi',
        data:{
            total_taxi:$('#total_taxi').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(response){
            alert(response['total_taxi']+" Taxi Initiated");
            location.href = "/";
        },
    });
});



document.getElementById("book_taxi").addEventListener("click", function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:'/book-taxi',
        data:{
            customer_id:$('#customer_id').val(),
            pickup_point:$('#pickup_point').val(),
            drop_point:$('#drop_point').val(),
            pickup_time:$('#pickup_time').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(response){
            if(response['taxi_id']==0){
                alert("No Taxi Available");
            }
            else{alert("Taxi "+response['taxi_id']+" Booked for Customer ID: "+response['customer_id']);}
            BookingData();
        }
    });
});


// for getting the taxi count
function GetTaxiCount() {
    document.getElementById("taxi_id").innerHTML = "";
    $.ajax({
        type:'POST',
        url:'/get-taxi-count',
        data:{
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(response){
            $('#taxi_id').append($('<option>',{value: "all",text : "All Taxi" }));
            for (i=1;i<=response;i++){ 
                $('#taxi_id').append($('<option>',{value: i,text : "Taxi "+i }));
            }
        }
    });
}
// ends for getting the taxi count

function SelectedTaxi(taxi_id){
    document.getElementById("booking-data").innerHTML = "";
    $.ajax({
        type:'POST',
        url:'/selectedtaxi',
        data:{
            taxi_id:taxi_id,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(RawData){
            var total_pay = 0;
            for (i=0;i<RawData.total_booking;i++){
                setTimeout(function(i) {
                    $('#booking-data').append(
                        $('<tr>'+
                            '<td>'+(i+1)+'</td>'+
                            '<td>Taxi '+RawData.booking[i][0]+'</td>'+
                            '<td>'+RawData.booking[i][1]+'</td>'+
                            '<td>'+RawData.booking[i][2]+'</td>'+
                            '<td>'+RawData.booking[i][3]+'</td>'+
                            '<td>'+RawData.booking[i][4]+'</td>'+
                            '<td>'+RawData.booking[i][5]+'</td>'+
                            '<td>Rs:'+RawData.booking[i][6]+'.00/-</td>'+
                        '</tr>'));
                    total_pay += parseInt(RawData.booking[i][6]);
                    $("#totalsum").html("Total Amount: Rs:"+total_pay+".00/-");
                }, 100*i,i);
            }
        }
    });
}

function SearchBookingData(data){
    if (data==""){BookingData();return;}
    document.getElementById("booking-data").innerHTML = "";
    $.ajax({
        type:'POST',
        url:'/get-sorted-booking-data',
        data:{
            search:data,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(RawData){
            var total_pay = 0;
            for (i=0;i<RawData.total_booking;i++){
                setTimeout(function(i) {
                    $('#booking-data').append(
                        $('<tr>'+
                            '<td>'+(i+1)+'</td>'+
                            '<td>Taxi '+RawData.booking[i][0]+'</td>'+
                            '<td>'+RawData.booking[i][1]+'</td>'+
                            '<td>'+RawData.booking[i][2]+'</td>'+
                            '<td>'+RawData.booking[i][3]+'</td>'+
                            '<td>'+RawData.booking[i][4]+'</td>'+
                            '<td>'+RawData.booking[i][5]+'</td>'+
                            '<td>Rs:'+RawData.booking[i][6]+'.00/-</td>'+
                        '</tr>'));
                    total_pay += parseInt(RawData.booking[i][6]);
                    $("#totalsum").html("Total Amount: Rs:"+total_pay+".00/-");
                }, 100*i,i);
            }
        }
    });
}

function SortedBookingData(){
    document.getElementById("booking-data").innerHTML = "";
    $.ajax({
        type:'POST',
        url:'/get-sorted-booking-data',
        data:{
            search:1,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(RawData){
            var total_pay = 0;
            for (i=0;i<RawData.total_booking;i++){
                setTimeout(function(i) {
                    $('#booking-data').append(
                        $('<tr>'+
                            '<td>'+(i+1)+'</td>'+
                            '<td>Taxi '+RawData.booking[i][0]+'</td>'+
                            '<td>'+RawData.booking[i][1]+'</td>'+
                            '<td>'+RawData.booking[i][2]+'</td>'+
                            '<td>'+RawData.booking[i][3]+'</td>'+
                            '<td>'+RawData.booking[i][4]+'</td>'+
                            '<td>'+RawData.booking[i][5]+'</td>'+
                            '<td>Rs:'+RawData.booking[i][6]+'.00/-</td>'+
                        '</tr>'));
                    total_pay += parseInt(RawData.booking[i][6]);
                    $("#totalsum").html("Total Amount: Rs:"+total_pay+".00/-");
                }, 100*i,i);
            }
        }
    });
}

function BookingData(){
    document.getElementById("booking-data").innerHTML = "";
    $.ajax({
        type:'POST',
        url:'/get-booking-data',
        data:{
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(RawData){
            var total_pay = 0;
            for (i=0;i<RawData.total_booking;i++){
                setTimeout(function(i) {
                    $('#booking-data').append(
                        $('<tr>'+
                            '<td>'+(i+1)+'</td>'+
                            '<td>Taxi '+RawData.booking[i][0]+'</td>'+
                            '<td>'+RawData.booking[i][1]+'</td>'+
                            '<td>'+RawData.booking[i][2]+'</td>'+
                            '<td>'+RawData.booking[i][3]+'</td>'+
                            '<td>'+RawData.booking[i][4]+'</td>'+
                            '<td>'+RawData.booking[i][5]+'</td>'+
                            '<td>Rs:'+RawData.booking[i][6]+'.00/-</td>'+
                        '</tr>'));
                    total_pay += parseInt(RawData.booking[i][6]);
                    $("#totalsum").html("Total Amount: Rs:"+total_pay+".00/-");
                }, 100*i,i);
        }
    }});
}

function OnLoadCall(){
    BookingData();
    GetTaxiCount();
}


function bruteforce_test(){
    $.ajax({
        type:'POST',
        url:'/bruteforce_testing',
        data:{
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(response){
            location.href = "/";
        }
    });
}
