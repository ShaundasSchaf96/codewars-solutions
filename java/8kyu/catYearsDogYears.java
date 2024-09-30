"""Kata Task
I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1
humanYears are whole numbers only

Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that

Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that""";

public class Dinglemouse {
    public static int[] humanYearsCatYearsDogYears(final int humanYears) {
        int catYears = 0;
        int dogYears = 0;
        switch (humanYears) {
            case 1:
                catYears = 15;
                dogYears = 15;
            break;
            case 2:
                catYears = 15 + 9;
                dogYears = 15 + 9;
            break;
            default:
            if (humanYears >= 3) {
                catYears = 15 + 9 + 4 * (humanYears - 2);
                dogYears = 15 + 9 + 5 * (humanYears - 2);
            };
        }
        return new int[]{humanYears,catYears,dogYears};
    }
}