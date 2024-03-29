#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct List{ int data; struct List* next;} List;

List* add_list(int p_node, List* src){
    List* n_node;
    List* origin_node;

    n_node = (List*)malloc(sizeof(List));
    origin_node = src;
    n_node->data = p_node;
    n_node->next = NULL;
    while(src->next){
        printf("%p\n",src);
        src = src->next;
    }
    src->next = n_node;
    return origin_node;
}

void freeall(List* src){
    while(src){
        List* temp = src->next;
        free(src);
        src = temp;
    }
}

int main(){
    List* test;
    
    test = (List*)malloc(sizeof(test));
    test->data = 1;
    test->next = NULL;

    for(int i = 0; i < 10; i++){
        test = add_list(i,test);
    }
    while (test)
    {
        printf("%d\n", test->data);
        test = test->next;
    }
    freeall(test);
}