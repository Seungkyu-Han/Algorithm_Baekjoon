#include <stdio.h>

long long max_result(int, int);
long long max(long long, long long, long long);

long long squ[100000];

int main(void){

    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) scanf("%lld", &squ[i]);

    long long final_result = max_result(0, N - 1);

    printf("%lld", final_result);

    return 0;
}

long long max_result(int start, int end){
    if (start > end) return 0;

    if (start == end) return squ[start];

    int mid = (start + end) / 2;

    long long left = max_result(start, mid);
    long long right = max_result(mid + 1, end);

    int go_l = mid, go_r = mid;
    long long result = squ[mid];
    long long height = squ[mid];

    for(int i = 0; i < end - start; i++){
        if (go_l == start){
            go_r++;
            height = (height > squ[go_r])? squ[go_r] : height;
            int made_area = height * (go_r - go_l + 1);
            result = (made_area > result)? made_area: result;
            continue;
        }
        if (go_r == end){
            go_l--;
            height = (height > squ[go_l])? squ[go_l] : height;
            int made_area = height * (go_r - go_l + 1);
            result = (made_area > result)? made_area: result;
            continue;
        }
        if (squ[go_l - 1] < squ[go_r + 1]){
            go_r++;
            height = (height > squ[go_r])? squ[go_r] : height;
            int made_area = height * (go_r - go_l + 1);
            result = (made_area > result)? made_area: result;
            continue;
        }
        else{
            go_l--;
            height = (height > squ[go_l])? squ[go_l] : height;
            int made_area = height * (go_r - go_l + 1);
            result = (made_area > result)? made_area: result;
            continue;
        }
    }
    return max(left, right, result);
}

long long max(long long a, long long b, long long c){
    int tmp = (a > b)? a : b;
    return (tmp > c)? tmp : c;
}
