 <?php
$myfile = fopen("https://docs.google.com/spreadsheets/d/e/2PACX-1vRrYePMLyI58kvYWZ2icXi3Fe8LZxUNS29clJfwoz3Jjh5mMwMoJemOzMz86fkJoBYtkRcK8fs4JUms/pub?output=tsv", "r") or die("Unable to open file!");
echo fread($myfile,filesize("https://docs.google.com/spreadsheets/d/e/2PACX-1vRrYePMLyI58kvYWZ2icXi3Fe8LZxUNS29clJfwoz3Jjh5mMwMoJemOzMz86fkJoBYtkRcK8fs4JUms/pub?output=tsv"));
fclose($myfile);
?> 