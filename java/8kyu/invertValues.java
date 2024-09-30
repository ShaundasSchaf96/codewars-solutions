"""Description:
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []""";

public class Kata {
    public static int[] invert(int[] array) {
    if(array.length == 0){
        return new int[0];
    }else{
        for(int i = 0; i<array.length; i++){
            array[i] = -array[i];
        }
        return array;
        }
    }
}