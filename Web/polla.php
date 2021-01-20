<?php
      $nombre= $_POST['no'];
      $niv= $_POST['ni']; 
      $punts= $_POST['punts']; 
      $temps= $_POST['temps'];
      include("abrir_conexion.php");
      $conexion->query("INSERT INTO $tabla_db1 (nom,nivell,punts,temps) values ('$nombre','$niv','$punts','$temps')");
      $estat=0;
	include("abrir_conexion.php");
	$sql="SELECT count(*) FROM `puntuacions`";
	$result=mysqli_query($conexion,$sql);
	while($mostrar=mysqli_fetch_array($result)){
	$codi=$mostrar['count(*)'];
	echo $codi;
}
      //include("cerrar_conexion.php");
        ?>