
function getBackground() {
    let backGround = document.getElementsByClassName("postContainer");
    for (let i = 0; i < backGround.length; i++) {
        if (backGround[i].id % 2 === 0) {
            return backGround[i].style.background = "#453d3d";
        }
        else if (backGround[i].id % 3 === 0) {
            return backGround[i].style.backgroundColor = "#fefefe"
        }
        else if (backGround[i].id % 5 === 0) {
            return backGround[i].style.backgroundColor = "#d6b6b6"
        }
        else {
            return backGround[i].style.backgroundColor = "#d44a4a";
        }
    }
}

docReady(getBackground());

