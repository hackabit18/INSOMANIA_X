<?php
$db = new Mysqli;
$db ->connect('localhost','root','','rajasthan',3306);
if(!$db)
{
    echo "Error Occured";
}
?>