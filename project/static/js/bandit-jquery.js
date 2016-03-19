$(document).ready(function() {

        $('#make_gig_request').click(function(){
            var evid;
            var bandid;
            evid = $(this).attr("data-evid");
            bandid = $(this).attr("data-bandid");
            $.get('/bandit/make_gig_request/', {event_id: evid, band_id: bandid}, function(data){
                       $('#gig_request_sent').html(data);
                       $('#make_gig_request').hide();
            });
        });

        $('#accept_gig_request').click(function(){
            var evid;
            var bandid;
            evid = $(this).attr("data-evid");
            bandid = $(this).attr("data-bandid");
            $.get('/bandit/accept_gig_request/', {event_id: evid, band_id: bandid}, function(data){
                       $('#gig_request_accepted').html(data);
                       $('#accept_gig_request').hide();
            });
        });


});