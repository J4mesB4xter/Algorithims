function getMiddle(s) {
    console.log(s)
    let x = s.split("").length;
    let y = Number.isInteger(x/2);
    let z = Math.floor(x/2)
    if (x == 1) {
      return s[0];
    } else if (y == false) {
      return s[z]
    } else if (y == true) {
      return s.substring(z-1, z+1)
    }
    }

    