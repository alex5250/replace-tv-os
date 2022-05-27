


function exit_from_app(){
    console.log("User called exit. Calling launcher.");
    window.close();
    eel.exit_from_app(1, 2); // This calls the Python function that was decorated

}


function install_os(){
    window.close();
    eel.install_os();
}



function get_drives_names(){
    alert(eel.scan_for_drives()());

}
async function run() {
    let n = await eel.scan_for_drives()();
    var select = document.getElementById("select_drive");
    var options = n;
for(var i = 0; i < options.length; i++) {
    var opt = options[i];
    var el = document.createElement("option");
    el.textContent = opt;
    el.value = opt;
    select.appendChild(el);
}
}

function download_install_os() {
    //var document=document.getElementById("install");
    //document.remove();
    var modal = document.getElementById("myModal");
modal.style.display = "block";
window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
    var select = document.getElementById("select_drive");
    var text= select.options[select.selectedIndex].text;
    eel.clone_install_os(text);

}


// Get the modal
