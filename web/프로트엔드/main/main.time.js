const today = new Date();
const year = today.getFullYear();
const month = today.getMonth();
const date = today.getDate();
const hour = today.getHours();
const minute = today.getMinutes();
const second = today.getSeconds();

var day = new Array('일','월','화','수','목','금','토');

function printDate()
{
document.write(year+"년 "+month+"월 "+date+"일 "+day[today.getDay()]+"요일 ");
document.write(hour+"시 "+minute+"분 "+second+"초 ");
}
