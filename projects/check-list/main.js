// pop up box
let theTitle;
let selectedDiv = null;


const openBtn = document.getElementById("create-event");
const closeBtn = document.getElementById("closeModal");
const modal = document.getElementById("modal");
const closeBtn2 = document.getElementById("closeModal2");
const modal2 = document.getElementById("modal2");

openBtn.addEventListener("click", ()=> {
    modal.classList.add("open");
    let newdiv = document.createElement("div");
    
    newdiv.style.width = "350px";
    newdiv.style.height= "500px";
    newdiv.style.backgroundColor = "#e35ffd70";
    newdiv.style.borderRadius ="8px";
    newdiv.style.display = "flex";
    newdiv.style.flexDirection = "column";

    let title = document.createElement("h2");
    title.textContent ="new event";
    title.style.textAlign = "center";
    title.style.marginTop = "20px";
    title.style.color = "white"

    let tasks = document.createElement("ul");
    tasks.style.color= "white";
    tasks.style.marginLeft = "30px";
    tasks.style.marginTop = "20px";


    let addtask = document.createElement("button");
    addtask.style.width = "125px";
    addtask.style.height = "50px";
    addtask.textContent = "add task";
    addtask.style.marginTop = "auto";
    
    theTitle = title;

    //selection logit
    newdiv.addEventListener("click", () => {
        if (selectedDiv !== newdiv) {
            if (selectedDiv) {
                selectedDiv.style.border = ''; 
            }
            selectedDiv = newdiv;
            selectedDiv.style.border = '1px solid purple';  
        }
    });
    

    addtask.addEventListener("click", () => {
        
        modal2.classList.add("open2");
    });

    //selection logic

    newdiv.appendChild(title);
    newdiv.appendChild(tasks);
    newdiv.appendChild(addtask);

    document.getElementById("main-screen").appendChild(newdiv);    
});

closeBtn2.addEventListener("click", () => {
    modal2.classList.remove("open2");
    let taskName = document.getElementById("taskname").value;

    if (selectedDiv && taskName) {
        const tasks = selectedDiv.querySelector("ul");
        const currentTaskCount = tasks.childElementCount;

        if (currentTaskCount >= 19) {
            alert("You can only add up to 19 tasks per event!");
            return; 
        }

        let newTask = document.createElement("li");
        newTask.textContent = taskName;
        newTask.style.color = "white";
        tasks.appendChild(newTask);

        newTask.addEventListener("click", () => {
            newTask.style.textDecoration = newTask.style.textDecoration === "line-through" ? "none" : "line-through";
            newTask.style.color = newTask.style.color === "red" ? "white" : "red";
            newTask.style.listStyleType = newTask.style.listStyleType === "none" ? "disc" : "none";
        });
    } else {
        console.error("closeModal2 element not found.");
    }
});

closeBtn.addEventListener("click", ()=>{
    modal.classList.remove("open");
    let eventName = document.getElementById("eventname").value;
    if (eventName) {
        theTitle.textContent = eventName; 
    }
});
// pop up box 


const checkbox = document.getElementById("filter1");
const checkbox2 = document.getElementById("filter2");

checkbox.addEventListener("change", () => {
    if (selectedDiv) {
        const listItems = selectedDiv.querySelector("ul").getElementsByTagName("li");
        Array.from(listItems).forEach(item => {
            if (checkbox.checked && item.style.color === "red") {
                item.style.display = "none";
            } else { 
                item.style.display = "list-item";
            }
        });
    }
});


checkbox2.addEventListener("change", () => {
    if (selectedDiv) {
        const listItems = selectedDiv.querySelector("ul").getElementsByTagName("li");
        Array.from(listItems).forEach(item => {
            if (checkbox2.checked && item.style.color === "white") {
                item.style.display = "none";
            } else { 
                item.style.display = "list-item";
            }
        });
    }
});





