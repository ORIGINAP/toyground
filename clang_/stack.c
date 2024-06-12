#include<stdio.h>
#include<stdbool.h>
#include<stack.h>
#define MAX_SIZE 5

int stack[MAX_SIZE];
int top = -1;

int IsEmpty(){
    if(top<0)
        return true;
    else
        return false;
}

int IsFull(){
    if(top == MAX_SIZE-1)
        return true;
    else
        return false;
}

void push(int val){
    if(IsFull()==true)
        printf("Stack is full");
    else
        stack[++top] = val;
}

int pop(){
    if(IsEmpty()==true)
        printf("Stack is Empty");
    else
        return stack[top--];
    return -1;
}