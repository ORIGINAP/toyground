#include <stdio.h>

void main(){
    int arr[2][3][4];
    int i,j,k,value = 1;
    for(i=0; i<2; i++){
        for(j=0; j<3; j++){
            for(k=0; k<4; k++){
                arr[i][j][k] = value;
                printf("arr[%d][%d][%d] = %d\n", i,j,k,arr[i][j][k]);
            }
        }
    }
}