<?php

//$output = shell_exec('python getDataset.py');
$output = exec('python getDataset.py');
echo "$output";

?>