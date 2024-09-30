"""Description:
Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.""";

public class MostDigits {
    public static int findLongest(int[] numbers) {
      int maxCount = -1;
      int numWithMostDigits = -1;
      for(int num : numbers){
        int count = (int)Math.log10(Math.abs(num)) + 1;
        if(count > maxCount){
            maxCount = count;
            numWithMostDigits = num;
            }
        }
        return numWithMostDigits;
    }
}