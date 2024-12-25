<!DOCTYPE html>
<html>
<head>
	<title>CyberVault</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
     <form action="login.php" method="post">
     	<h2>CyberVault </h2>
		
     	<?php if (isset($_GET['error'])) { ?>
     		<p class="error"><?php echo $_GET['error']; ?></p>
     	<?php } ?>
     	<label>Kullanıcı Adı</label>
     	<input type="text" name="uname" placeholder="User Name"><br>

     	<label>Şifre</label>
     	<input type="password" name="password" placeholder="Password"><br>

     	<button type="submit">Giriş Yap</button>
          <a href="signup.php" class="ca">Hesap Oluştur</a>
     </form>
</body>
</html>