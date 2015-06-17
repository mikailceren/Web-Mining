$(function () {
    $('#chart2').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: 'En Yeniler'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.y} tl</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>',
                    style: {
                        color: 'point.color',
                    }
                }
            }
        },
        series: [{
            type: 'pie',
            name: 'Fiyat',
            data: [
                ['İhanetin 5 Yüzü',14.30],
                ['Kızılcık Burnu',14.25],
                {
                    name: 'Yolun Sonu',
                    y: 21,
                    sliced: true,
                    selected: true
                },
                ['Renkler Şehri',10.50],
                ['Yer Sema Gök Semah',9.79],
                ['Hz. İshak',7],
                ['Gerçekten Bilmeniz Gereken 50 Ekonomi Fikri',18.85],
                ['Nikola Tesla Kendini Anlatıyor',6.44],
                ['Kuş Adam',20.65],
                ['Panzehir',14.30],
            ]
        }]
    });
});