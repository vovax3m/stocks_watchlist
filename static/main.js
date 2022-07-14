function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function getHour(){
	var t = new Date();
	return  t.getHours();  
}

function getWeekday(){
	var t = new Date();
	return  t.getDay();  
}

function startTime() {
  var today = new Date();
  var h = today.getHours();
  var m = today.getMinutes();
  var s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  document.getElementById('time').innerHTML =
  h + ":" + m + ":" + s;
  var t = setTimeout(startTime, 500);
}

function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;
}

async function asyncForEach(array, callback) {
  for (let index = 0; index < array.length; index++) {
    await callback(array[index], index, array);
  }
}
const start = async () => {
  var w=document.getElementById("tickerlist").textContent.split(" ");
  await asyncForEach(w, async (num) => {
    //console.log(num);
    var activel=document.getElementById(num);
    var gr=document.getElementById("tradingview_" + num)
    activel.style["background-color"] = '#110044'; 
    gr.style["top"]='40px';
    url="http://192.168.1.125:5000/get?ticker=" + num
    var hour=getHour();
    var day=getWeekday();
    if(hour > 6 && hour < 16 && day > 0 && day < 6){
    	document.getElementById("message").innerHTML="";
      let response = await fetch(url);
      if (response.ok) { // if HTTP-status is 200-299
  // get the response body (the method explained below)
        let json = await response.json();
        document.getElementById(num + "_price").innerHTML=json.price
        document.getElementById(num + "_pers").innerHTML=json.changePercent + "%"
        document.getElementById(num + "_chg").innerHTML=json.change
        if(json.changePercent > 0){
          document.getElementById(num + "_pers").className="green";
          document.getElementById(num + "_chg").className="green";
        }else{
          document.getElementById(num + "_pers").className="red";
          document.getElementById(num + "_chg").className="red";
        }
      //document.getElementById(num + "_stat").innerHTML="open:" + json.open +"<br>" + "high:" + json.high + "<br>" + "low:" + json.low
      } else {
        console.log("HTTP-Error: " + response.status);
    }
   }else{
   	document.getElementById("message").innerHTML="Market closed, watch list not updating";
   };
    await sleep(30000);
    activel.style["background-color"] = '';
    gr.style["top"]='-1200px';
  });
  start();
}

document.addEventListener("DOMContentLoaded", function(){
  startTime();
  getHour();
  setTimeout(function(){ start(); }, 60000);
    
});