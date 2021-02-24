let string = 'aabcccccaaa';

stringCompression('aabcccccaaa')


//compress string --> then compare lengths  
//don't repeatedly concatenate strings as this is inefficient 

function stringCompression(string) {
    //compress the string
    let newString = "";
    for (let i = 0; i < string.length; i++) {
        if (string[i] !== string[i - 1]) {
            newString += string[i];
        }
        if ((i === string.length - 1) && (string[i] === string[i - 1])) {

        } else if ((i === string.length - 1) && (string[i] !== string[i - 1])) {
            newString += string[i];
        }
        else {
            let myCount = 1;
            while (string[i] === string[i + myCount]) {
                myCount += 1;
            }
        }
    }


    //count
    let stringArray = string.split("")
    numbersArray = [];
    for (let i = 0; i < string.length; i++) {
        if (string[i] !== string[i - 1]) {
            let count = 1;
            while (string[i] === string[i + count]) {
                count++;
            }
            numbersArray.push(count)
        }
    }

    //join
    let numberString = numbersArray.toString()
    numberString = numberString.replace(/,/g, "")
    let jointString = [];
    for (let i = 0; i < newString.length; i++) {
        jointString += newString[i]
        jointString += numberString[i]
    }

    console.log(jointString)
    return jointString
}