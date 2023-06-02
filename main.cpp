// Write a recursive program to print an array of size in in reverse order
#include<iostream>
using namespace std;

void rev(int *arr,int n, int i){
    if(i<n){
        cout<<arr[n-1]<<" ";
        rev(arr, n-1, i);
    }
}

int main(){
    cout<<"Program started\n";
    int arr[] = {1,2,3,4};
    int n = sizeof(arr)/sizeof(arr[0]);
    int i = 0;
    rev(arr, n, i);
}
