/* Implementation of a dynamic array with int data type using JAVA */

public class DynamicArrayImplementation {
    // Arr is the Array to store the elements
    private int[] arr;
    // Num of elements currently stored in the array
    private int size;
    private static final int DEFAULT_ARRAY_CAPACITY = 20;

    public DynamicArrayImplementation() {
        arr = new int[DEFAULT_ARRAY_CAPACITY];
        size = 0;
    }

    public void addArrayElement(int ele) {
        if (size == arr.length) {
            // Resizing the array if it is full
            resizeArray();
        }
        // Adding the element at the end of the array and incrementing the array size of 1
        arr[size++] = ele;
    }
   
       // Removing the array element at the end  of array and gives the exception if array size out of bound
    public void removeArrayElement(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Array Index " + index + " out of the bounds for size " + size);
        }
        for (int i = index; i < size - 1; i++) {
            arr[i] = arr[i + 1];
        }
        size--;
    }

    // To Retrieve the array element index
    public int getArrayIndex(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Array Index " + index + " out of the bounds for size " + size);
        }
        return arr[index];
    }

    // Returning the number of elements present in the array
    public int size() {
        return size;
    }

    // To resize the array
    private void resizeArray() {
        int newArrayCapacity = arr.length * 2;
        int[] newArray = new int[newArrayCapacity];
        System.arraycopy(arr, 0, newArray, 0, size);
        arr = newArray;
    }

    public static void main(String[] args) {
        DynamicArrayImplementation dynamicArray = new DynamicArrayImplementation();

        // Adding the element to array
        dynamicArray.addArrayElement(56);
        dynamicArray.addArrayElement(13);
        dynamicArray.addArrayElement(25);
        dynamicArray.addArrayElement(47);
        dynamicArray.addArrayElement(89);
        

        System.out.println("The Size of the given array is: " + dynamicArray.size());

        dynamicArray.removeArrayElement(2);

        System.out.println("The array Size after removing the element from array: " + dynamicArray.size());

        System.out.println("The array Element at index 3: " + dynamicArray.getArrayIndex(3));
    }
}


/* OutPut:

 * The Size of the given array is: 5
 * The array Size after removing the element from array: 4
 * The array Element at index 3: 89

 */