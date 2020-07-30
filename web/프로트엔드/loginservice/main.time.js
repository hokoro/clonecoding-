var nowtime =document.querySelector('.nowtime');

var day = new Array('일','월','화','수','목','금','토');

function startInterval()		//단위 시간동안 함수 출력 
{
	setInterval(printDate,1000);
}
function printDate()
{
const today = new Date();
const year = today.getFullYear();
const month = today.getMonth();
const date = today.getDate();
const hour = today.getHours();
const minute = today.getMinutes();
const second = today.getSeconds();
document.getElementById("today").innerHTML = year+"년 "+(month+1)+"월 "+date+"일 "+day[today.getDay()]+"요일 "+hour+"시 "+minute+"분 "+second+"초 ";

}
