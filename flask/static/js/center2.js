var center2 = echarts.init(document.getElementById('center2'), "dark");

var center2_option = {
    title: {
        text: '',
        subtext: '',
        x: 'left'
    },
    tooltip: {
        trigger: 'item'
    },
    //左侧小导航图标
    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        // splitNumber:4,//分段
        // piece:[
        //     //分段
        //     {min:100000},
        //     {min:1000,max:9999},
        //     {min:100,max:999},
        //     {min:10,max:99},
        //     {min:1,max:9}
        // ],
        align:'left',//默认left
        // orient:'horizontal',//横排显示（默认数值）
        //left right 这些属性控制分段位置
        // showLabel:false,
        textStyle: {
            //字体样式
            fontSize: 8,
        },
        // inRange:{
        //     symbol:'circle',
        //     symbol:'rect',
        //     // 默认：rect
        // },
        itemWidth:20,
        itemHeight:10,
        splitList: [{ start: 20000,end: 29999 },
            {start: 30000, end: 39999 },
			{ start: 40000, end: 49999 },
            {  start: 50000, end: 59999 },
            { start: 60000 }],
        color: ['#8A3310', '#C64918', '#E55B25', '#F2AD92', '#F9DCD1']
    },
    //配置属性
    series: [{
        name: '预测二手房价（元/平米）',
        type: 'map', //告诉echarts 要去渲染的是一个地图
        mapType: 'shenzhen', //告诉echarts 要去渲染中国地图
        roam: false, //拖动和缩放
        itemStyle: { //地图板块的颜色和边框
            normal: {
                borderWidth: .5, //区域边框宽度
                borderColor: '#009fe8', //区域边框颜色
                areaColor: "#ffefd5", //区域颜色
            },
            emphasis: {//鼠标滑过地图高亮的相关设置（字体颜色）
                borderWidth: .5,
                borderColor: '#4b0082',
                areaColor: "#fff",
            }
        },
        label: {
            //控制对应地区的汉字
            normal: {
                show: true, //区名称
                fontSize: 8,
            },
            emphasis: { //鼠标滑过地图高亮的相关设置（字体颜色）
                show: true,
                fontSize: 8,
            }
        },
        //zoom:1.5,//
        data: []  //数据
    }]
};


center2.setOption(center2_option);
