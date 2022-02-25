const player = {
    name: "nico",
    points: 10,
    fat: true,
};
console.log(player);
console.log(player.name);
console.log(player["name"]);
player.fat = false;
console.log(player);
player.lastName = "potato";
console.log(player);
player.points = player.points + 10;
console.log(player.points);