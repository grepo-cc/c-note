// function validateImage(url)
// {    
// 	var xmlHttp ;
// 	if (window.ActiveXObject)
// 	 {
// 	  xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
// 	 }
// 	 else if (window.XMLHttpRequest)
// 	 {
// 	  xmlHttp = new XMLHttpRequest();
// 	 } 
// 	xmlHttp.open("Get",url,false);
// 	xmlHttp.send();
// 	if(xmlHttp.status==404)
// 		return false;
// 	else
// 		return true;
// } 
document$.subscribe(({ body }) => { 
    var vase_url = location.hostname + ":" + location.port;
    var mksvg = "192.168.120.157:15780/myftppicgo/mksvg.php?h=";
    var extl = ["jpg", "svg", "png"];

    var a_ist = document.querySelectorAll("a.go-gitic");
    var pres = document.querySelectorAll("pre");

    a_ist.forEach(function (a_i) {
        pp = a_i.parentNode;
        divp = pp.nextElementSibling;
         
        var divpcs = divp.childNodes;
        divpcs.forEach(function (divpc) {
            if (divpc.tagName == "PRE") {
                a_i.target = "_blanket";
                divpc.prepend(a_i);
            }
            
           
        });
        
        // prep.append(prep);
       
    });
    // a_ist[0].innerHTML = "goto1";
    // a_ist[0].target = "_blanket";
    // $("pre").append(a_ist[0])
    
// images.forEach(function(imgae) {
// 	var srcx = imgae.src;
// 	if(srcx.indexOf(vase_url+location.pathname+":/") !== -1){
// 		// console.log("======================");
// 		// console.log(vase_url+location.pathname+":/");
// 		for (i = 0; i < extl.length; i++) { 
// 		var pathImg = srcx.replace(vase_url+location.pathname+":/", vase_url+"/assets/images/")+"."+extl[i];
// 			if(validateImage(pathImg)){
// 				 imgae.src =  pathImg;
// 			}
// 		}
// 	}
// 	// var stri = "net@/";
 
// 	// if(srcx.indexOf(vase_url+location.pathname+stri) !== -1){
		 
		
// 	// 	imgae.src =  srcx.replace(vase_url+location.pathname+stri
// 	// 	, mksvg) +"&d=网络工程";
// 	// }
// //http://192.168.0.160:16090/assets/images/6d7af8c2ca774d5399b974b88c2bace1.jpg
// })
/////////////////////////////////////////////////////////////////
/* var a_s = document.querySelectorAll("a");
a_s.forEach(function(a) {
//image.src =image.src+"/asset/images/";
var srca= a.src
if(srca  != undefined && srca.length>1){
a.src =srca.replace(":", mksvg);;
}
//http://192.168.0.160:16090/assets/images/6d7af8c2ca774d5399b974b88c2bace1.jpg
}) */
/////////////////////////////////////////////////////////////////
var tabindexs = document.querySelectorAll('article div[class^="tabbed-set"]  div[class^="tabbed-labels"] label');
 //console.log(tabindexs);
tabindexs.forEach(function(tabindex) {
//image.src =image.src+"/asset/images/";
 
 /* //console.log(tabindex.childNodes);
var newElement = document.createElement("h4");
newElement.appendChild( tabindex.childNodes[0]);
 //console.log(newElement);
tabindex.insertBefore(newElement, tabindex.childNodes[0]); */
//http://192.168.0.160:16090/assets/images/6d7af8c2ca774d5399b974b88c2bace1.jpg
})
})