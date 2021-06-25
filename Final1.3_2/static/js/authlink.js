

function jwtuse() {
    let token = localStorage.getItem("jwt-auth-token");
    const xhttp = new XMLHttpRequest();
    console.log(token)

    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            appRes = JSON.parse(this.response)
            console.log(appRes.id)
            console.log(appRes.result)
            if (appRes.result == 200 && document.getElementById('jwtdiv')) {        //에러방지를 위해 'jwtdiv'가 있는지도 조건에 넣었음. 없으면 menu이외의 페이지를 열 때 실행되어 에러 log가 생성됨.
                document.getElementById('jwtdiv').innerText = appRes.id
            }
        }else if (this.readyState == 4 && this.status !== 200) {
            alert("토큰이 유효하지 않습니다")
            location.href='/'
        }
    };

    xhttp.open("GET", "jwtconfirm");
    xhttp.setRequestHeader("Authorization", "Bearer " + token);
    xhttp.send();
}


function jwttodolist() {
    let token = localStorage.getItem("jwt-auth-token");
    const xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            appRes = JSON.parse(this.response)
            

        }else if (this.readyState == 4 && this.status == 422){
            alert("토큰이 유효하지 않습니다")
            location.href='/'
        }
    };

    xhttp.open("GET", "jwttodolist");
    xhttp.setRequestHeader("Authorization", "Bearer " + token);
    xhttp.send();
}


