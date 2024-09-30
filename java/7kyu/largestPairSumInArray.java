"""Description:
Given a sequence of numbers, find the largest pair sum in the sequence.

For example

[10, 14, 2, 23, 19] -->  42 (= 23 + 19)
[99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
Input sequence contains minimum two elements and every element is an integer.""";

import java.util.Arrays;
import java.util.OptionalInt;

public class Solution{
    public static int largestPairSum(int[] numbers){
        OptionalInt max1 = Arrays.stream(numbers).max();
        int num1 = max1.getAsInt();
        long countNum1 = Arrays.stream(numbers).filter(num -> num == num1).count();
        if (countNum1 > 1) {
            return num1 + num1;
        }
        OptionalInt max2 = Arrays.stream(numbers)
                          .filter(num -> num != num1)
                          .max();
        int num2 = max2.getAsInt();
        return num1 + num2;
    }
}