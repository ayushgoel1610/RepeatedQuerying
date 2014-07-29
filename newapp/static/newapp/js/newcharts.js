function charts(url,timeformat){
  $(".chart").show();
  d3.csv(url, function (error, data) {
    // "./halfhour_any_month.csv"
    var obj = crossfilter(data);
    var parseTime;
    if (timeformat == "H")
      parseTime = d3.time.format("%H:%M:%S").parse;

     //a function to display data through applied filter in the console
    function print_filter(filter){
      var f=eval(filter);
      if (typeof(f.length) != "undefined") {}
        else{}
      if (typeof(f.top) != "undefined") {f=f.top(Infinity);}
        else{}
      if (typeof(f.dimension) != "undefined") {f=f.dimension(function(d) { return "";}).top(Infinity);}
        else{}
      console.log(filter+"("+f.length+") = "+JSON.stringify(f).replace("[","[\n\t").replace(/}\,/g,"},\n\t").replace("]","\n]"));
    }
     //parsing the data
    data.forEach(function(d) {
      if (timeformat == "H")
        d.time = parseTime(d.time);
      var arr = d.batch.match(/(\d+|\D+)/gi);
      d.batch = arr[0];
      if (arr[1])
        d.year = parseInt(arr[1],10);
      else 
        d.year = null;
      d.count = parseInt(d.count, 10);
    });
    //printing data to console, only for debugging purposes
   print_filter("obj");

   var TimeDim = obj.dimension(function(d){ return d.time;});
   var Time_total = TimeDim.group().reduceSum(function(d){ return d.count});
   var minDate, maxDate;
   if (timeformat == "H") {
    minDate = TimeDim.bottom(1)[0].time;
    maxDate = TimeDim.top(1)[0].time;
   }   
   var timebarChart  = dc.barChart("#chart-bar-count");

   var batchDim = obj.dimension(function(d){ return d.batch;});
   var batch_total = batchDim.group().reduceSum(function(d){ return d.count});
   var BatchRingChart   = dc.pieChart("#chart-ring-batch");

   var yearDim = obj.dimension(function(d){ return d.year;});
   var year_total = yearDim.group().reduceSum(function(d){ return d.count});
   var YearRingChart   = dc.pieChart("#chart-ring-year");
      
   var locDim = obj.dimension(function(d){ return d.device_id;});
   var loc_total = locDim.group().reduceSum(function(d){ return d.count});
   var APNameRingChart   = dc.pieChart("#chart-ring-AP");

   if (timeformat == "H")
    timebarChart
      .xUnits(function(){return 150;})
      //.xUnits(d3.time.hours)
      //.xUnits(dc.units.ordinal)
      .width(1200).height(300)
      .dimension(TimeDim)
      .group(Time_total)
      .x(d3.time.scale().domain([minDate,maxDate]))
      //.x(d3.scale.ordinal().domain(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]))
      .y(d3.scale.linear())
      //.brushOn(false)
      .xAxisLabel("Date")
      .yAxisLabel("People in campus on average")
      .transitionDuration(500)
      .centerBar(true)    
      //.gap(25)
      .elasticY(true)
      .elasticX(true)
      .xAxisPadding(1)
      .xAxis().tickFormat();
    else 
   timebarChart
      //.xUnits(function(){return 35;})
      .xUnits(dc.units.ordinal)
      .width(1200).height(300)
      .dimension(TimeDim)
      .group(Time_total)
      //.x(d3.time.scale().domain([minDate,maxDate]))
      .x(d3.scale.ordinal().domain(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]))
      //.y(d3.scale.linear())
      //.brushOn(false)
      .xAxisLabel("Date")
      .yAxisLabel("People in campus on average")
      .transitionDuration(500)
      .centerBar(true)    
      .gap(25)
      .elasticY(true)
      .elasticX(true)
      .xAxisPadding(1)
      .xAxis().tickFormat();

    YearRingChart
        .width(300).height(300)
        .dimension(yearDim)
        .group(year_total)
        .innerRadius(50);

    BatchRingChart
        .width(300).height(300)
        .dimension(batchDim)
        .group(batch_total)
        .innerRadius(50);

    APNameRingChart
        .width(300).height(300)
        .dimension(locDim)
        .group(loc_total)
        .innerRadius(50);
    
    dc.renderAll();
  });
}