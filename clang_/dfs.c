#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#define MAX_SIZE 100

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
    if(IsFull()==false)
        stack[++top] = val;
}
int pop(){
    if(IsEmpty()==false)
        return stack[top--];
    return -1;
}

void DFS(int start_vertex,int** graph,int* visited, int max_vertex){
    int connected_net=0;
    //시작정점을 방문
    push(start_vertex);
    visited[start_vertex] = true;
    while(IsEmpty()==false){
        int ver = pop();
        for(int i = 0; i<max_vertex; i++){
            //인접정점 마다 네트워크 카운트
            if(graph[ver][i]==1 && visited[i] == false){
                push(i);
                visited[i] = true;
                connected_net++;
            }
        }
    }
    printf("%d",connected_net);
}

int main(){
    int     com_max;
    int     input_size=0;
    int*    p1;
    int*    p2;

    int**   graph;
    int*    visited;
    //컴퓨터 대수를 입력받고 그 수에 맞춰 방문여부확인 플래그 생성.
    scanf("%d",&com_max);
    visited = (int*)malloc(sizeof(int*)*com_max);
    //이중포인터로 행렬 생성.
    graph = (int**)malloc(sizeof(int**)*com_max);
    for(int i=0; i<com_max; i++)
        graph[i] = (int*)malloc(sizeof(int*)*com_max);
    //컴퓨터 연결쌍을 입력받는다.
    scanf("%d",&input_size);
    p1 = (int*)malloc(sizeof(int*)*input_size);
    p2 = (int*)malloc(sizeof(int*)*input_size);
    for(int i = 0; i < input_size; i++){
        scanf("%d %d",(p1+i),(p2+i));
        graph[*(p1+i)-1][*(p2+i)-1]=1;
        graph[*(p2+i)-1][*(p1+i)-1]=1;
    }
    DFS(0,graph,visited,com_max);
}