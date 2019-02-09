<html>
	<head>
		<title>Indoor Plant Log</title>
	</head>
	<body>
        <?php
            $fp = fopen('/var/www/html/heaterPin.txt', 'r');
            $statut = 0;
            $target = 0;
            $current = 0;
            $status  = (int)fgets($fp);
            $target  = (float)fgets($fp);
            $current = (float)fgets($fp);

            fclose($fp);
                
            echo "Current heater status: ";
            if($status == 0) {
                echo "<b><font color=\"red\">Off</font></b>";
            }else{
                echo "<b><font color=\"green\">On</font></b>";
            }
            echo ", current temperature: ";
            echo $current;
            echo ", target: ";
            echo $target;
            echo "<br>";
        ?>
		<h1>Temperature Log</h1>
		<p><h2>Last Hour</h2>
		<img src="lastHourTemp.png" alt="Temperature of the last hour">
		</p>
		<p><h2>Last Day</h2>
		<img src="lastDayTemp.png" alt="Temperature of the last day">
		</p>
		<img src="allTime.png">
	</body>
	<form action="process.php" method="post">
		Lights ():...
		<input type="radio" name="lights" value="disable">Disable
		<input type="radio" name="lights" value="enable">Enable
		<input type="radio" name="lights" value="forceon">Force on
		<br>
		<input type="submit">
	</form>
</html>

