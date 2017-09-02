<?php
set_time_limit(0);

//$output = shell_exec('python getDataset.py');
$output = exec('python radialBasisFunctionModelSVM.py 5');
echo "$output";

?>