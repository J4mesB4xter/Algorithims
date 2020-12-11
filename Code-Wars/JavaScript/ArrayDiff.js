function ArrayDiff(a, b) {
    let x = [];
    var y;
    for (y in a) {
        if (b.includes(y)) {
            continue
        } else {
            x.append(y);
        }
    }
}