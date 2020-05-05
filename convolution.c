#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define kernalMAX 3
#define matrixMAX 5
int kernal[kernalMAX][kernalMAX];
int matrix[matrixMAX+2][matrixMAX+2];// extra 1 for margin
int rmatrix[matrixMAX][matrixMAX];

int convoSum(int i,int j);


int main()
{
    memset(matrix,0,sizeof(matrix));
    memset(kernal,0,sizeof(kernal));
    memset(rmatrix,0,sizeof(rmatrix));
    printf("Initialize smooth_kernal\n");
    for(int i=0;i<kernalMAX;i++){
        for(int j=0;j<kernalMAX;j++)
            scanf("%d",&kernal[i][j]);
    }
    printf("kernal\n");
    for(int i=0;i<kernalMAX;i++){
        for(int j=0;j<kernalMAX;j++)
            printf("%4d",kernal[i][j]);
        printf("\n");
    }
    /*对卷积核需要一个上下翻转和左右翻转操作*/
    printf("Initialize image_matrix to 0\n");
    
    printf("Input the image_matrix\n ");
    for(int i=1;i<=matrixMAX;i++){
        for(int j=1;j<=matrixMAX;j++)
            scanf("%d",&matrix[i][j]);
    }
    for(int i=0;i<matrixMAX+2;i++){
        for(int j=0;j<matrixMAX+2;j++)
            printf("%4d",matrix[i][j]);
        printf("\n");
    }
    /*Test for correct*/
    /*carry out 滑动卷积计算*/
    for(int i=0;i<matrixMAX;i++){
        for(int j=0;j<matrixMAX;j++)
            rmatrix[i][j]=convoSum(i+1,j+1);//这里的索引遍历范围.
    }
    printf("after convolution\n");
    for(int i=0;i<matrixMAX;i++){
        for(int j=0;j<matrixMAX;j++)
            printf("%4d",rmatrix[i][j]);
        printf("\n");
    }


    return 0;
}
/*这里求卷积应该还有一个更一般的形式*/
int convoSum(int i,int j){
    int res1=matrix[i-1][j-1]*kernal[0][0]+matrix[i-1][j]*kernal[0][1]+matrix[i-1][j+1]*kernal[0][2];
    int res2=matrix[i][j-1]*kernal[1][0]+matrix[i][j]*kernal[1][1]+matrix[i][j+1]*kernal[1][2];
    int res3=matrix[i+1][j-1]*kernal[2][0]+matrix[1+i][j]*kernal[2][1]+matrix[i+1][j+1]*kernal[2][2];
    return res1+res2+res3;
}
