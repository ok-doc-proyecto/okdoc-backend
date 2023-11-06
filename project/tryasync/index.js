let url = "ws://localhost:7000/ws/async/";
var socket = new WebSocket(url);
socket.onmessage = function (event) {
  var data = JSON.parse(event.data);
  var wPsep;
  if (data.funcion === "f1") {
    wPsep = "/*/";
    console.log(wPsep);
    funcion1(socket, data, wPsep);
  } else {
    wPsep = "/?/";
    console.log(wPsep);
    funcion1(socket, data, wPsep);
  }
};

function funcion1(pSocket, pData, pSep) {
  console.log(pData);
  let acum = document.querySelector("#app").innerText;
  let acum2 = pData.message;
  let acum3 = acum + pSep + acum2;
  document.querySelector("#app").innerText = acum3;
  let xjson = {
    numero: pData.message,
    message: "mensaje" + ":" + pData.message,
    username: "de prueba",
  };
  pSocket.send(JSON.stringify(xjson));
  console.log(xjson);
}
