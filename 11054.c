#include <stdio.h>

int max(int a,int b);

int main(void){

    int ans[1000];
    int revans[1000];
    int left[1000];
    int right[1000];

    int cnt;
    scanf("%d", &cnt);
    
    for (int i = 0; i < cnt; i++){
        scanf("%d", &ans[i]);
        revans[cnt - i - 1] = ans[i];
    }
    for (int i = 0; i < cnt; i++){
        left[i] = 1;
        for (int j = 0; j < i; j++){
            if (ans[i] > ans[j]){
                left[i] = max(left[i], left[j] + 1);
            }
        }
    }
    for (int i = 0; i < cnt; i++){
        right[i] = 1;
        for (int j = 0; j < i; j++){
            if (revans[i] > revans[j]){
                right[i] = max(right[i], right[j] + 1);
            }
        }
    }
    int max_num = 0;

    for (int i = 0; i < cnt; i++){
        if (max_num < left[i] + right[cnt - 1 - i] - 1){
            max_num = left[i] + right[cnt - 1 - i] - 1;
        }
    }


    printf("%d", max_num);
}

int max(int a, int b){
    return (a > b) ? a : b;
}
