function createNode() {
    var body = document.body;
    var link = document.createElement("a");
    link.href = "www.google.com";
    link.nodeValue = "Google";
    link.id = "aid";
    link.style.color = "red";
    body.appendChild(link);
}