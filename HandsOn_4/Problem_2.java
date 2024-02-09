// Given a sorted array array of size N, the task is to remove the duplicate elements from the array.

import java.util.Scanner;
import java.util.Arrays;

public class RemoveDuplicateElementsFromArray {
    public static void main(String[] args) {
        
        // Taking the input from user
        Scanner scanner = new Scanner(System.in);
       
       // Taking input of array size N as user input 
        System.out.print("Enter size of the array elements: ");
        int size = scanner.nextInt();
        
        // Taking the array elements as input to remove duplicates
        int[] arr = new int[size];
        System.out.println("Enter the elements to remove duplicates from sorted array:");
        for (int i = 0; i < size; i++) {
            arr[i] = scanner.nextInt();
        }
        
        int[] originalArray = Arrays.copyOf(arr, size);
        int[] outputArray = removeDuplicates(arr);
        
        // Printing the Original and Output arrays 
        System.out.println("Original Array before removing duplicate elements: " + Arrays.toString(originalArray));
        System.out.println("Output Array after removing duplicates elements: " + Arrays.toString(outputArray));
    }

    public static int[] removeDuplicates(int[] arr) {
        if (arr.length == 0 || arr.length == 1) {
            return arr;
        }
        
       // tracking elements index
        int uniqueVal = 0;
        
        // moving unique elements to the beginning
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] != arr[uniqueVal]) {
                uniqueVal++;
                arr[uniqueVal] = arr[i];
            }
        }

        // copying and returing only unique elements
        return Arrays.copyOf(arr, uniqueVal + 1);
    }
}

/*Output:
 Enter size of the array elements: 10
Enter the elements to remove duplicates from sorted array:
2 3 3 4 5 6 7 7 8 9
Original Array before removing duplicate elements: [2, 3, 3, 4, 5, 6, 7, 7, 8, 9]
Output Array after removing duplicates elements: [2, 3, 4, 5, 6, 7, 8, 9]

 */