var chart1;
$(function () {
    $('#chart1').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: 'Çok Satanlar'
        },
        tooltip: {
            backgroundColor: '#FCFFC5'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: false,
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                },
                showInLegend: true
            }
        },
        series: [{
            type: 'pie',
            name: 'Satış Sayısı',
            data: [
                ['Esrarengiz Bahçe',    6358],
                ['Konstantiniyye',      1829],
                ['Çocuk Neyi Neden Yapar?',      8398],
                ['Gizemli Orman',      447],
                ['Çocuk Eğitiminde 100 Temel Kural',1772],
                ['Ölümsüz Aşk',      5018],
                ['Türklerin Tarihi',      4421],
                ['İçimizdeki Şeytan',      8403],
                ['Öğrendim ki...',      395],
                ['Küçük Prens',      3909],
                
            ]
        }]
    });
});



