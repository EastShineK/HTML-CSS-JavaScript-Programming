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
function plus(a, b) {
  console.log(a + b);
}
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
plus(4, 12);
player.sayHi("lynn");
