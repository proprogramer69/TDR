var amunt=0;
var avall=0;
var esquerra=0;
var dreta=0;
document.addEventListener('keydown', function(evento){
if(evento.keyCode == 38){
	amunt=1;
	if (estat==0){
		var x = document.getElementById("myAudio"); 
		x.volume=0.1
  		x.play(); 
  		var yu = document.getElementById("mort"); 
  		yu.currentTime=0;
  		yu.pause(); 
	} 
}
if(evento.keyCode == 32){
	if (estat==1){
	estat=0;
	tempstotal=0;
	y=0;
	y1=0;
	y2=0;
	y3=0;
	y4=0;
	y5=0;
	y6=0;
	y7=0;
	y8=0;
	y9=0;
	y10=0;
	y11=0;
	peces=[1,1,1,1,1,1,1];
	up= true;
	costat=true;
	ycor=alto/2 - (coralt/2);
	xcor=50;
	punt=0;
    nivell=hola2-1;
	mort = {x:0, y:0, an:midesmort*332/429, alt:midesmort, enable: false};
	mort1 = {x:0, y:0, an:midesmort*332/429, alt:midesmort,enable: false};
	mort2 = {x:0, y:0, an:midesmort*332/429, alt:midesmort, enable: false};
	mort3 = {x:0, y:0, an:midesmort*332/429, alt:midesmort, enable: false};
	mort4 = {x:0, y:0, an:midesmort*332/429, alt:midesmort, enable: false};
	rand=-1;
	xpeça=0;
	ypeça=0;
	separacio=150;
	i=0;
	angle=-1;
	recovel=0;
	minim=300;
	temps=150;	
	var quadrant;
	direccio=-1000;
	paret=-1000;
	paretultima=-1000;
	recorregutx=-1000;
	recorreguty=-1000;
	recorregutangle=-1000;
	recox=-1000;
	recoy=-1000;
	recoang=-1000;
	recovel=0;
	posx=-1000;
	posy=-1000;
	lol=0;
	elegirpeça()
	}
}
if(evento.keyCode == 40){
	avall=1;
	if (estat==0){
		var x = document.getElementById("myAudio"); 
		x.volume=0.1
  		x.play(); 
  		var yu = document.getElementById("mort"); 
  		yu.currentTime=0;
  		yu.pause();
	}
	
}
if(evento.keyCode == 37){
	esquerra=1;
		if (estat==0){
		var x = document.getElementById("myAudio"); 
		x.volume=0.1
  		x.play();
  		var yu = document.getElementById("mort"); 
  		yu.currentTime=0;
  		yu.pause();  
	}
}
if(evento.keyCode == 39){
	dreta=1;
	if (estat==0){
		var x = document.getElementById("myAudio"); 
		x.volume=0.1
  		x.play(); 
  		var yu = document.getElementById("mort"); 
  		yu.currentTime=0;
  		yu.pause(); 
	} 
}
})

document.addEventListener('keyup', function(evento){
if(evento.keyCode == 38){
	amunt=0;
}
if(evento.keyCode == 40){
	avall=0;
}
if(evento.keyCode == 37){
	esquerra=0;
}
if(evento.keyCode == 39){
	dreta=0;
}
})

var imgCor;
var imgMort;
var img1;
var img2;
var img3;
var img4;
var img5;
var img6;
var img7;
var fons;


	

