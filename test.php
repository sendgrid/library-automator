<?php
$query_params = array('limit' => 100, 'offset' => 0);
print_r($query_params);
$query_params = json_decode('{"end_date": "2016-04-01", "aggregated_by": "day"}', true);
print_r($query_params);