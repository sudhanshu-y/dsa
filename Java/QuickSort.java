import java.util.Arrays;

class QuickSort{
    public static void main(String[] args) {
        int arr[] = new int[]{1, 7, 4, 1, 10, 9, -2};
        // int arr[] = new int[]{0, -2, 80, 80, 3, 3};
        System.out.println(Arrays.toString(arr));

        quickSort(arr, 0, arr.length-1);
        System.out.println(Arrays.toString(arr));
    }
        
    private static void quickSort(int[] arr, int low, int high) {
        if(low<high){
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }
            
    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];

        // index which will divide left and right subarray
        // initially there will be no left subarray
        int i = low - 1;

        // if element smaller than pivot found then swap bigger element of left with smaller element 
        for(int j=low;j<high;j++){
            if(arr[j]<=pivot){
                i++;
                swap(arr, i, j);
            }
        }

        // swap next pivot index - (i+1) element with last/pivot element 
        swap(arr, i+1, high);

        return i + 1;
    }

    private static void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }
    
}