function carga(){
	fons= new Image();
	imgCor= new Image();
	imgCor.src='ima/cor.png';
	imgMort=new Image();
	imgMort.src='ima/mort.png';
	img1= new Image();
	img2= new Image();
	img3= new Image();
	img4= new Image();
	img5= new Image();
	img6= new Image();
	img7= new Image();
	img1.src='ima/1.png';
	img2.src='ima/2.png';
	img3.src='ima/3.png';
	img4.src='ima/4.png';
	img5.src='ima/5.png';
	img6.src='ima/6.png';
	img7.src='ima/7.png';
	fons.src='ima/estrelles.jpg';
}
var nivell=1;
var estat=0;
var falten
var tempstotal=0;
var y=0;
var y1=0;
var y2=0;
var y3=0;
var y4=0;
var y5=0;
var y6=0;
var y7=0;
var y8=0;
var y9=0;
var y10=0;
var y11=0;
var quadradet=30;
var peces=[1,1,1,1,1,1,1];
var up= true;
var costat=true;
var midescor = 75;
var midesmort=150;
var ancho = 1510;
var alto = 700;
var coralt=midescor;
var coran=midescor*617/514;
var ycor=alto/2 - (coralt/2);
var xcor=50;
var punt=0;
var mort = {x:0, y:0, an:midesmort*332/429, alt:midesmort, enable: false};
var mort1 = {x:0, y:0, an:midesmort*332/429, alt:midesmort,enable: false};
var mort2 = {x:0, y:0, an:midesmort*332/429, alt:midesmort, enable: false};
var mort3 = {x:0, y:0, an:midesmort*332/429, alt:midesmort, enable: false};
var mort4 = {x:0, y:0, an:midesmort*332/429, alt:midesmort, enable: false};
var rand=-1;
var xpeça=0;
var ypeça=0;
var costat;
var punticos;
var separacio=150;
var i=0;
var velocitat;
var x;
var angle=-1;
var quadrant;
var direccio;
var paret;
var paretultima;
var recorregutx;
var recorreguty;
var recorregutangle;
var recox;
var recoy;
var recoang;
var recovel=0;
var posx;
var posy;
var lol=0;
var minim=300;
var temps=150;
var stupid=0;
var code;
var inicia=0;
function crearfons(){
	ctx.drawImage(fons,0,0,474,355,0,0,ancho,ancho/474*355);
}
function creamort(){
	ctx.drawImage(imgMort,0,0,332,429,mort.x,mort.y,mort.an,mort.alt);
}
function creamort1(){
	ctx.drawImage(imgMort,0,0,332,429,mort1.x,mort1.y,mort1.an,mort1.alt);
}
function creamort2(){
	ctx.drawImage(imgMort,0,0,332,429,mort2.x,mort2.y,mort2.an,mort2.alt);
}
function creamort3(){
	ctx.drawImage(imgMort,0,0,332,429,mort3.x,mort3.y,mort3.an,mort3.alt);
}
function creamort4(){
	ctx.drawImage(imgMort,0,0,332,429,mort4.x,mort4.y,mort4.an,mort4.alt);
}

function cor(){
	ctx.drawImage(imgCor,0,0,617,514,xcor,ycor,coran,coralt);
}

var canvas, ctx;

function inicializa(){
	//music.play();

	nivell=document.getElementById("lol").innerHTML
	hola2=nivell
	hola1=document.getElementById("kep").innerHTML
	if (hola1=="" || hola1=='<font style="vertica'){
		stupid=1
	}
	if (nivell=="0" || nivell==""||nivell=="NaN"){
		nivell==1;
	}
	nivell=nivell-1

	canvas= document.getElementById('canvas');
	ctx = canvas.getContext('2d');
	carga();
	elegirpeça()
	inicia=1
}



