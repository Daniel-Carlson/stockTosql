<?php

// This File connects to a SQL DB runs a query 


include('db_connect.php');

$sql  = 'SELECT `id`,`day`,`total_value`,`total_change` FROM total;';

//execute the query

$statement = $connect->prepare($sql);
$statement->execute();


$result= $statement->fetchAll();
//loop through the returned data
$data = array();
foreach ($result as $row) {
	$data1['id'] = $row['id'];
	$data1['day'] = $row['day'];
	$data1['total_value'] = $row['total_value'];
	$data1['total_change'] = $row['total_change'];
	
	array_push($data,$data1);
}

//print the json data
print json_encode($data);

?>

