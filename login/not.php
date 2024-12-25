

<!DOCTYPE html>
<html lang="en" >
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta charset="UTF-8">
<title>CyberVault</title>
<link rel="stylesheet" href="not.css">
<script src="not.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Lato|Short+Stack" rel="stylesheet">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<nav class="main-menu">
      <ul>
        <li>
          <a href="home.php">
            <i class="fa fa-home nav-icon"></i>
            <span class="nav-text">Home</span>
          </a>
        </li>

        
        <li id="uygulamalar-menu">
    <a href="#">
        <i class="fa fa-bomb" style="font-size:24px"></i>
        <span class="nav-text">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Uygulamalar</span>
    </a>
    <ul class="submenu">
    <li><a href="http://127.0.0.1:5003/" target="_blank">RECON</a></li>
    <li><a href="http://127.0.0.1:5004/" target="_blank">NMAP</a></li>
    <li><a href="http://127.0.0.1:5005/" target="_blank">SUBDOMAİN FİNDER</a></li>
    <li><a href="http://127.0.0.1:5006/" target="_blank">DİRSEARCH</a></li>
    <li><a href="http://127.0.0.1:5002/" target="_blank">XSS İNJECTİON</a></li>
    <li><a href="http://127.0.0.1:5001/" target="_blank">SQL İNJECTİON</a></li>
    </ul>
    
</li>
        <li>
          <a href="not.php">
            <i class="fa fa-pen nav-icon"></i>
            <span class="nav-text">Notlar</span>
          </a>
        </li>

        <li>
          <a href="login.php">
          <i class="fa fa-right-from-bracket nav-icon"></i>
            <span class="nav-text">
              Logout
            </span>
          </a>
        </li>
      </ul>
   </nav>
   
   <div class="container">
	<div class="blob-c">
    <div class="blob"></div>
    <div class="blob one"></div>
    <div class="blob two"></div>
    <div class="blob three"></div>
    <div class="blob four"></div>
    <div class="blob five"></div>
    <div class="blob six"></div>
    <div class="blob seven"></div>
  </div>
   <ul>
    <li id="how-it-works-btn"></li>
    <li id="deleteAll"></li>
</ul>

  
  <main id="main">
    <div class="sticky">
      <div class="sticky-header">
        <span class="sticky-header-menu add-button fas fa-plus" title='new sticky'></span>
        <span class="sticky-header-menu notSaved fas fa-check" title='not saved'></span>
        <span class="sticky-header-menu drop-button fas fa-paint-brush" title='change color'></span>
        <div class="dropdown-content-hide">
          <div class="pink-color"></div>
          <div class="yellow-color"></div>
          <div class="green-color"></div>
          <div class="blue-color"></div>
          <div class="purple-color"></div>
        </div>
        <span class="sticky-header-menu remove-button fas fa-trash-alt" title='delete sticky'></span>
      </div>
      <textarea class="sticky-content">
        </textarea>
    </div>
    <div id="createStickyBtn">+</div>
  </main>

</div>


</body>
</html>

