#include <stdio.h>

int findMax(int arr[2][2], int row, int col) {
    // Base case: if we reach the last element of the array, return it
    if (row == 1 && col == 1) {
        return arr[row][col];
    }
    // Recursive case:
    // If we reach the last column of a row, move to the next row
    if (col == 1 && row != 1) {
        return findMax(arr, row + 1, 0);
    }
    // Otherwise, compare the current element with the maximum of the rest of the array
    int maxRest = findMax(arr, row, col + 1);
    if (arr[row][col] > maxRest) {
        return arr[row][col];
    } else {
        return maxRest;
    }
}

int main() {
    int arr[2][2] = {
            {7, 2,},
            {5, 6},
    };
    int max = findMax(arr, 0, 0);
    printf("The maximum element in the array is %d\n", max);
    return 0;
}
