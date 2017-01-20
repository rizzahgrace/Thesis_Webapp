<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Weather Station - Faura Hall</title>

    <!-- Bootstrap Core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/small-business.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
    <!-- amCharts javascript sources -->
		<script type="text/javascript" src="https://www.amcharts.com/lib/3/amcharts.js"></script>
		<script type="text/javascript" src="https://www.amcharts.com/lib/3/serial.js"></script>


		<!-- amCharts javascript code -->
		<script type="text/javascript">
			AmCharts.makeChart("chartdiv",
				{
					"type": "serial",
					"categoryField": "date",
					"dataDateFormat": "YYYY-MM-DD HH",
					"categoryAxis": {
						"minPeriod": "hh",
						"parseDates": true
					},
					"chartCursor": {
						"enabled": true,
						"categoryBalloonDateFormat": "JJ:NN"
					},
					"chartScrollbar": {
						"enabled": true
					},
					"trendLines": [],
					"graphs": [
						{
							"id": "AmGraph-4",
							"tabIndex": 2,
							"title": "Temperature(Celsius)",
							"valueField": "Temperature (Celsius)"
						},
						{
							"id": "AmGraph-5",
							"title": "Rainfall (mm/h)",
							"valueField": "Rainfall (mm/hour)"
						},
						{
							"id": "AmGraph-6",
							"title": "Wind Speed (kph)",
							"valueField": "Wind Speed (KPH)"
						},
						{
							"id": "AmGraph-7",
							"title": "Humidity (%)",
							"valueField": "Humidity (%)"
						}
					],
					"guides": [],
					"valueAxes": [
						{
							"id": "ValueAxis-1",
							"title": "="
						}
					],
					"allLabels": [],
					"balloon": {},
					"legend": {
						"enabled": true,
						"useGraphSettings": true
					},
					"titles": [
						{
							"id": "Title-1",
							"size": 15,
							"text": "Weather Data - Faura Hall"
						}
					],
					"dataProvider": [
						{
							"date": "2014-03-01 08",
							"Temperature (Celsius)": "29.5",
							"Rainfall (mm/hour)": "0",
							"Wind Speed (KPH)": 7,
							"Humidity (%)": 51
						},
						{
							"date": "2014-03-01 09",
							"Temperature (Celsius)": "29.4",
							"Rainfall (mm/hour)": "0",
							"Wind Speed (KPH)": 8,
							"Humidity (%)": 26
						},
						{
							"date": "2014-03-01 10",
							"Temperature (Celsius)": "29.2",
							"Rainfall (mm/hour)": "0.10",
							"Wind Speed (KPH)": 10,
							"Humidity (%)": 43
						},
						{
							"date": "2014-03-01 11",
							"Temperature (Celsius)": "29.5",
							"Rainfall (mm/hour)": "0.15",
							"Wind Speed (KPH)": 10,
							"Humidity (%)": 35
						},
						{
							"date": "2014-03-01 12",
							"Temperature (Celsius)": "29.6",
							"Rainfall (mm/hour)": "0.25",
							"Wind Speed (KPH)": 10,
							"Humidity (%)": 42
						},
						{
							"date": "2014-03-01 13",
							"Temperature (Celsius)": "29.8",
							"Rainfall (mm/hour)": "1",
							"Wind Speed (KPH)": 7,
							"Humidity (%)": 44
						},
						{
							"date": "2014-03-01 14",
							"Temperature (Celsius)": 30,
							"Rainfall (mm/hour)": "1.5",
							"Wind Speed (KPH)": 9,
							"Humidity (%)": 35
						}
					]
				}
			);
		</script>

</head>

<body>

 <center> <img src = header.png alt = "" align = "center"></center>
    <!-- Page Content -->
    <div class="container">

        <!-- Heading Row -->
        <div class="row">
            <div class="col-md-8">

                	<div id="chartdiv" style="width: 100%; height: 400px; background-color: #FFFFFF;" ></div>
            </div>
            <!-- /.col-md-8 -->
            <div class="col-md-4">
              <br><br><br>
                <h1><i>Weather Now</i></h1>

                <p>This website aims to provide the current weather data provided by the weather station installed in the Faura Hall rooftop. This will provide data such as rainfall, wind speed, wind direction, humidity, and temperature.
                Here is some more filler text just because okay then. Well let's add more. The quick brown fox jumps over the lazy dog. </p>

                <?php echo date("D M d, Y G:i a"); ?>
                <br>
                <br>


            </div>
            <!-- /.col-md-4 -->
        </div>
        <!-- /.row -->

        <hr>

        <!-- Call to Action Well -->
        <div class="row">
            <div class="col-lg-12">
                <div class="well text-center">
Comparison with other weather data collection websites and forecasts              </div>
            </div>
            <!-- /.col-lg-12 -->
        </div>
        <!-- /.row -->

        <!-- Content Row -->
        <div class="row">
            <div class="col-md-4">
              <h2><center>Booked.net Weather </h2>
