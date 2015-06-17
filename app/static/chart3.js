
$(function () {
    $('#chart3').highcharts({
        
        title: {
            text: 'Çok Satanlar'
        },
        tooltip: {
            
            shared: true,
        },
		xAxis: {
            categories: ['Esrarengiz Bahçe','Konstantiniyye','Çocuk Neyi Neden Yapar?','Gizemli Orman','Çocuk Eğitiminde 100 Temel Kural','Ölümsüz Aşk','Türklerin Tarihi','İçimizdeki Şeytan','Öğrendim ki...','Küçük Prens'],
			crosshair: true
        },
		yAxis: [{ // Primary yAxis
            labels: {
                format: '{value}tl',
                style: {
                    color: Highcharts.getOptions().colors[1]
                }
            },
            title: {
                text: 'Fiyat',
                style: {
                    color: Highcharts.getOptions().colors[1]
                }
            },
            opposite: true

        }, { // Secondary yAxis
            gridLineWidth: 0,
            title: {
                text: 'Satış Sayısı',
                style: {
                    color: Highcharts.getOptions().colors[0]
                }
            },
            labels: {
                format: '{value}',
                style: {
                    color: Highcharts.getOptions().colors[0]
                }
            }

        }],
		legend: {
            layout: 'vertical',
            align: 'left',
            x: 80,
            verticalAlign: 'top',
            y: 30,
            floating: true,
            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
        },
		
        plotOptions: {
            series: {
                allowPointSelect: true
            }
        },
        series: [{
            name: 'Satış Sayısı',
            type: 'column',
            yAxis: 1,
            data: [6358,1829,8398,447,1772,5018,4421,8403,395,3909],
            tooltip: {
                valueSuffix: ' adet'
            }

        }, {
            name: 'Fiyat',
            type: 'spline',
            data: [15,20,10.50,15,12.37,13.65,14.62,10.82,11.92,6.93],
            tooltip: {
                valueSuffix: ' tl'
            }
        }]
    });
});


