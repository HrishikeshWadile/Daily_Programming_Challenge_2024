#include<iostream>
using namespace std;

// Function to search duplicate element in the array
int search_duplicate(int array[], int size){
    for (int i = 0; i < size - 1; i++){
        int check = array[i];
        for (int j = i + 1; j < size; j++){
            if (array[j] == check){ 
                return check; // If duplicate found return the number
            }
        }
    }
    return -1; // If duplicate not foun, return -1
}

// Function to display array 
void display_array(int arr[], int size){
    for (int i = 0; i < size; i++){
        cout << arr[i] << " ";
        if (i != size - 1){
            cout << ", ";
        }
    }
}

int main(){
    string ans;
    cout << "If to input your own array enter 'y'\nElse enter any other key if you want to take a sample example array\nEnter your answer: "; // Asking user to use pre-defined array or create their own array and use
    cin >> ans;
    if (ans == "y"){
        int n;
        cout << "Enter the size of the array: "; // Input for the size of the array
        cin >> n;

        if (n <= 0){
            cout << "Array size must be positive.\n";
            return 1;
        }
        if (n == 1){
            cout << "With an array of size 1, it's not possible to determine a duplicate number in the range.\n";
            return 1;
        }
        
        int arr[n];
        for (int i = 0; i < n; i++){
            cout << "Enter the element " << i+1 << " of the array: "; // Inputing the  elements in array
            cin >> arr[i];
        }
        cout << "Array: ";
        display_array(arr, n);
        int duplicate = search_duplicate(arr, n);
        if (duplicate == -1) {
            cout << "\nNo duplicate element in the range.";
        } 
        else {
            cout << "\nDuplicate element in the range: " << duplicate;
        }

    }
    else{
        int numbers[]= {3, 1, 3, 4, 2}; // Predefined array
        int n = sizeof(numbers)/sizeof(numbers[0]); // Calculating the size of the array
        cout << "Array: ";
        display_array(numbers, n);
        int duplicate = search_duplicate(numbers, n);
        if (duplicate == -1) {
            cout << "\nNo duplicate element in the range.";
        } 
        else {
            cout << "\nDuplicate element in the range: " << duplicate;
        }
    return 0;
    }
}
