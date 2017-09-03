<?php
set_time_limit(0);

$arg1 = 5;

if(isset($_POST['arg1'])){
	$arg1 = $_POST['arg1'];
}

//$output = shell_exec('python getDataset.py');
$output = exec("python regression3.py $arg1");
echo "$output";

?>