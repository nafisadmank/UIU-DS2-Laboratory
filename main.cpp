// Write a recursive program to check if a given string is a palindrome or not.
#include <iostream>
using namespace std;
#include <cstring>

int palindrome(char *my_string,int start,int end){
    if(start >= end){
        return 1;
    }
    else if(my_string[start] == my_string[end]){
        return palindrome(my_string,start+1,end-1);
    }
    return 0;
}
int main() {
    char my_string[] = "aba";
    int length = strlen(my_string);
    int binary = palindrome(my_string,0,length-1);
    if(binary==1)
        cout<<"This is Palindrome";
    else
        cout<<"This is not a Palindrome";
    return 0;
}
