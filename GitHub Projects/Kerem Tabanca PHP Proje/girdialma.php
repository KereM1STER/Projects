<html>
<body>
<?php
    $conn=mysqli_connect("localhost","root","","veritabani");
    mysqli_set_charset($conn,"utf8");
?>
    <header>
        <div align="center">
            <img src="https://www.istinye.edu.tr/sites/istinye.edu.tr/files/docs/2018-09/isu_transparan_logo.png" height="120" width="375"><br>
            <i><h2>MESLEK YÜKSEK OKULU</h2>
            <h4>BİLGİSAYAR PROGRAMCILIĞI</h4></i>
            <i><a href="anasayfa.php"> <font color="red" >ANASAYFA</font></a> &nbsp; &nbsp; <a href="hakkımızda.php"><font color="red">HAKKINDA</font></a> &nbsp;  &nbsp; <a href="login.php"> <font color="red">ÜYE GİRİŞİ</font></a></i>&nbsp;  &nbsp;<i><a href="girdialma.php"> <font color="red" >KAYIT OL</font></a></i><br><br><br>
        </div>
        <hr>
    </header>
<center>
    <table>
    <form name="form1" method="POST" action="register.php">
        <h2><i><u><font color="red">KAYIT OL</font></h2></i></u>
        <br>
        <tr bgcolor="cyan">
            <td>Kullanıcı Adı : </td>
            <td><input type="text" name="kullanici1"></td>
        </tr>
        <tr bgcolor="cyan">
            <td>Şifre    :</td> 
            <td><input type="text" name="sifre1"></td>
        </tr>
        <tr bgcolor="cyan">
            <td></td>
            <td><input type="submit" name="gönder" value="KAYIT OL"></td>
        </tr>

</form>
</table>
</center>
<hr>
<footer>
        <div align="center">
        <img src="https://www.istinye.edu.tr/sites/istinye.edu.tr/files/docs/2018-09/isu_transparan_logo.png" height="120" width="375"><br>
        <i><u><a href="https://www.youtube.com/watch?v=f6PMWqlryXc"><font color="red">BÜTÜN HAKLARI KEREM TABANCAYA AİTTİR.</font></a></i></u>
        </div>
</footer>
</body>
</html>