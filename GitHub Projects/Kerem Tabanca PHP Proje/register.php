<?php
$conn=mysqli_connect("localhost", "root","","veritabani");
    mysqli_set_charset($conn,"utf8");
    $user1=$_POST['kullanici1'];
    $pw1=$_POST['sifre1'];
    $sqlekle="INSERT INTO USERS (kullanici_adi,sifre) values ('$user1','$pw1')";
    $sonuc=mysqli_query($conn,$sqlekle);
    if ($sonuc==0){
        echo "<center>Bir hata oluştu</center>";
    }else{
        echo "<center>Başarıyla kayıt edildi</center>";
        header("Location:login.php");
    }
?>