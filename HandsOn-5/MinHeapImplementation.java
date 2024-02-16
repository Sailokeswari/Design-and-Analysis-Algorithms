// Implementation of a Min Heap data structure

import java.util.ArrayList;
import java.util.List;

public class MinHeapImplementation<T extends Comparable<T>> {
    private List<T> heap;

    public MinHeapImplementation() {
        heap = new ArrayList<>();
    }

     // parent method to represent the indices of the parent nodes
     
    private int parent(int i) {
        return (i - 1) >> 1;
    }

     // left method to represent the indices of the left child nodes
     
    private int left(int i) {
        return (i << 1) + 1;
    }

     // right method to represent the indices of the right child nodes
     
    private int right(int i) {
        return (i << 1) + 2;
    }

     // it moves a node up the heap if child node value is less than its parent node
     
    private void heapifyUp(int i) {
        while (i > 0 && heap.get(parent(i)).compareTo(heap.get(i)) > 0) {
            swap(i, parent(i));
            i = parent(i);
        }
    }
    
     // it moves a node down the heap if child node value is greater than its parent node
     
    private void heapifyDown(int i) {
        int smallest = i;
        int l = left(i);
        int r = right(i);
        if (l < heap.size() && heap.get(l).compareTo(heap.get(smallest)) < 0)
            smallest = l;
        if (r < heap.size() && heap.get(r).compareTo(heap.get(smallest)) < 0)
            smallest = r;
        if (smallest != i) {
            swap(i, smallest);
            heapifyDown(smallest);
        }
    }

     // it builds the min heap from the given array elements
     
    public void build_Min_Heap(List<T> arr) {
        heap = new ArrayList<>(arr);
        for (int i = heap.size() / 2 - 1; i >= 0; i--) {
            heapifyDown(i);
        }
    }
    
     // it will returns the root node of the heap
     
    public T getRootNode() {
        return heap.isEmpty() ? null : heap.get(0);
    }
   
     // it inserts a new array element into the heap
     
    public void insert(T value) {
        heap.add(value);
        heapifyUp(heap.size() - 1);
    }
     
     // it removes the root node from the heap
     
    public T popRoot() {
        if (heap.isEmpty())
            return null;
        T root = heap.get(0);
        heap.set(0, heap.get(heap.size() - 1));
        heap.remove(heap.size() - 1);
        heapifyDown(0);
        return root;
    }

    private void swap(int i, int j) {
        T temp = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, temp);
    }

    public static void main(String[] args) {
       
       // implementation for min heap of integer data type
        
        MinHeapImplementation<Integer> heap1 = new MinHeapImplementation<>();
        List<Integer> arr1 = List.of(6, 8, 4, 3, 9, 1, 7);
        heap1.build_Min_Heap(arr1);
        System.out.println("Initial build_min_heap of Integers: " + heap1.heap);

      // adding element 2 to the heap

        heap1.insert(2);
        System.out.println("Heap after insertion of element 2 to heap: " + heap1.heap);

        Integer root1 = heap1.popRoot();
        System.out.println("Popping Root Node: " + root1);
        System.out.println("Min Heap after removing root node: " + heap1.heap);
        
         // implementation for min heap of float data type
        
        MinHeapImplementation<Float> heap = new MinHeapImplementation<>();
        List<Float> arr = List.of(8.4f, 6.2f, 1.2f, 4.7f, 8.9f, 3.6f, 5.3f);
        heap.build_Min_Heap(arr);
        System.out.println("Initial build_min_heap of Float: " + heap.heap);

        // adding element 2.1f to the heap
        
        heap.insert(2.1f);
        System.out.println("Heap after insertion of element 2.1f to heap: " + heap.heap);

        Float root = heap.popRoot();
        System.out.println("Popping Root Node: " + root);
        System.out.println("Min Heap after removing root node: " + heap.heap);
        
        
         // implementation for min heap of Custom datastructure
    
        MinHeapImplementation<CustomObject> minHeapCustomDS = new MinHeapImplementation<>();
        List<CustomObject> objects = new ArrayList<>();
        objects.add(new CustomObject(9));
        objects.add(new CustomObject(3));
        objects.add(new CustomObject(5));
        objects.add(new CustomObject(2));
        objects.add(new CustomObject(7));
        objects.add(new CustomObject(1));

        minHeapCustomDS.build_Min_Heap(objects);
        System.out.println("\nMin Heap (Custom Objects): " + minHeapCustomDS.heap);
        System.out.println("Root Node: " + minHeapCustomDS.getRootNode());
        System.out.println("Popping Root: " + minHeapCustomDS.popRoot());
        System.out.println("Min Heap after popping root: " + minHeapCustomDS.heap);
    }
 
        static class CustomObject implements Comparable<CustomObject> {
        private int value;

        public CustomObject(int value) {
            this.value = value;
        }

        @Override
        public int compareTo(CustomObject o) {
            return Integer.compare(this.value, o.value);
        }

        @Override
        public String toString() {
            return "CustomObject{" +
                    "value=" + value +
                    '}';
        } 
        }
}


/*
 * Output:
 * For Integer Datatype
 Initial build_min_heap of Integers: [1, 3, 4, 8, 9, 6, 7]
Heap after insertion of element 2 to heap: [1, 2, 4, 3, 9, 6, 7, 8]
Popping Root Node: 1
Min Heap after removing root node: [2, 3, 4, 8, 9, 6, 7]

* For Float Datatype
Initial build_min_heap of Float: [1.2, 4.7, 3.6, 6.2, 8.9, 8.4, 5.3]
Heap after insertion of element 2.1f to heap: [1.2, 2.1, 3.6, 4.7, 8.9, 8.4, 5.3, 6.2]
Popping Root Node: 1.2
Min Heap after removing root node: [2.1, 4.7, 3.6, 6.2, 8.9, 8.4, 5.3]

* For Custom Datastructure
Min Heap (Custom Objects): [CustomObject{value=1}, CustomObject{value=2}, CustomObject{value=5}, CustomObject{value=3}, CustomObject{value=7}, CustomObject{value=9}]
Root Node: CustomObject{value=1}
Popping Root: CustomObject{value=1}
Min Heap after popping root: [CustomObject{value=2}, CustomObject{value=3}, CustomObject{value=5}, CustomObject{value=9}, CustomObject{value=7}]
 */