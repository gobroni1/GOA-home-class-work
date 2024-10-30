document.getElementById("one").addEventListener("click", () => calculator("1"));
document.getElementById("two").addEventListener("click", () => calculator("2"));
document.getElementById("three").addEventListener("click", () => calculator("3"));
document.getElementById("four").addEventListener("click", () => calculator("4"));
document.getElementById("five").addEventListener("click", () => calculator("5"));
document.getElementById("six").addEventListener("click", () => calculator("6"));
document.getElementById("seven").addEventListener("click", () => calculator("7"));
document.getElementById("eight").addEventListener("click", () => calculator("8"));
document.getElementById("nine").addEventListener("click", () => calculator("9"));
document.getElementById("minus").addEventListener("click", () => calculator("-"));
document.getElementById("plus").addEventListener("click", () => calculator("+"));
document.getElementById("equal").addEventListener("click", () => calculator("="));
document.getElementById("C").addEventListener("click", () => calculator("C"));

const possibleNums =["1","2","3","4","5","6","7","8","9"];
const possibleOps = ["-","+"];
let conNum = [];

let prs = [];
let ops = [];
let res;


function calculator (input) {
    if (possibleNums.includes(input)) {
        conNum.push(input);
    }else if (possibleOps.includes(input)){
        prs.push(parseInt(conNum.join("")));
        conNum = [];
        ops.push(input);
    }else if (input === "=") {
        prs.push(parseInt(conNum.join("")));
        res = prs[0];
        for (let i = 0; i < ops.length; i++) {
            if (ops[i] === "-") {
                res -= prs[i + 1];
            } else if (ops[i] === "+") {
                res += prs[i + 1];
            }
        }
        console.log(res);
    }else if (input === "C") {
        conNum = [];
        prs = [];
        ops = [];
        res = 0;
        console.log("all clear")
    }
}