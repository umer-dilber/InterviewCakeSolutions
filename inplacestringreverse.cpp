#include <iostream>
using namespace std;

void swapChar(char &a, char &b){
    char temp = a;
    a = b;
    b = temp;
}

void reverseString(string &str){
    int last = str.length();
    int first = 0;
    while(first < last){
        swapChar(str[first], str[last]);
        first++;
        last--;
    }
}

int main(){
    string originalStr = "Jack";
    reverseString(originalStr);
    cout << originalStr << endl;
    return 0;
}