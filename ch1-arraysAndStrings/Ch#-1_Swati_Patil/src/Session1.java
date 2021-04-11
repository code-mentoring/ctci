public class Session1 {
//    Questions: 1.1:

    public boolean checkUniqueChars(String string){
        if(string.length()<2){
            return true;
        }
        else if (string.substring(1).contains(string.substring(0, 1))) {
            return false;
        }
           return checkUniqueChars(string.substring(1));
    }

//    Questions: 1.2:

    public boolean checkPermutation(String str, String permStr){
        if(permStr.length()<=1){
            return true;
        }
        else if(!str.contains(permStr.substring(0,1))){
            return false;
        }
        return checkPermutation(str, permStr.substring(1));
    }
//    Questions: 1.3:
private boolean checkPalindromePermutation(String string) {
    boolean flag = false;
    for (int i = 0, j = string.length() - 1; i < string.length() & j >= 0; i++, j--) {
        if (string.charAt(i) == string.charAt(j)) {
            flag = true;
        } else {
            flag = false;
            break;
        }
    }
    return flag;
}

}
