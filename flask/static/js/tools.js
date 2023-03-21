function get_time() {
    $.ajax({
        url: "/time",
        // type:'post',
        timeout: 10000,//超时时间设置为10秒
        success: function (data) {
            $("#time").html(data)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}

function get_center1_data() {
    $.ajax({
        url: "/center1",
        //type:'get',
        success: function (data) {
            $(".num h1").eq(0).text(data.res);
            $(".num h1").eq(1).text(data.avg);
            $(".num h1").eq(2).text(data.min);
            $(".num h1").eq(3).text(data.area);
        },
        error: function (xhr, type, errorThrown) {

        }
    })

}

function get_center2_data() {
    $.ajax({
        url: "/center2",
        success: function (data) {
            center2_option.series[0].data = data.data;
            center2.setOption(center2_option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })

}

function get_left1_data() {
    $.ajax({
        url: "/left1",
        success: function (data) {
            left1_Option.xAxis[0].data = data.day;
            left1_Option.series[0].data = data.avg;
            left1.setOption(left1_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}

function get_left2_data() {
    $.ajax({
        url: "/left2",
        success: function (data) {
            left2_Option.xAxis[0].data = data.day;
            left2_Option.series[0].data = data.avg;
            left2.setOption(left2_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}

function get_left3_data() {
    $.ajax({
        url: "/left3",
        success: function (data) {
            left3_Option.series[0].data = data.data;
            left3.setOption(left3_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}

function get_right1_data() {
    // $.ajax({
    //     url: "/right1",
    //     success: function (data) {
    //         dataAxis = data.area;
    //         right1_option.xAxis.data = data.area;
    //         right1_option.series[0].data = data.count;
    //         right1.setOption(right1_option);
    //     }
    // })
}

function get_right2_data() {
    right2_option.series[0].data = [{"name": '平层', "value": "654"}, {"name": '平层', "value": "654"}, {
        "name": '平层',
        "value": "654"
    }, {"name": '平层', "value": "654"}, {"name": '平层', "value": "654"}, {"name": '平层', "value": "654"}];
    right2.setOption(right2_option);
}


get_time();
get_center1_data();
get_center2_data();
get_left1_data();
get_left2_data();
get_left3_data();
get_right1_data();
get_right2_data();


setInterval(get_time, 1000);
setInterval(get_center1_data, 1000 * 10);
setInterval(get_center2_data, 1000);
setInterval(get_left1_data, 1000 * 10);
setInterval(get_left2_data, 1000 * 10);
setInterval(get_left3_data, 1000 * 10);
setInterval(get_right1_data, 1000 * 10);
setInterval(get_right2_data, 1000);
