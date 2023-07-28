//var jh=new Array();
//let switchBtn = document.querySelector('.banner-imgBox-div');
//jh[0]="url('../static/image/picture1.jpg')";
//jh[1]="url('../static/image/picture2.jpg')";
//jh[2]="url('../static/image/picture3.png')";
//jh[3]="url('../static/image/picture4.png')";
//var kj=document.getElementById("imagebo");
////<!--获取框架div的标签，在下面进行更改背景-->
//var x=-1;
//var index=-1;
////<!--定义变量x，建立索引-->
//var l=jh.length;
//var y=0;
////<!--获取集合中元素个数-->
//function lb()
//{
//    x++;
//    index++;
//    y++;
//    kj.style.backgroundImage=jh[x];
//    switchBtn.children[index].classList.add('on2');
//    if (index==0)
//    {
//        if (y)
//        {
//            switchBtn.children[3].classList.remove('on2');
//        }
//    }
//    else if(index!=0)
//    {
//        switchBtn.children[index-1].classList.remove('on2');
//        y=1;
//    }
//    if (x==l-1)
//    {
//        index=-1;
//        x=-1;
//    }
//    window.setTimeout("lb()",2000);
////    <!--2s后再次播放集合中的图片-->
//}
//window.setTimeout("lb()",0);
////<!--开始进行轮播-->




var imgShow = document.getElementsByClassName('parent')[0],
	dotList = document.querySelectorAll('.dots >.clearfix > li');
var btnLeft = document.getElementsByClassName('btnLeft')[0],
    btnRight = document.getElementsByClassName('btnRight')[0];
var dotLen = dotList.length,
	index = 0; //轮播层的图片索引，0表示第一张

//圆点显示
function showRadius() {
	for(var i = 0; i < dotLen; i++) {
		if(dotList[i].className === "on"){
			dotList[i].className = "off";
		}
	}
	dotList[index].className = "on";
}

//向左移动
btnLeft.onclick = function() {
	index--;
    if(index < 0){  /*第1张向左时，变为第5张*/
        index = 3;
    }
    showRadius();
	var left;
	var imgLeft = imgShow.style.left;
	if(imgLeft === "0px") { /*当是第1张时，每张图片左移，移4张图，位置为-(4*500)*/
		left = -1770;
	}
	else{
		left = parseInt(imgLeft) + 590; /*由于left为负数，每左移一张加500*/
	}
	imgShow.style.left = left + "px";
}

//向右移动
btnRight.onclick = function() {
	index++;
    if(index > 3){  /*第5张向右时，变为第1张*/
        index = 0;
    }
    showRadius();
	var right;
	var imgLeft = imgShow.style.left;
	if(imgLeft === "-1770px") { /*当是第5张时，第1张的位置为0*/
		right = 0;
	}
	else{
		right = parseInt(imgLeft) - 590; /*由于left为负数，每右移一张减500*/
	}
	imgShow.style.left = right + "px";
}
function zidongbofang(right){
    if(right){
        index++;
        if(index > 3){  /*第5张向右时，变为第1张*/
            index = 0;
        }
        showRadius();
        var right;
        var imgLeft = imgShow.style.left;
        if(imgLeft === "-1770px") { /*当是第5张时，第1张的位置为0*/
            right = 0;
        }
        else{
            right = parseInt(imgLeft) - 590; /*由于left为负数，每右移一张减500*/
        }
        imgShow.style.left = right + "px";
    }
    else
    {
        index--;
        if(index < 0){  /*第1张向左时，变为第5张*/
            index = 3;
        }
        showRadius();
        var left;
        var imgLeft = imgShow.style.left;
        if(imgLeft === "0px") { /*当是第1张时，每张图片左移，移4张图，位置为-(4*500)*/
            left = -1770;
        }
        else{
            left = parseInt(imgLeft) + 590; /*由于left为负数，每左移一张加500*/
        }
        imgShow.style.left = left + "px";
    }
}
// 自动轮播
var timer;
var time=2000;
function autoPlay() {
	timer = setInterval(function() {
		var right;
		index++;
        if(index > 3){  /*第4张向右时，变为第1张*/
            index = 0;
        }
        showRadius();
		var imgLeft = imgShow.style.left;
		if(imgLeft === "-1770px") {
			right = 0;
		}
		else{
			right = parseInt(imgLeft) - 590;
		}
		imgShow.style.left = right + "px";
	} ,time)
}
for(var i = 0; i < dotLen; i++) {
    /*利用闭包传递索引*/
    (function(i) {
        dotList[i].onclick = function() {
	        var dis = index - i; //当前位置和点击的距离
	        imgShow.style.left = (parseInt(imgShow.style.left) + dis * 590) + "px";
	        index = i; //显示当前位置的圆点
	        showRadius();
    	}
    })(i);
}
var interval = setInterval(() => {
    zidongbofang(true)
}, time);
function stop(x){
    clearInterval(interval);
}
function running(){
    clearInterval(interval);
    interval = setInterval(() => {
            zidongbofang(true)
        }, time);
}

