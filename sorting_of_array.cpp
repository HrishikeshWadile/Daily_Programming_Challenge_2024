#include<iostream>
using namespace std;

// FUNCTION TO PRINT AN GIVEN ARRAY 
void print_array(int array[], int n){
    for (int i = 0; i < n; i++){
        cout << array[i] << "  ";
    }
    cout << endl;
}

// FUNCTION TO SORT A ARRAY USING BUBBLE SORT
void bubble_sort(int arr[], int n){
    for (int i = 0; i < n - 1; i++){
        for (int j = 0; j < n - i - 1; j++){
            if (arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
        // print_array(arr, n);
    }   
    cout << "Bubble Sorted array: ";
    print_array(arr, n);
}

int main(){
    int numbers[]= {0 ,1 ,2 ,1 ,0 ,2 ,1 ,0 }; // DEFINITION OF THE ARRAY
    int n = sizeof(numbers)/sizeof(numbers[0]); // COMMAND TO RETRIVE SIZE OF THE ARRAY
    cout << "Unsorted array: ";
    print_array(numbers, n);
    bubble_sort(numbers, n);

    return 0;
}
