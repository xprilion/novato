<?php
set_time_limit(0);

//$output = shell_exec('python getDataset.py');
$output = exec('python PolynomialSupportVectorregression.py 3');
echo "$output";

?>