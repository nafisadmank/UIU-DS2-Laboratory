//Write a recursive program to solve the Tower of Hanoi problem for n disks.
#include<iostream>
using namespace std;

int tower_of_hanoi(int no_of_disks){
    if (no_of_disks<=0)
        return 0;
    else {
        int no_of_moves = 2 * tower_of_hanoi(no_of_disks - 1) + 1;
        return no_of_moves;
    }
}

int main(){
    //cout<<"Input:\t";
    int value=3;
    //cin>>value;
    cout<<"Number of Moves Required: "<<tower_of_hanoi(value);
}
