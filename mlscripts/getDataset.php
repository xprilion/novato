<?php
set_time_limit(0);

$arg1 = "nofile";

if(isset($_POST['arg1'])){
	$arg1 = $_POST['arg1'];
	$arg1 = strtolower($arg1);
}

$output = exec('python getDataset.py $arg1');
echo "$output";

?>