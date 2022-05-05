#include <stdio.h>

int main(void){

    int resarr[21][21][21];
    
    for (int i = 0; i < 21; i++){
        for (int j = 0; j < 21; j++){
            for (int k = 0; k < 21; k++){
                if (i == 0 || j == 0 | k == 0){
                    resarr[i][j][k] = 1;
                }
                else if (i < j && j < k){
                    resarr[i][j][k] = resarr[i][j][k-1] + resarr[i][j-1][k-1] - resarr[i][j-1][k];
                }
                else{
                    resarr[i][j][k] = resarr[i-1][j][k] + resarr[i-1][j-1][k] + resarr[i-1][j][k-1] - resarr[i-1][j-1][k-1];
                }
            }
        }
    }

    int a = 0, b = 0, c = 0;
    scanf("%d %d %d", &a, &b, &c);
    while(!(a == -1 && b == -1 && c == -1)){
        if (a <= 0 || b <= 0 || c <= 0){
            printf("w(%d, %d, %d) = %d\n", a, b, c, 1);
        }
        else if (a > 20 || b > 20 || c > 20){
            printf("w(%d, %d, %d) = %d\n", a, b, c, resarr[20][20][20]);
        }
        else{
            printf("w(%d, %d, %d) = %d\n", a, b, c, resarr[a][b][c]);
        }
        scanf("%d %d %d", &a, &b, &c);
    }

    return 0;
}
