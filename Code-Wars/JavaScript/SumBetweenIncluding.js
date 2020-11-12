function getSum( a,b ) {
    var x = Math.min.apply(a, [a, b])
    var y = Math.max.apply(a, [a, b])
    var z = 0
      while (x<=y) {
        z = z + x;
        x = ++x;
    }
    return z;
  }
  