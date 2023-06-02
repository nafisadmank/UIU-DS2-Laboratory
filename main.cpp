// Write a recursive program to find the sum of the elements of an array of size n 
#include<iostream>
using namespace std;

int sum(int *arr,int n){
    if (n==1){
        return arr[0];
    }else{
        return arr[n-1]+sum(arr,n-1);   
    }
}

int main(){
    cout<<"Program started\n";
    int arr[] = {1,2,3,4};
    int n = sizeof(arr)/sizeof(arr[0]);
    int result = sum(arr, n);
    cout<<result;
}
