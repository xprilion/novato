<?php
set_time_limit(0);

//$output = shell_exec('python getDataset.py');
$output = exec('nearest_neighbour_regression.py 10');
echo "$output";

?>