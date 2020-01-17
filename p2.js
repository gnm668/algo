function tabFib(n) {
    let table = new Array(n);

    table[0] = 0;
    table[1] = 1;

    for (let i = 0; i <= n; ++i) {
        table[i] = table[i - 1] + table[i -2];
    }

    return table[n];
}