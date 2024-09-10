#include<iostream>
using namespace std;

// Function to find the missing number in the range from 1 to n in n-1 size array
int find_missing_number(int arr[], int size){
    int check = 1;
    for (int i = 0; i < size; i++) {
        if (arr[i] == check) {
            check++; // Move to the next expected number
        }
    }
    // If check is still equal to size + 1, it means no number is missing
    if (check == size + 1) {
        return -1; // Indicates no missing element
    }
    return check; // The missing number is the one not matched
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
            cout << "With an array of size 1, it's not possible to determine a missing number in the range.\n";
            return 1;
        }
        
        int arr[n];
        for (int i = 0; i < n; i++){
            cout << "Enter the element " << i+1 << " of the array: "; // Inputing the  elements in array
            cin >> arr[i];
        }
        cout << "Array: ";
        display_array(arr, n);
        int missing = find_missing_number(arr, n);
        if (missing == -1) {
            cout << "\nNo missing element in the range.";
        } 
        else {
            cout << "\nMissing element in the range: " << missing;
        }

    }
    else{
        int numbers[]= {1, 2, 4, 5}; // Predefined array
        int n = sizeof(numbers)/sizeof(numbers[0]); // Calculating the size of the array
        cout << "Array: ";
        display_array(numbers, n);
        int missing = find_missing_number(numbers, n);
        if (missing == -1) {
            cout << "\nNo missing element in the range.";
        } 
        else {
            cout << "\nMissing element in the range: " << missing;
        }
    return 0;
    }
}
