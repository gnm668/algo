//tabulation notes

function tabFib(n) {
    let table = new Array(n);

    table[0] = 0;
    table[1] = 1;

    for (let i = 2; i <= n; ++i) {
        table[i] = table[i - 1] + table[i -2];
    }

    return table[n];
}

function tabFib2(n) {
    let secondLast = 0;
    let last = 1;

    if (n === 0) return secondLast;
    if (n === 1) return last;

    for (let i = 2; i <= n; ++i) {
            let temp = last;
            last = last + secondLast;
            secondLast = temp;
    }

    return last;
}

//bubble sort notes

function swap(arr, idx1, idx2) {
    let temp = arr[idx1];
    arr[idx1] = arr[idx2];
    arr[idx2] = temp;
}

