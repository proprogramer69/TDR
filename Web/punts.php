<html lang="en">
<head>
	<script type="text/javascript">
      function Compro(e){
        key =e.keyCode || e.which;
        tecla=String.fromCharCode(key).toString();
        letras="1234567890";

        especiales=[8,13,127];//codi ascii
        tecla_especial=false
        for(var i in especiales){
          if(key==especiales[i]){
              tecla_especial=true
              break
          }
        }
        if(letras.indexOf(tecla)==-1 && !tecla_especial){
          alert("Per posar el teu codi només necessites números")
          return false
        }
      }


    </script>
    <meta charset="UTF-8">
    <title>tetrisrun</title>
    <link rel="icon" type="image/png" href="logo/logo.png">
    <link rel="stylesheet" type="text/css" href="css/punts.css">
</head>
<body>
	<center>
		<h1>PUNTUACIONS</h1>
	<table>
		<tr>
			<td>POSICIÓ</td>
			<td>NOM</td>
			<td>PUNTS</td>
			<td>TEMPS(s)</td>
		</tr>
<?php
      include("abrir_conexion.php");
      $sql="SELECT * FROM `puntuacions` ORDER BY punts DESC, temps ASC, nivell DESC, id ASC LIMIT 0, 5";
      $result=mysqli_query($conexion,$sql);
      $hola=0;
      while($mostrar=mysqli_fetch_array($result)){
      	$hola=$hola+1;
?>
<tr>
<td><?php echo $hola ?></td>
<td><?php echo $mostrar['nom'] ?></td>
<td><?php echo $mostrar['punts'] ?></td>
<td><?php echo $mostrar['temps'] ?></td>
</tr>
<?php
      }
?>
</table>
	<form action="punts.php" method="post">
	<h2>Introdueix el teu codi per conèixer la puntuació</h2>
<input type="text" name="codi" id="codi" onkeypress="return Compro(event);" required="">
<input type="submit" value="BUSCAR" id="buscar">
</form>

<table>
<?php
	$consulta=$_POST['codi'];
	$sql1="SELECT nom, punts, temps, id, ROW_NUMBER() OVER(ORDER BY punts DESC, temps ASC, nivell DESC, id ASC) AS HOLA FROM `puntuacions`";
	$result1=mysqli_query($conexion,$sql1);

	while($mostrar1=mysqli_fetch_array($result1)){
			if ($mostrar1['id']==$consulta){

?>
<h2>La teva recerca</h2>
<tr>
			<td>POSICIÓ</td>
			<td>NOM</td>
			<td>PUNTS</td>
			<td>TEMPS(s)</td>
		</tr>
<tr>
<td><?php echo $mostrar1['HOLA'] ?></td>
<td><?php echo $mostrar1['nom'] ?></td>
<td><?php echo $mostrar1['punts'] ?></td>
<td><?php echo $mostrar1['temps'] ?></td>
</tr>

<?php
	}
}
?>
	</table>
<a href="index.html"><button id="menu"> MENÚ </button></a>
</center>
</body>
</html>