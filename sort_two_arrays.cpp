#include<iostream>
using namespace std;

void sort_two_array(int arr1[], int size1, int arr2[], int size2) {
    int i = 0, j = 0;
    while (i < size1 && j < size2) {
        if (arr1[i] > arr2[j]) {
            // Swap arr1[i] with arr2[j]
            swap(arr1[i], arr2[j]);

            // After swapping, ensure that arr2 remains sorted
            // Bubble the element arr2[j] to its correct position in arr2
            for (int k = 0; k < size2 - 1; k++) {
                if (arr2[k] > arr2[k + 1]) {
                    swap(arr2[k], arr2[k + 1]);
                } else {
                    break; // Array is sorted, no need to swap further
                }
            }
        }
        i++; // Move to the next element in arr1
    }
}

// Function to display array
void display_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i];
        if (i != size - 1) {
            cout << ", ";
        }
    }
    cout << endl;
}

int main() {
    int choice;
    cout << "Enter your choice: \n1. Enter the elements of the array manually.\n2. Use predefined arrays." << endl;
    cin >> choice;
    
    if (choice == 1) {
        int m, n;
        cout << "Enter the size of the array 1: ";
        cin >> m;
        cout << "Enter the size of the array 2: ";
        cin >> n;
        
        int arr1[m], arr2[n];
        cout << "Enter the elements of the first array: ";
        for (int i = 0; i < m; i++) {
            cin >> arr1[i];
        }
        
        cout << "Enter the elements of the second array: ";
        for (int i = 0; i < n; i++) {
            cin >> arr2[i];
        }

        // Call sorting function and display the results
        sort_two_array(arr1, m, arr2, n);
        cout << "Sorted arrays are:" << endl;
        display_array(arr1, m);
        display_array(arr2, n);
    }
    else {
        int arr1[] = {1, 3, 5, 7};
        int arr2[] = {2, 4, 6, 8};
        int m = sizeof(arr1) / sizeof(arr1[0]);
        int n = sizeof(arr2) / sizeof(arr2[0]);
        
        sort_two_array(arr1, m, arr2, n);
        cout << "Sorted predefined arrays are:" << endl;
        display_array(arr1, m);
        display_array(arr2, n);
    }

    return 0;
}