function borrarCanvas(){
	canvas.width = ancho;
	canvas.height=	alto;
}
function crearpeça(){
	if(rand==0){
		ctx.drawImage(img1,0,0,295,76,xpeça,ypeça,quadradet*4,quadradet);
	} else if(rand==1){
		ctx.drawImage(img2,0,0,221,148,xpeça,ypeça,quadradet*3,quadradet*2);
	}else if(rand==2){
		ctx.drawImage(img3,0,0,221,147,xpeça,ypeça,quadradet*3,quadradet*2);
	}else if(rand==3){
		ctx.drawImage(img4,0,0,222,148,xpeça,ypeça,quadradet*3,quadradet*2);
	}else if(rand==4){
		ctx.drawImage(img5,0,0,221,147,xpeça,ypeça,quadradet*3,quadradet*2);
	}else if(rand==5){
		ctx.drawImage(img6,0,0,221,148,xpeça,ypeça,quadradet*3,quadradet*2);
	}else if(rand==6){
		ctx.drawImage(img7,0,0,147,147,xpeça,ypeça,quadradet*2,quadradet*2);
	}
}
function elegirpeça(){
	if (punt!=0){

		var z = document.getElementById("point");
		z.pause();
		z.currentTime=0;
  		z.play();
	}
	punt++
	do {
		rand=Math.floor(Math.random() * 7);
	} while(peces[rand]!=1)
	peces[rand]=0;
	triarpos();
	if(punt%7==0){
		peces=[1,1,1,1,1,1,1];
		
	}
	if(punt%7==1){
		if (nivell!=0){
			var f = document.getElementById("nevelup"); 
	  		f.play(); 
	  	}
	  	angle=-1;
	  	recovel=0;
		nivell++;
		mort.x=ancho/2 - (mort.an/2);
		mort.y=alto/2 - (mort.alt/2);
		mort1.x=ancho/2 - (mort1.an/2);
		mort1.y=alto/2 - (mort1.alt/2);
		mort2.x=ancho/2 - (mort2.an/2);
		mort2.y=alto/2 - (mort2.alt/2);
		mort3.x=ancho/2 - (mort3.an/2);
		mort3.y=alto/2 - (mort3.alt/2);
		mort4.x=ancho/2 - (mort4.an/2);
		mort4.y=alto/2 - (mort4.alt/2);
		mort.enable=false;
		mort1.enable=false;
		mort2.enable=false;
		mort3.enable=false;
		mort4.enable=false;
		ycor=alto/2 - (coralt/2);
		xcor=50;
	}
}
function triarpos(){
	do{
		xpeça=Math.random() * (ancho-quadradet*4);
		ypeça=Math.random() * (alto-quadradet*2);
	}while(Math.abs(xpeça-xcor)<separacio && Math.abs(ypeça-ycor)<separacio)
}
function moviment(){
	if (amunt==1){
		if (ycor>0){
			ycor-=10;
		}
	}
	if(avall==1){
		if (ycor<(alto-coralt))
			ycor+=10;
	}
	if(esquerra==1){
		if (xcor>0){
			xcor-=10;
		}
	}
	if(dreta==1){
		if (xcor<(ancho-coran))
			xcor+=10;
	}
}
function xoc(){
	for (x=xcor;x<=xcor+coran;x++) { 
		if (mort.enable==true){
			y=mort.y+mort.alt/2+Math.sqrt((1-(x-(mort.x+mort.an/2))**2/(mort.an/2)**2)*(mort.alt/2)**2);
			y1=mort.y+mort.alt/2-Math.sqrt((1-(x-(mort.x+mort.an/2))**2/(mort.an/2)**2)*(mort.alt/2)**2);
		}
		if (mort1.enable==true){
			y4=mort1.y+mort1.alt/2+Math.sqrt((1-(x-(mort1.x+mort1.an/2))**2/(mort1.an/2)**2)*(mort1.alt/2)**2);
			y5=mort1.y+mort1.alt/2-Math.sqrt((1-(x-(mort1.x+mort1.an/2))**2/(mort1.an/2)**2)*(mort1.alt/2)**2);
		}
		if (mort2.enable==true){
			y6=mort2.y+mort2.alt/2+Math.sqrt((1-(x-(mort2.x+mort2.an/2))**2/(mort2.an/2)**2)*(mort2.alt/2)**2);
			y7=mort2.y+mort2.alt/2-Math.sqrt((1-(x-(mort2.x+mort2.an/2))**2/(mort2.an/2)**2)*(mort2.alt/2)**2);
		}
		if (mort3.enable==true){
			y8=mort3.y+mort3.alt/2+Math.sqrt((1-(x-(mort3.x+mort3.an/2))**2/(mort3.an/2)**2)*(mort3.alt/2)**2);
			y9=mort3.y+mort3.alt/2-Math.sqrt((1-(x-(mort3.x+mort3.an/2))**2/(mort3.an/2)**2)*(mort3.alt/2)**2);
		}
		if (mort4.enable==true){
			y10=mort4.y+mort4.alt/2+Math.sqrt((1-(x-(mort4.x+mort4.an/2))**2/(mort4.an/2)**2)*(mort4.alt/2)**2);
			y11=mort4.y+mort4.alt/2-Math.sqrt((1-(x-(mort4.x+mort4.an/2))**2/(mort4.an/2)**2)*(mort4.alt/2)**2);
		}
		if (x>xcor+(coran/2) && x<coran+xcor){
			y2=(ycor+coralt)-(x-(xcor+coran/2));
			y3= ycor+coran/4-Math.sqrt((coran/4)**2-(x-(xcor+3*coran/4))**2);
		}else if (x>xcor && x<=xcor+(coran/2)){
			y2=(ycor+coralt)+(x-(xcor+coran/2));
			y3= ycor+coran/4-Math.sqrt((coran/4)**2-(x-(xcor+coran/4))**2);
		}
		if (rand==0){
			if(xpeça<x && x<quadradet*4+xpeça && ((ypeça<y2 && y2<quadradet+ypeça)||(ypeça<y3 && y3<quadradet+ypeça))){
				elegirpeça();
			}
		}else if (rand==1) {
			if(xpeça<x && x<quadradet*2+xpeça && ((ypeça+quadradet<y2 && y2<quadradet*2+ypeça)||(ypeça+quadradet<y3 && y3<quadradet*2+ypeça))){
				elegirpeça();
			}else if(xpeça+quadradet<x && x<quadradet*3+xpeça && ((ypeça<y2 && y2<quadradet+ypeça)||(ypeça<y3 && y3<quadradet+ypeça))){
				elegirpeça();
			}
		}else if (rand==2) {
			if(xpeça<x && x<quadradet*3+xpeça && ((ypeça+quadradet<y2 && y2<quadradet*2+ypeça)||(ypeça+quadradet<y3 && y3<quadradet*2+ypeça))){
				elegirpeça();
			}else if(xpeça<x && x<quadradet+xpeça && ((ypeça<y2 && y2<quadradet+ypeça)||(ypeça<y3 && y3<quadradet+ypeça))){
				elegirpeça();
			}
		}else if (rand==3) {
			if(xpeça<x && x<quadradet*3+xpeça && ((ypeça+quadradet<y2 && y2<quadradet*2+ypeça)||(ypeça+quadradet<y3 && y3<quadradet*2+ypeça))){
				elegirpeça();
			}else if(xpeça+quadradet<x && x<quadradet*2+xpeça && ((ypeça<y2 && y2<quadradet+ypeça)||(ypeça<y3 && y3<quadradet+ypeça))){
				elegirpeça();
			}
		}else if (rand==4) {
			if(xpeça<x && x<quadradet*3+xpeça && ((ypeça+quadradet<y2 && y2<quadradet*2+ypeça)||(ypeça+quadradet<y3 && y3<quadradet*2+ypeça))){
				elegirpeça();
			}else if(xpeça+quadradet*2<x && x<quadradet*3+xpeça && ((ypeça<y2 && y2<quadradet+ypeça)||(ypeça<y3 && y3<quadradet+ypeça))){
				elegirpeça();
			}
		}else if (rand==5) {
			if(xpeça<x && x<quadradet*2+xpeça && ((ypeça<y2 && y2<quadradet+ypeça)||(ypeça<y3 && y3<quadradet+ypeça))){
				elegirpeça();
			}else if(xpeça+quadradet<x && x<quadradet*3+xpeça && ((ypeça+quadradet<y2 && y2<quadradet*2+ypeça)||(ypeça+quadradet<y3 && y3<quadradet*2+ypeça))){
				elegirpeça();
			}
		}else if (rand==6) {
			if(xpeça<x && x<quadradet*2+xpeça && ((ypeça<y2 && y2<quadradet*2+ypeça)||(ypeça<y3 && y3<quadradet*2+ypeça))){
				elegirpeça();
			}
		}

		if ((y>y2 && y2>y1) ||(y>y3 && y3>y1)){
			estat=1;
			
		} else if((y4>y2 && y2>y5) ||(y4>y3 && y3>y5)){
			estat=1;
			
		}else if((y6>y2 && y2>y7) ||(y6>y3 && y3>y7)){
			estat=1;
		
		}else if((y8>y2 && y2>y9) ||(y8>y3 && y3>y9)){
			estat=1;
		
		}else if((y10>y2 && y2>y11) ||(y10>y3 && y3>y11)){
			estat=1;
			
		}
		y=0;
		y1=0;
		y4=0;
		y5=0;
		y6=0;
		y7=0;
		y8=0;
		y9=0;
		y10=0;
		y11=0;
		//if((x-(mort.x+mort.an/2)**2/mort.an**2)+(y-(mort.y+mort.alt/2)**2/mort.alt**2)==1){
		//}
		
		//if((x-(xcor+coran/2)**2/coran**2)+(y-(ycor+coralt/2)**2/coralt**2)==1){
		//}
		//if (corbox==mortbox==true) {
			//console.log("hola")
		//}
	}
	
}
function nivell1(){	
	creamort();
	mort.enable=true;
	if (mort.y<=0){
		up=false;
	}else if (mort.y>=(alto-mort.alt)){
		up=true;
	}
	if (up==true){
		mort.y-=2*velocitat;
	}else{
		mort.y+=2*velocitat;
	}
}
function nivell2(){
	creamort1();
	mort1.enable=true;
	if (mort1.x<=0){
		costat=false;
	}else if (mort1.x>=(ancho-mort1.an)){
		costat=true;
	}
	if (costat==true){
		mort1.x-=2*velocitat;
	}else{
		mort1.x+=2*velocitat;
	}
}
function nivell3(){
	creamort2();
	paret=0;
	mort2.enable=true;
	if (angle==-1){
		paretultima=0;
		angle=Math.random() * 90;	
		quadrant= Math.floor(Math.random() * 4);
	}
	if(quadrant==4){
		quadrant=3;
	}
	direccio=angle+90*quadrant;
	mort2.x+=Math.cos(direccio*2*Math.PI/360)*velocitat*3;//convertir a radiants
	mort2.y+=Math.sin(direccio*2*Math.PI/360)*velocitat*3;
	if (mort2.x<=0){
		paret=1;
	}else if (mort2.x>=(ancho-mort1.an)){
		paret=2;
	}
	if (mort2.y<=0){
		paret=3;
	}else if (mort2.y>=(alto-mort.alt)){
		paret=4;
	}
	if (paret!=0 && paret!=paretultima){
		angle=90-angle
		if (paret==1){
			if (quadrant==1){
				quadrant=0;
			}else{
				quadrant=3;
			}
		} else if(paret==2){
			if (quadrant==3){
				quadrant=2
			}else{
				quadrant=1
			}
		}else if(paret==3){
			if (quadrant==2){
				quadrant=1;
			}else{
				quadrant=0;
			}
		}else if(paret==4){
			if (quadrant==0){
				quadrant=3;
			}else{
				quadrant=2;
			}
		}
		
		paretultima=paret;
	
	}
}
function nivell4(){
	creamort3();
	mort3.enable=true;
	recorregutx=(xcor+coran/2)-(mort3.x+mort3.an/2);
	recorreguty=(ycor+coralt/2)-(mort3.y+mort3.alt/2);
	recorregutangle=Math.atan(recorreguty/recorregutx);
	if (recorregutx>0){
		mort3.x+=Math.cos(recorregutangle)*velocitat;
		mort3.y+=Math.sin(recorregutangle)*velocitat;
	}else{
		mort3.x-=Math.cos(recorregutangle)*velocitat;
		mort3.y-=Math.sin(recorregutangle)*velocitat;
	}
}
function nivell5(){
	creamort4();
	mort4.enable=true;
	if (recovel==0 || posx==mort4.x){
		do{
			posx=Math.random() * (ancho-mort4.an);
			posy=Math.random() * (alto-mort4.alt);
		}while(Math.abs(posx-mort4.x)<minim && Math.abs(posy-mort4.y)<minim)
		recox=posx-(mort4.x);
		recoy=posy-(mort4.y);
		recovel=Math.sqrt(recox**2+recoy**2)/(temps/2);//(temps/velocitat) wtf? (espai/temps)
		recoang=Math.atan(recoy/recox)
	}		
	
	if (recox>0){
		mort4.x+=Math.cos(recoang)*recovel;
		mort4.y+=Math.sin(recoang)*recovel;
		if (posx<mort4.x) {
			posx=mort4.x;
		}
	}else{
		mort4.x-=Math.cos(recoang)*recovel;
		mort4.y-=Math.sin(recoang)*recovel;
		if (posx>mort4.x) {
			posx=mort4.x;
		}	
	}
}
function movmort(){
	velocitat=(punt%7)
	if (velocitat==0){
		velocitat=7;
	}
	if(nivell==1){
		nivell1()
	}else if(nivell==2){
		nivell1()
		nivell2()
	}else if(nivell==3){
		nivell3()
	}else if(nivell==4){
		nivell2()
		nivell3()
	}else if(nivell==5){
		nivell4()
	}else if(nivell==6){
		nivell4()
		nivell1()
	}else if(nivell==7){
		nivell1()
		nivell2()
		nivell3()
	}else if(nivell==8){
		nivell4()
		nivell3()
	}else if(nivell==9){
		nivell1()
		nivell2()
		nivell3()
		nivell4()
	}else if(nivell==10){
		nivell5()
	}else if(nivell==11){
		nivell5()
		nivell1()
		nivell2()
	}else if(nivell==12){
		nivell5()
		nivell3()
	}else if(nivell==13){
		nivell4()
		nivell5()
	}else if(nivell==14){
		nivell3()
		nivell4()
		nivell5()
	}else {
		nivell1()
		nivell2()
		nivell3()
		nivell4()
		nivell5()
	}
}

	

