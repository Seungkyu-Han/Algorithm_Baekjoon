#include <stdio.h>

int max(int a, int b);
int max_arr(int arr[], int size);

int main(void){
    int cnt;
    scanf("%d", &cnt);

    int arr[1000] = {0};
    for (int i = 0; i < cnt; i++){
        scanf("%d", &arr[i]);
    }
    int res[1000] = {0};
    for (int i = 0; i < cnt; i++){
        res[i] = 1;
        for (int j = 0; j < i; j++){
            if (arr[i] > arr[j]){
                res[i] = max(res[i], res[j]+1);
            }
        }
    }
    printf("%d", max_arr(res, cnt));


    return 0;
}

int max(int a, int b){
    return (a > b) ? a : b;
}

int max_arr(int arr[], int size){
    int max = 0;
    for (int i = 0; i < size; i++){
        if (arr[i] > max){
            max = arr[i];
        }
    }

    return max;
}
