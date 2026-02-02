
//新建一个div元素节点
var div=document.createElement("center");
// div.innerText = "helloworld";
div.id = "bigimg";
 
//把div元素节点添加到body元素节点中成为其子节点，但是放在body的现有子节点的最后
document.body.appendChild(div);
//插入到最前面
document.body.insertBefore(div, document.body.firstElementChild);

$(document).ready(function(){
    $("#bigimg").on("click",function(obj){
        
        $("#bigimg").css("display","none");
    //   alert("段落被点击了。");
    });
    $("img").on("click",function(obj){
        
        var eles = $(obj);
        // console.log(eles[0].target.src);
        var imgsrc = eles[0].target.src;
        $("#bigimg").css("display","block");
        $("#bigimg").html("<img src="+imgsrc+" />");
        // var imgsrc = eles[0].src;
        // console.log(imgsrc);
      //alert("段落被点击了。");
    });
  });

 