var FPS=10;
setInterval(function(){
	if (inicia==1){
	if (stupid==0){
		if (estat==0){
			principal();
		}else{
			//fetch("joc1.php",{
			//	method: 'POST',
			//	body:nivell
			//})
			borrarCanvas();
			//$.ajax({
		            //type : "POST",  //type of method
		            //url  : "joc1.php",  //your page
		            //data : { est : 1},
       // }); 	
			
			ctx.drawImage(imgMort,0,0,332,429,500,0,alto/429*332,alto);
			var x = document.getElementById("myAudio"); 
	  		x.pause(); 
	  		x.currentTime=0;
	  		if (lol==0){
	  			lol++;
	  			var yu = document.getElementById("mort"); 
	  			yu.play();
	  			$.ajax({
		            type : "POST",  //type of method
		            url  : "polla.php",  //your page
		            data : { no : hola1, ni : hola2, punts:punticos, temps: Math.floor(tempstotal)},
		            success(e){
		            	console.log(e)
		            	code=e
		            }
        }); 	
	  		}
	  		document.getElementById("verga").innerHTML = "MORISTE WEY (clica espai per reiniciar)"+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;El teu codi és: "+code  		
		}
	}else{
		borrarCanvas();
		document.getElementById("verga").innerHTML = "NO ET PASSIS DE LLEST! VES AL MENÚ I POSA EL TEU NOM!!! (POTSER HI HA HAGUT UN ERROR)"
	}
}
},250/10)
setInterval(function(){
	if (inicia==1){
	if (estat==0){
		tempstotal+=0.1
	}
}
},1000/10)
function principal(){
	punticos=punt-1;
	falten=punticos%7;
	document.getElementById("verga").innerHTML = "Nivell: "+nivell+"&nbsp;&nbsp;&nbsp;&nbsp;Punts: "+punticos+"&nbsp;&nbsp;&nbsp;&nbsp;Tens : "+falten+"/7 peces"+"&nbsp;&nbsp;&nbsp;&nbsp;Temps: "+Math.floor(tempstotal)+" s"
	xoc();
	borrarCanvas();
	crearfons();
	moviment();
	crearpeça();
	movmort();
	cor();
}