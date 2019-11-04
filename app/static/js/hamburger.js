// /* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
// function openNav() {
//     document.getElementById("mySidenav").style.width = "250px";
//     document.getElementById("main").style.marginLeft = "250px";
//     document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
//   }
  
//   /* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
//   function closeNav() {
//     document.getElementById("mySidenav").style.width = "0";
//     document.getElementById("main").style.marginLeft = "0";
//     document.body.style.backgroundColor = "white";
//   }

// /* Set the width of the side navigation to 250px and the left margin of the page content to 250px */
// function openNav() {
//   document.getElementById("mySidenav").style.width = "250px";
//   document.getElementById("main").style.marginLeft = "250px";
// }

// /* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
// function closeNav() {
//   document.getElementById("mySidenav").style.width = "0";
//   document.getElementById("main").style.marginLeft = "0";
// }

/* Set the width of the side navigation to 250px */
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

/*For the Profile Icon*/

function openWindowQR() 
{
  window.open("/qrread","_self");
}

function openWindowProf() 
{
  window.open("/MyProfile","_self");
}

function openWindowLog() 
{
  window.open("/login","_self");
}

function openWin1() 
{
  window.open("https://onedrive.live.com/?authkey=%21AH0mw8qHPuXrqZg&cid=AC759418B23FAA47&id=AC759418B23FAA47%21981&parId=AC759418B23FAA47%21979&o=OneUp/","_self");
}

function openWin2() 
{
  window.open("https://onedrive.live.com/?authkey=%21AOBQ4z%5FYpQWOGaU&cid=AC759418B23FAA47&id=AC759418B23FAA47%21982&parId=AC759418B23FAA47%21979&o=OneUp","_self");
}

function openWin3() 
{
  window.open("https://graduation.udacity.com/confirm/TLA96MF6/","_self");
}

function openWin4() 
{
  window.open("https://www.coursera.org/account/accomplishments/certificate/88QVGK3ZMK5K","_self");
}

function openBranch() 
{
  window.open("/branch","_self");
}


  // Get the modal
  var modal = document.getElementById("myModal");

  // Get the button that opens the modal
  var btn = document.getElementById("myBtn");
  
  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];
  
  // When the user clicks the button, open the modal 
  btn.onclick = function() {
    modal.style.display = "block";
  }
  
  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
    modal.style.display = "none";
  }
  
  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
