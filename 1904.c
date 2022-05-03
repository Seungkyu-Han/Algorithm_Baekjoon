#include <stdio.h>

int main(void){

    int num;
    scanf("%d", &num);

    if (num == 1){
        printf("%d", 1);
        return 0;
    }
    else if(num == 2){
        printf("%d", 2);
    }
    else{
        long long result[1000000] = {0};
        result[0] = 1;
        result[1] = 2;
        for (int i = 2; i < num; i++){
            result[i] = (result[i-1] + result[i-2]) % 15746;
        }
        printf("%lld", result[num - 1]);
    }

}
