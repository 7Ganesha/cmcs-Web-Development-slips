<?php
    $file=$_POST["fname"];
    $selected=$_POST["opt"];
    $file_stat=stat($file);

    switch($selected){
        case "1":
            echo pathinfo($file,PATHINFO_EXTENSION);
            break;
        case "2":
            echo "Last modification time of file    :   ".$file_stat['mtime'];
            break;
        case "3":
            echo "Size of file  :   ".$file_stat['size'];
            break;
        case "4":
            if(unlink($file)){
                echo "file deleted successfully";
            }else{
                echo "file not deleted";
            }
            break;
    }
?>