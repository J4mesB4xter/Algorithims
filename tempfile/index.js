async function main() {

    const response = await fetch('http://localhost:8000/issues.json')
      .then(r => r.json())
    
    console.log(response)

    for (let issue of response.data) {
        const title = document.createElement('p');
        title.innerText = issue.title;

        document.querySelector('.issues').appendChild(title)
    }
  
    // for (let product of products) {
  
    //   const image = document.createElement('img');
    //   image.src = product.image;
  
    //   const title = document.createElement('p');
    //   title.innerText = product.title;
  
    //   const price = document.createElement('p');
    //   price.innerText = product.price;
  
    //   const container = document.createElement('div');
    //   container.classList.add('product');
  
    //   container.appendChild(image)
    //   container.appendChild(title)
    //   container.appendChild(price)
  
    //   document.querySelector('.products').appendChild(container)
    //}
  
  }
  
  main();