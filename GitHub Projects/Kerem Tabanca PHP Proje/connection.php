<html>
<body>
<?php
	session_start();
	//database giris işlemleri
	$baglanti=mysqli_connect("localhost","root","","veritabani")
	or die ("Bağlantı Başarısız!"); 
	$baglanti->set_charset("utf8");
	$stmt=$baglanti->prepare('SELECT * FROM USERS');
	$stmt->execute();
	$result = $stmt->get_result();
	$key=false;
	foreach ($result as $row) {
	    if(($_POST["kullanici"]==$row["kullanici_adi"]) and ($_POST["parola"]==$row["sifre"]))
	    	$key=true;
	}
	//kontrol kısmı
	if($key) 
	{
	$_SESSION["giris"] = true;
	$_SESSION["kullanici"] = $_POST["kullanici"]; 
	$_SESSION["parola"] = $_POST["parola"]; 
	echo '<script>alert("Giriş Tamamlandı 5 Saniye İçerisinde Ana Sayfaya yönlendirileceksiniz.")</script>';
	header("refresh:3 url=anasayfa.php");
	}
	else
	{ 
	echo "Kullanıcı adı veya Şifre Yanlış.<br>"; 
	echo "<a href=login.php>Geri dön</a>"; 
	} 
?>
</body>
</html>