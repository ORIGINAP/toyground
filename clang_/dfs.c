#include<stdio.h>
#include<stdlib.h>
//#include<stack.h>

/*
들어온 컴퓨터 대수 만큼 테이블 생성 -> ok


*/
int main(){
    int     com_max;
    int     input_size=0;
    int*    p1;
    int*    p2;

    int*     visited;

    scanf("%d",&com_max);
    visited = (int*)malloc(sizeof(int*)*com_max);
    scanf("%d",&input_size);
    p1 = (int*)malloc(sizeof(int*)*input_size);
    p2 = (int*)malloc(sizeof(int*)*input_size);
    for(int i = 0; i < input_size; i++){
        scanf("%d %d",(p1+i),(p2+i));
    }
    
    for(int i = 0; i < input_size; i++){
        printf("%d %d\n",*(p1+i),*(p2+i));
    }
}