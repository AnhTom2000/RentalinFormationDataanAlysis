var right1 = echarts.init(document.getElementById('right1'),"dark");

var dataAxis = []

var right1_option = {
	//标题样式
	title : {
	    text : "各区域挂牌数量排行榜",
	    textStyle : {
	        color : 'white',
	    },
	    left : 'left'
	},
	// color: ['#3398DB'],
	tooltip: {
		trigger: 'axis',
		axisPointer: {            // 坐标轴指示器，坐标轴触发有效
			type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
		}
	},
    xAxis: {
		axisLabel: {
                interval:0,//代表显示所有x轴标签显示
                rotate:45, //代表逆时针旋转45度
				inside: false,
				textStyle: {
					color: '#fff'
				}
            },
        type: 'category',
        axisTick: {
            show: false
        },
        axisLine: {
            show: false
        },
        z: 10,
        data: []
    },
    yAxis: {
        type: 'value',
		axisLine: {
            show: false
        },
        axisTick: {
            show: false
        },
        axisLabel: {
            textStyle: {
                color: '#999'
            }
        }
    },
    //区域缩放
	dataZoom: [
        {
            type: 'inside'
        }
    ],
    series: [{
        type: 'bar',
		barMaxWidth:"50%",
		showBackground: true,
		itemStyle: {
                color: new echarts.graphic.LinearGradient(
                    0, 0, 0, 1,
                    [
                        {offset: 0, color: '#83bff6'},
                        {offset: 0.5, color: '#188df0'},
                        {offset: 1, color: '#188df0'}
                    ]
                )
            },
		emphasis: {
                itemStyle: {
                    color: new echarts.graphic.LinearGradient(
                        0, 0, 0, 1,
                        [
                            {offset: 0, color: '#2378f7'},
                            {offset: 0.7, color: '#2378f7'},
                            {offset: 1, color: '#83bff6'}
                        ]
                    )
                }
            },
		data:[]
    }]
};

var zoomSize = 6;
right1.on('click', function (params) {
    // param.dataIndex：数值序列（X轴上当前点是第几个点、console.log() 方法用于在控制台输出信息。

    console.log(dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)]);
    right1.dispatchAction({
        type: 'dataZoom',
        startValue: dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)],
        endValue: dataAxis[Math.min(params.dataIndex + zoomSize / 2, data.length - 1)]
    });
});

right1.setOption(right1_option);
