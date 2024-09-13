
#include <iostream>
#include <vector>
using namespace std;

// Function to find leader elements in the array
vector<int> find_leaders(int array[], int size) {
    vector<int> leaders;
    
    // Start from the last element, which is always a leader
    int leader = array[size - 1];
    leaders.push_back(leader); // Add the last element as a leader
    
    // Traverse the array from second last to the first element
    for (int i = size - 2; i >= 0; i--) {
        if (array[i] > leader) {
            leader = array[i];
            leaders.push_back(leader); // Add the leader element
        }
    }
    
    return leaders; // Return the list of leader elements
}

int main() {
    
    int choice;
    cout << "Enter your choice: \n1. Enter the elements of the array manually.\n2. Use predefined arrays." << endl;
    cin >> choice;
    
    if (choice == 1) {
        int n;
        
        cout << "Enter the size of the array: ";
        cin >> n;
        
        int array[n];
        int size = sizeof(array) / sizeof(array[0]);
        cout << "Enter the elements of the array: ";
        for (int i = 0; i < n; i++) {
            cin >> array[i];
        }

        vector<int> leaders = find_leaders(array, size);
        
        cout << "Leader elements: ";
        // Print the leader elements in reverse order as we pushed them from right to left
        for (int i = leaders.size() - 1; i >= 0; i--) {
            cout << leaders[i] << " ";
        }
    }
    else {
        int array[] = {16, 17, 4, 3, 5, 2};
        int size = sizeof(array) / sizeof(array[0]);

        vector<int> leaders = find_leaders(array, size);
        
        cout << "Leader elements: ";
        // Print the leader elements in reverse order as we pushed them from right to left
        for (int i = leaders.size() - 1; i >= 0; i--) {
            cout << leaders[i] << " ";
        }
    }

    return 0;
}
