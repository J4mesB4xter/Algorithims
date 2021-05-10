const fetch = require('node-fetch');
const faker = require('faker');

function fakeUser() {
  return {
    firstName: faker.name.firstName(),
    lastName: faker.name.lastName(),
    email: faker.internet.email(),
    username: faker.internet.userName(),
    password: faker.internet.password(),
    gender: faker.random.arrayElement(['MALE', 'FEMALE']),
  }
}


async function main() {
  let url = 'http://localhost:8000/users'
  let body = JSON.stringify(fakeUser())
  let options = { method : 'POST', body }
  let response = await fetch(url, options).then(r => r.json());
  console.log(response);
}

main();