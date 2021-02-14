<?php

function permutation($string1, $string2) {
$is_palindrom = true;
for($i=0; $i<strlen($string1); $i++) {
	$found = false;
	for($s=0; $s<strlen($string2); $s++) {
		if(strtolower($string1[$i])==(strtolower($string2[$s]))) {
			$found = true;
			break;
		}
		
	}
	if($found==false) {
		return "Is not a Permutation";
	}
}
return "is a permutation";
	
}
echo permutation("abcd", "dabc");