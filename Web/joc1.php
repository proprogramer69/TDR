<!DOCTYPE html>
<html lang="en">
<head>

    <meta charset="UTF-8">
    <script src="script26.js"></script>
    <title>tetrisrun</title>
    <link rel="stylesheet" type="text/css" href="css/estilbo10.css">
    <link rel="icon" type="image/png" href="logo/logo.png"> 
    <script src="jquery-3.2.1.min.js"></script>
</head>
<body onload="inicializa();">
	<center>
	<div class="holis" id="verga"></div>
	<audio id="myAudio" >
  		<source src="song/tetris.mp3" type="audio/mpeg" autoplay="true" loop="true">
	</audio>
	<audio id="mort" >
  		<source src="song/mort.wav" autoplay="true" loop="true" >
	</audio>
	<audio id="point" >
  		<source src="song/moneda.mp3" autoplay="true" loop="true">
	</audio>
	<audio id="nevelup">
  		<source src="song/r.mp3" autoplay="true" loop="true">
	</audio>
	<canvas id="canvas"></canvas>
	<div id="lol"><?php echo ($_POST['nivell']);?></div>
<div id="kep"><?php echo ($_POST['nom']);?></div>
<a href="index.html"><button id="menu"> MENÚ </button></a>
<a href="punts.php"><button id="puntuacio"> PUNTUACIÓ </button></a>
    </center>
</div>
</body>
</html>