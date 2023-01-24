<?php
date_default_timezone_set("Asia/Jakarta");
$proxy= file_get_contents('https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt');
$selek= explode("\n", $proxy)[rand(0,150)];
file_put_contents("proxy.txt", $selek);
$myfile = fopen("last.txt", "w") or die("Unable to open file!");
$txt = "Last Update On " . date("Y-m-d  h:i:sa");
fwrite($myfile, $txt);
fclose($myfile);
?>
