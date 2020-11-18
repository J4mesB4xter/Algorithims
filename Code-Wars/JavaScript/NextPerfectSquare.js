function findNextSquare(sq) {
    x = Math.sqrt(sq)
    if (Number.isInteger(x)) {
      return (2*x + sq + 1)
    }
    else {
      return "Number provided not perfect square"
    }
  }