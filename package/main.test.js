const {test, expect} = require("@jest/globals");
const {spawn} = require("child_process");

test("Insufficient params", () => {
    const main = spawn("node", ["main.js", "agv"]);
    const outputs = [];
    main.stdout.on("data", (output) => {
        outputs.push(output);
    });
    main.stdout.on("end", () => {
        const output = outputs.join("").trim();
        expect(output).toBe("Insufficient parameter!");
    });
});

test("Wrong command", () => {
    const main = spawn("node", ["main.js", "count", "0"]);
    const outputs = [];
    main.stdout.on("data", (output) => {
        outputs.push(output);
    });
    main.stdout.on("end", () => {
        const output = outputs.join("").trim();
        expect(output).toBe("Wrong command!");
    });
});

test("repeat test 1 correct", () => {
    const main = spawn("node", ["main.js", "sum", "4", "7", "3@4"]);
    const outputs = [];
    main.stdout.on("data", (output) => {
        outputs.push(output);
    });
    main.stdout.on("end", () => {
        const output = outputs.join("").trim();
        var outputNumber = Number(output);
        expect(outputNumber).toBe(23);
        //expect(output).toBe(23);
    });
});

test("repeat test 2 correct", () => {
    const main = spawn("node", ["main.js", "min", "5", "7", "3@4", "-5@7"]);
    const outputs = [];
    main.stdout.on("data", (output) => {
        outputs.push(output);
    });
    main.stdout.on("end", () => {
        const output = outputs.join("").trim();
        var outputNumber = Number(output);
        expect(outputNumber).toBe(-5);
        //expect(output).toBe(23);
    });
});

test("repeat test 3 correct", () => {
    const main = spawn("node", ["main.js", "med", "4", "7", "3@2", "2@2"]);
    const outputs = [];
    main.stdout.on("data", (output) => {
        outputs.push(output);
    });
    main.stdout.on("end", () => {
        const output = outputs.join("").trim();
        var outputNumber = Number(output);
        expect(outputNumber).toBe(3);
        //expect(output).toBe(23);
    });
});

test("repeat test 4 correct", () => {
    const main = spawn("node", ["main.js", "avg", "2", "12@4"]);
    const outputs = [];
    main.stdout.on("data", (output) => {
        outputs.push(output);
    });
    main.stdout.on("end", () => {
        const output = outputs.join("").trim();
        var outputNumber = Number(output);
        expect(outputNumber).toBe(10);
        //expect(output).toBe(23);
    });
});

test("repeat test 5 correct", () => {
    const main = spawn("node", ["main.js", "max", "2", "17@4", "16@2", "11@5", "4@10"]);
    const outputs = [];
    main.stdout.on("data", (output) => {
        outputs.push(output);
    });
    main.stdout.on("end", () => {
        const output = outputs.join("").trim();
        var outputNumber = Number(output);
        expect(outputNumber).toBe(17);
        //expect(output).toBe(23);
    });
});

test("repeat test 6 correct", () => {
    const main = spawn("node", ["main.js", "max", "2", "17@4", "16@0", "11@5", "4@10"]);
    const outputs = [];
    main.stdout.on("data", (output) => {
        outputs.push(output);
    });
    main.stdout.on("end", () => {
        const output = outputs.join("").trim();
        expect(output).toBe("Invalid repeat!");
        //expect(output).toBe(23);
    });
});