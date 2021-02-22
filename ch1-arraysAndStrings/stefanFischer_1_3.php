<?php

function palindrom($string) {
$string = str_replace(' ', '', $string);	
for($i=0; $i<strlen($string); $i++) {
	if(strtolower($string[$i])!=(strtolower($string[strlen($string)-1-$i]))) {
		return "Is not a Palindrom";
	}
}
return "is a palindrom";
	
}
echo palindrom("A nut for a jar of tunat");