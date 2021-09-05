const{test, expect} = require("@jest/globals");
const lib = require("./lib");

test("sum([1, 2]) should be 3", () => {
    expect(lib.sum([1,2])).toBe(3);
});

test("avg([-5, 5]) should be 0", () => {
    expect(lib.avg([-5,5])).toBe(0);
});

test("max([0, 3, 2]) should be 3", () => {
    expect(lib.max([0,3,2])).toBe(3);
});

test("min([1, -5, 3, 2]) should be -5", () => {
    expect(lib.min([1, -5, 3, 2])).toBe(-5);
});

test("med([1, 5, 2, 3, 12]) should be 3", () => {
    expect(lib.med([1, 5, 2, 3, 12])).toBe(3);
});

test("med([1, 9, 3, 12]) should be 6", () => {
    expect(lib.med([1, 9, 3, 12])).toBe(6);
});

test("med([1, 2, 3, 12]) should be 2.5", () => {
    expect(lib.med([1, 2, 3, 12])).toBe(2.5);
});