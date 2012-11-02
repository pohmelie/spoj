int main(){
    long long int x, y, s, a1, d, n, i, t;
    scanf("%lld", &t);
    while(t--){
        scanf("%lld %lld %lld", &x, &y, &s);
        n = 2 * s / (x + y);
        d = (x * x - y * y) / (5 - n) / (x + y);
        a1 = x - 2 * d;
        printf("%lld\n", n);
        printf("%lld", a1);
        for(i = 1; i != n; i++){
            a1 = a1 + d;
            printf(" %lld", a1);
        }
        printf("\n");
    }
    return 0;
}
