<?php

$string = "anna";

for($i=0; $i<strlen($string); $i++) {
	for($s=0; $s<strlen($string); $s++) {
		if($s==$i)
			continue;
		if(strtolower($string[$i])==strtolower($string[$s])) {
			throw new Exception("String is not unique at position ".$i +1 ." and ".$s +1);
		}
	}
}
echo "String is unique";