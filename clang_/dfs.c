#include<stdio.h>
#include<stdlib.h>
#include<stack.h>

/*
들어온 컴퓨터 대수 만큼 테이블 생성 -> ok
*/

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
    *graph = (int*)malloc(sizeof(int*)*com_max);
    //컴퓨터 연결쌍을 입력받는다.
    scanf("%d",&input_size);
    p1 = (int*)malloc(sizeof(int*)*input_size);
    p2 = (int*)malloc(sizeof(int*)*input_size);
    for(int i = 0; i < input_size; i++){
        scanf("%d %d",(p1+i),(p2+i));
    }   
}

int DFS(int start, int** graph, int size){
    그래프의 첫번째 요소부터 탐색을 시작.
    행렬을 탐색할때, 방문한 노드를 스택에 넣는다. 그리고 인접노드중 방문하지 않았고, 정렬된 것중 우선되는 노드에 방문한다.
    스택에 다시 넣는다. 만일 이미 방문한 노드라면 스킵하고 넣는다. 넣을게 없다면 그대로 pop을 한다.
    위를 반복하면 결국 top이 -1이 될 것.
}