<!-- weather widget start --><div id="m-booked-weather-bl250-32894"> <a href="//www.booked.net/weather/quezon-city-5546" class="booked-wzs-250-175" style="background-color:#137AE9;"> <div class="booked-wzs-250-175-data wrz-18"> <div class="booked-wzs-250-175-right"> <div class="booked-wzs-day-deck"> <div class="booked-wzs-day-val"> <div class="booked-wzs-day-number"><span class="plus">+</span>31</div> <div class="booked-wzs-day-dergee"> <div class="booked-wzs-day-dergee-val">&deg;</div> <div class="booked-wzs-day-dergee-name">C</div> </div> </div> <div class="booked-wzs-day"> <div class="booked-wzs-day-d">H: <span class="plus">+</span>32&deg;</div> <div class="booked-wzs-day-n">L: <span class="plus">+</span>25&deg;</div> </div> </div> <div class="booked-wzs-250-175-city smolest">Quezon City</div> <div class="booked-wzs-250-175-date">Tuesday, 06 December</div> <div class="booked-wzs-left"> <span class="booked-wzs-bottom-l">See 7-Day Forecast</span> </div> </div> </div> <table cellpadding="0" cellspacing="0" class="booked-wzs-table-250"> <tr> <td>Wed</td> <td>Thu</td> <td>Fri</td> <td>Sat</td> <td>Sun</td> <td>Mon</td> </tr> <tr> <td class="week-day-ico"><div class="wrz-sml wrzs-18"></div></td> <td class="week-day-ico"><div class="wrz-sml wrzs-18"></div></td> <td class="week-day-ico"><div class="wrz-sml wrzs-18"></div></td> <td class="week-day-ico"><div class="wrz-sml wrzs-18"></div></td> <td class="week-day-ico"><div class="wrz-sml wrzs-18"></div></td> <td class="week-day-ico"><div class="wrz-sml wrzs-18"></div></td> </tr> <tr> <td class="week-day-val"><span class="plus">+</span>23&deg;</td> <td class="week-day-val"><span class="plus">+</span>24&deg;</td> <td class="week-day-val"><span class="plus">+</span>28&deg;</td> <td class="week-day-val"><span class="plus">+</span>27&deg;</td> <td class="week-day-val"><span class="plus">+</span>27&deg;</td> <td class="week-day-val"><span class="plus">+</span>27&deg;</td> </tr> <tr> <td class="week-day-val"><span class="plus">+</span>22&deg;</td> <td class="week-day-val"><span class="plus">+</span>23&deg;</td> <td class="week-day-val"><span class="plus">+</span>23&deg;</td> <td class="week-day-val"><span class="plus">+</span>23&deg;</td> <td class="week-day-val"><span class="plus">+</span>22&deg;</td> <td class="week-day-val"><span class="plus">+</span>23&deg;</td> </tr> </table> </a> </div><script type="text/javascript"> var css_file=document.createElement("link"); css_file.setAttribute("rel","stylesheet"); css_file.setAttribute("type","text/css"); css_file.setAttribute("href",'//s.bookcdn.com/css/w/booked-wzs-widget-275.css?v=0.0.1'); document.getElementsByTagName("head")[0].appendChild(css_file); function setWidgetData(data) { if(typeof(data) != 'undefined' && data.results.length > 0) { for(var i = 0; i < data.results.length; ++i) { var objMainBlock = document.getElementById('m-booked-weather-bl250-32894'); if(objMainBlock !== null) { var copyBlock = document.getElementById('m-bookew-weather-copy-'+data.results[i].widget_type); objMainBlock.innerHTML = data.results[i].html_code; if(copyBlock !== null) objMainBlock.appendChild(copyBlock); } } } else { alert('data=undefined||data.results is empty'); } } </script> <script type="text/javascript" charset="UTF-8" src="http://widgets.booked.net/weather/info?action=get_weather_info&ver=4&cityID=5546&type=3&scode=124&ltid=3458&domid=w209&cmetric=1&wlangID=1&color=137AE9&wwidth=250&header_color=ffffff&text_color=333333&link_color=08488D&border_form=1&footer_color=ffffff&footer_text_color=333333&transparent=0"></script><!-- weather widget end -->
            </div>
            <!-- /.col-md-4 -->
            <div class="col-md-4">
                <h2><center>AccuWeather </h2>
                  <a href="http://www.accuweather.com/en/ph/quezon-city/264873/weather-forecast/264873" class="aw-widget-legal">
    <!--
    By accessing and/or using this code snippet, you agree to AccuWeather’s terms and conditions (in English) which can be found at http://www.accuweather.com/en/free-weather-widgets/terms and AccuWeather’s Privacy Statement (in English) which can be found at http://www.accuweather.com/en/privacy.
    -->
    </a><div id="awcc1484694296258" class="aw-widget-current"  data-locationkey="264873" data-unit="c" data-language="en-us" data-useip="false" data-uid="awcc1484694296258"></div><script type="text/javascript" src="http://oap.accuweather.com/launch.js"></script>
            <!-- /.col-md-4 -->
            <!-- /.col-md-4 -->
        </div>
        <div class="row">
            <div class="col-md-4">
              <h2><center>Darksky Forecast </h2>
                <iframe id="forecast_embed" type="text/html" frameborder="0" height="245" width="100%" src="http://forecast.io/embed/#lat=14.676041&lon=-121.043700&name=Quezon City"> </iframe>
            </div>
        <!-- /.row -->

        <!-- Footer -->
        <footer>
            <div class="row">
                <div class="col-lg-12">
                    <p>Copyright &copy; Your Website 2014</p>
                </div>
            </div>
        </footer>

    </div>
    <!-- /.container -->

    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

</body>

</html>
