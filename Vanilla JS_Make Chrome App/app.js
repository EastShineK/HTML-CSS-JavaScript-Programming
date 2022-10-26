const player = {
  name: "nico",
  points: 10,
  fat: true,
  sayHi: function (otherPersonName) {
    console.log("hello " + otherPersonName + " nice to meet you!");
  },
};
function sayHello(nameOfPerson, age) {
  console.log("Hello my name is " + nameOfPerson + " and I'm " + age + " old");
}

const calculator = {
  plus: function (a, b) {
    console.log(a + b);
  },
  minus: function (a, b) {
    console.log(a - b);
  },
  times: function (a, b) {
    console.log(a * b);
  },
  divide: function (a, b) {
    console.log(a / b);
  },
  power: function (a, b) {
    console.log(a ** b);
  },
};
calculator.plus(10, 5);
calculator.minus(10, 5);
calculator.times(10, 5);
calculator.divide(10, 5);
calculator.power(2, 2);

console.log(player);
console.log(player.name);
console.log(player["name"]);
player.fat = false;
console.log(player);
player.lastName = "potato";
console.log(player);
player.points = player.points + 10;
console.log(player.points);
sayHello("nico", 22);
player.sayHi("lynn");
