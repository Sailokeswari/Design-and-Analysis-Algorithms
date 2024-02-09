// Given K sorted arrays of size N each, the task is to merge them all maintaining their sorted order.

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class SortedArraysMerge {
    public static void main(String[] args) {
        
        // Taking the input from user
        Scanner scanner = new Scanner(System.in);
        
        // Taking input of number of sorted arrays of Size K as input
        System.out.println("Enter the number of Sorted Arrays:");
        System.out.print("K = ");
        int K = scanner.nextInt();
        
        // Taking input of each array size from user
        System.out.println("Enter the size of each array:");
         System.out.print("N = ");
        int N = scanner.nextInt();
        
        scanner.nextLine();
        
        // Creating ArrayList to store the sorted arrays
        ArrayList<Integer> sortedArr = new ArrayList<>();
        
        for (int i = 0; i < K; i++) {
            System.out.print("Enter sorted array elements:");
            String[] input = scanner.nextLine().split(" ");
            for (String num : input) {
                try {
                    sortedArr.add(Integer.parseInt(num));
                } catch (NumberFormatException e) {
                    System.out.println("Please enter only integer values");
                    return;
                }
            }
        }
        
        int[] mergedArrElements = mergeSortedArrays(sortedArr);
        
        // Printing the merged array in a sorted order
        System.out.print("Merged and Sorted array Elements:");
        for (int num : mergedArrElements) {
            System.out.print(num + " ");
        }
    }
    
    public static int[] mergeSortedArrays(ArrayList<Integer> arrays) {
        int[] mergedArrElements = new int[arrays.size()];
        int index = 0;
        for (int num : arrays) {
            mergedArrElements[index++] = num;
        }
        Arrays.sort(mergedArrElements);
        return mergedArrElements;
    }
}


/* Output:

Enter the number of Sorted Arrays:
K = 5
Enter the size of each array:
N = 4
Enter sorted array elements:2 4 6 7
Enter sorted array elements:3 6 9 10
Enter sorted array elements:0 2 5 9
Enter sorted array elements:4 5 8 15
Enter sorted array elements:11 15 16 20
Merged and Sorted array Elements:0 2 2 3 4 4 5 5 6 6 7 8 9 9 10 11 15 15 16 20

*/
